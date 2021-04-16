package com.learn.usehttp;

import com.google.gson.internal.bind.util.ISO8601Utils;
import okhttp3.*;
import org.junit.jupiter.api.Test;
import retrofit2.Call;
import retrofit2.Response;
import retrofit2.Retrofit;
import okhttp3.ResponseBody;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

import static org.junit.jupiter.api.Assertions.*;

class UploadServiceTest {

    Retrofit retrofit = new Retrofit.Builder().baseUrl("http://www.httpbin.org").build();
    UploadService uploadService = retrofit.create(UploadService.class);

    @Test
    public void test() throws IOException{
        File file1 = new File("/home/larry/Desktop/use.txt");
        MultipartBody.Part part = MultipartBody.Part.createFormData("file1",
                "use.txt", RequestBody.create(file1, MediaType.parse("text/plain")));

        Call<ResponseBody> call = uploadService.upload(part);
        System.out.println(call.execute().body().string());
    }

    @Test
    void testDownload() throws IOException{
        String link = "https://phoenixnap.dl.sourceforge.net/project/linuxedfschedul/tasks.tar.bz2";
        Response<ResponseBody> response = uploadService.download(link).execute();
        InputStream inputStream = response.body().byteStream();

        FileOutputStream fileOutputStream = new FileOutputStream("/home/larry/Desktop/a.jar");
        int len;
        byte[] buffer = new byte[4096];

        while((len = inputStream.read(buffer)) != -1){
            fileOutputStream.write(buffer,0,len);
        }
        fileOutputStream.close();
        inputStream.close();
    }

    @Test
    void testRxDownload() throws IOException{
        String link = "https://phoenixnap.dl.sourceforge.net/project/linuxedfschedul/tasks.tar.bz2";
        Response<ResponseBody> response = uploadService.rx_download(link).execute();
        InputStream inputStream = response.body().byteStream();
        FileOutputStream fileOutputStream = new FileOutputStream("/home/larry/Desktop/a.jar");
        int len;
        byte[] buffer = new byte[4096];

        while((len = inputStream.read(buffer)) != -1){
            fileOutputStream.write(buffer,0,len);
        }
        fileOutputStream.close();
        inputStream.close();
    }

}