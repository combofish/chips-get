<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>数据导入</title>
    <link rel="stylesheet" type="text/css" href="css/divForm.css">
</head>
<body class="bodyImg">
<h1>数据导入</h1>
<div class="divForm">
    <br/>
    <br/>
    <br/>
<%--    LocateTurn_war_exploded/ --%>
    <form method="post" action="/LocateTurn_war_exploded/UploadFileServlet" enctype="multipart/form-data">
        选择要导入的数据文件:
        <input type="file" name="uploadFile"/>
        <input type="submit" value="开始转换"/>
    </form>
</div>
</body>
</html>