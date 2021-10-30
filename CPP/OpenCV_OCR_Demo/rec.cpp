#include <algorithm>
#include <leptonica/allheaders.h>
#include <opencv2/opencv.hpp>
#include <opencv4/opencv2/calib3d.hpp>
#include <opencv4/opencv2/core.hpp>
#include <opencv4/opencv2/core/hal/interface.h>
#include <opencv4/opencv2/core/types.hpp>
#include <opencv4/opencv2/features2d.hpp>
#include <opencv4/opencv2/highgui.hpp>
#include <opencv4/opencv2/imgcodecs.hpp>
#include <opencv4/opencv2/imgproc.hpp>
#include <opencv4/opencv2/objdetect.hpp>
#include <opencv4/opencv2/videoio.hpp>
#include <string>
#include <tesseract/baseapi.h>
#include <tesseract/publictypes.h>
#include <vector>

using namespace cv;
using std::cout;
using std::endl;
using std::string;
using std::vector;

// 预处理图像
void preProcessing(Mat &, Mat &);

// 获取边界
vector<Point> getContours(Mat &, Mat &);

// 对边界点排序
vector<Point> reorder(vector<Point>);

// 裁剪图片
Mat getWarp(Mat &, vector<Point>, float, float);

// 画出边框的四个点
void drawPoints(Mat &, vector<Point>, Scalar);

// 调用 tesseract 识别图片
void outputRecResult(const Mat &);

int main() {
  string path = "use01.jpg";
  Mat img = imread(path);
  Mat imgClone, imgThre, imgWarp;

  // 预处理图像
  resize(img, img, Size(), 0.25, 0.25);
  imgClone = img.clone();
  preProcessing(img, imgThre);

  // 获取最大矩形的四个角的坐标
  vector<Point> initPoints = getContours(imgThre, imgThre);
  // cout << "initPoints.size(): " << initPoints.size() << endl;

  // 对坐标进行排序
  vector<Point> orderedPoints = reorder(initPoints);

  // 画出边框的四个点
  drawPoints(img, orderedPoints, Scalar(0, 0, 255));

  // 裁剪图形
  float w = 400, h = 640;
  imgWarp = getWarp(imgClone, orderedPoints, w, h);

  imshow("Image", img);
  imshow("Image Dil", imgThre);
  imshow("Image Warp", imgWarp);

  imwrite("scan01.jpg", imgWarp);

  outputRecResult(imgWarp);
  waitKey(0);
  return 0;
}

void preProcessing(Mat &img, Mat &imgDil) {
  Mat imgGray, imgBlur, imgCanny;

  cvtColor(img, imgGray, COLOR_BGR2GRAY);
  GaussianBlur(imgGray, imgBlur, Size(3, 3), 3, 0);
  Canny(imgBlur, imgCanny, 75, 200);

  Mat kernel = getStructuringElement(MORPH_RECT, Size(3, 3));
  dilate(imgCanny, imgDil, kernel);

  imshow("Image Gray", imgGray);
  imshow("Image Blur", imgBlur);
  imshow("Image Canny", imgCanny);
}

vector<Point> getContours(Mat &img, Mat &imgDil) {
  vector<vector<Point>> contours;
  vector<Vec4i> hierarchy;

  findContours(imgDil, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

  // 储存最大的边界框的四个点
  vector<Point> biggest;

  vector<vector<Point>> conPoly(contours.size());
  vector<Rect> boundRect(contours.size());

  // cout << "contours.size(): " << contours.size() << endl;
  int maxArea = 0;

  for (int i = 0; i < contours.size(); i++) {
    // 计算轮廓面积
    int area = contourArea(contours[i]);
    // cout << area << endl;

    // 找到最大的轮廓
    if (area > 1000) {
      // 计算轮廓周周长
      auto peri = arcLength(contours[i], true);
      approxPolyDP(contours[i], conPoly[i], 0.02 * peri, true);

      // 找到矩形
      int objCor = conPoly[i].size();
      if (4 == objCor && area > maxArea) {
        drawContours(img, conPoly, i, Scalar(255, 0, 255), 2);
        for (auto p : conPoly[i])
          biggest.push_back(p);

        maxArea = area;
      }
    }
  }
  return biggest;
}

vector<Point> reorder(vector<Point> initPoints) {
  vector<Point> orderedPoints;
  vector<int> sumPoints, subPoints;

  for (auto p : initPoints) {
    sumPoints.push_back(p.x + p.y);
    subPoints.push_back(p.x - p.y);
  }

  orderedPoints.push_back(
      initPoints[std::min_element(sumPoints.begin(), sumPoints.end()) -
                 sumPoints.begin()]);
  orderedPoints.push_back(
      initPoints[std::max_element(subPoints.begin(), subPoints.end()) -
                 subPoints.begin()]);
  orderedPoints.push_back(
      initPoints[std::min_element(subPoints.begin(), subPoints.end()) -
                 subPoints.begin()]);
  orderedPoints.push_back(
      initPoints[std::max_element(sumPoints.begin(), sumPoints.end()) -
                 sumPoints.begin()]);

  return orderedPoints;
}

void drawPoints(Mat &img, vector<Point> points, Scalar c) {
  for (int i = 0; i < points.size(); i++) {
    circle(img, points[i], 10, c, FILLED);
    putText(img, std::to_string(i), points[i], FONT_HERSHEY_PLAIN, 4, c, 4);
  }
}

Mat getWarp(Mat &img, vector<Point> docPoints, float w, float h) {
  Point2f src[4];
  for (int i = 0; i < 4; i++)
    src[i] = docPoints[i];

  Point2f dst[4] = {{0.0f, 0.0f}, {w, 0.0f}, {0.0f, h}, {w, h}};

  Mat imgWarp;
  Mat matrix = getPerspectiveTransform(src, dst);
  warpPerspective(img, imgWarp, matrix, Size(w, h));
  return imgWarp;
}

void outputRecResult(const Mat &img) {

  tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();

  if (api->Init(NULL, "eng", tesseract::OEM_LSTM_ONLY)) {
    cout << "Could not initialize tesseract." << endl;
    exit(1);
  }

  api->SetPageSegMode(tesseract::PSM_AUTO);
  api->SetImage(img.data, img.cols, img.rows, 3, img.step);
  string outText = string(api->GetUTF8Text());
  cout << outText;
  api->End();
}
