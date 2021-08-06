
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>文件上传结果</title>
    <style>
        h2 {
            text-align: center;
        }
        p {
            text-align: center;
        }

        span {
            color: red;
        }
    </style>
</head>
<body>
<h2>数据导入失败</h2>
<p>
    <span id="time">3</span>秒后返回数据导入页面...
</p>
<script>
    // 获取span对象
    var time = document.getElementById("time");
    // 设置秒数
    var second = 3;

    // 定义秒数显示方式
    function showTime() {
        // 执行1次秒数自减
        second--;
        // 判断，如果秒数小于0则跳转页面
        if (second <= 0) {
            // 设置href
            location.href = "/LocateTurn";
        }
        // 更改span标签的显示内容
        time.innerHTML = second.toString();
    }

    // 定义定时器，每隔1秒执行一次showTime方法
    setInterval(showTime, 1000);
</script>
</body>
</html>