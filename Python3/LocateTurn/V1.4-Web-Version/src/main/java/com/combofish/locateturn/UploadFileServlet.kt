package com.combofish.locateturn


import mu.KotlinLogging
import org.apache.commons.fileupload.FileItem
import org.apache.commons.fileupload.disk.DiskFileItemFactory
import org.apache.commons.fileupload.servlet.ServletFileUpload
import java.io.*
import java.nio.charset.Charset

import javax.servlet.annotation.WebServlet
import javax.servlet.http.HttpServlet
import kotlin.Throws
import javax.servlet.ServletException
import javax.servlet.http.HttpServletRequest
import javax.servlet.http.HttpServletResponse


@WebServlet(name = "UploadFileServlet", value = ["/UploadFileServlet"])
class UploadFileServlet : HttpServlet() {
    private val serialVersionUID = 1L
    private val logger = KotlinLogging.logger {}

    // 上传文件存储目录
    private val UPLOAD_DIRECTORY = "upload/Data"

    // 上传配置
    private val MEMORY_THRESHOLD = 1024 * 1024 * 3 // 3MB
    private val MAX_FILE_SIZE = 1024 * 1024 * 40 // 40MB
    private val MAX_REQUEST_SIZE = 1024 * 1024 * 50 // 50MB

    /**
     * 上传数据及保存文件
     */
    @Throws(ServletException::class, IOException::class)
    override fun doPost(request: HttpServletRequest, response: HttpServletResponse) {
        // 检测是否为多媒体上传
        if (!ServletFileUpload.isMultipartContent(request)) {
            // 如果不是则停止
            val writer: PrintWriter = response.getWriter()
            writer.println("Error: 表单必须包含 enctype=multipart/form-data")
            writer.flush()
            return
        }

        // 配置上传参数
        val factory = DiskFileItemFactory()
        // 设置内存临界值 - 超过后将产生临时文件并存储于临时目录中
        factory.setSizeThreshold(MEMORY_THRESHOLD)
        // 设置临时存储目录
        factory.setRepository(File(System.getProperty("java.io.tmpdir")))
        val upload = ServletFileUpload(factory)

        // 设置最大文件上传值
        upload.setFileSizeMax(MAX_FILE_SIZE.toLong())

        // 设置最大请求值 (包含文件和表单数据)
        upload.setSizeMax(MAX_REQUEST_SIZE.toLong())

        // 中文处理
        upload.setHeaderEncoding("UTF-8")

        // 构造临时路径来存储上传的文件
        // 这个路径相对当前应用的目录
        val projectPath = servletContext.getRealPath("/").toString()
        logger.info { ">>> project $projectPath" }
        println(">>> projectPath: $projectPath")
        val uploadPath: String =
            servletContext.getRealPath("/").toString() + UPLOAD_DIRECTORY
        //servletContext.getRealPath("/").toString() + File.separator + UPLOAD_DIRECTORY

        // 如果目录不存在则创建
        val uploadDir = File(uploadPath)
        if (!uploadDir.exists()) {
            uploadDir.mkdir()
        }
        try {
            // 解析请求的内容提取文件数据
            val formItems: List<FileItem> = upload.parseRequest(request)
            if (formItems != null && formItems.size > 0) {
                // 迭代表单数据
                for (item in formItems) {
                    // 处理不在表单中的字段
                    if (!item.isFormField()) {
                        val fileName: String = File(item.getName()).getName()
                        val filePath = uploadPath + File.separator + fileName
                        val storeFile = File(filePath)
                        // 在控制台输出文件的上传路径
                        logger.info { filePath }
                        println(filePath)
                        if (fileName.equals("")) {
                            logger.info { "Null fileName!!!" }
                            println("null FileName")
                            getServletContext().getRequestDispatcher("/message.jsp").forward(
                                request, response
                            )
                        }
                        // 保存文件到硬盘
                        item.write(storeFile)


                        // 返回消息
                        request.setAttribute(
                            "message",
                            "文件上传成功!"
                        )

                        // 处理文件
                        var newFileName = "${fileName.split('.')[0]}.txt"
                        var newFilePath = uploadPath + File.separator + "Res" + File.separator + newFileName
                        logger.info { " " }
                        logger.info { ">>> NewFilePath:$newFilePath" }
                        logger.info { ">>> UploadPath:$uploadPath" }
                        logger.info { ">>> FilePath:$filePath" }
                        processFile(projectPath)

                        deleteExcelFile(filePath)
                        downloadFile(request, response, newFileName)
                        deleteExcelFile(newFilePath)
                        //response.sendRedirect("/DownloadServlet?fileName=${newFileName}")
                        //request.getRequestDispatcher("/DownloadServlet?fileName=${newFilePath}").forward(request,response)
                    }
                }
            }
        } catch (ex: Exception) {
            request.setAttribute(
                "message",
                "错误信息: " + ex.message
            )
        }

        // 跳转到 message.jsp

        /**
        getServletContext().getRequestDispatcher("/message.jsp").forward(
        request, response
        )
         */

    }

    private fun downloadFile(request: HttpServletRequest, response: HttpServletResponse, newFileName: String) {
        var filename = newFileName
        //设置响应的头部属性content-disposition值为attachment
        //使用filename来指定文件名
        val bytes = filename.toByteArray(charset("utf-8"))
        //http协议规定浏览器只能接受ISO8859-1类型的字节数据
        filename = String(bytes, Charset.forName("ISO8859-1"))
        response.setHeader("content-disposition", "attachment;filename=$filename")
        //获取连接服务器资源文件的输入流
        var filePath = "/upload/Data/Res" + File.separator + newFileName
        logger.info { ">>>Download File Path: $filePath" }
        val isFile = request.servletContext.getResourceAsStream(filePath)

        //获取输出流
        val os = response.outputStream
        //将输入流中的数据写到输出流中
        var length = -1
        val buffer = ByteArray(1024)
        while (isFile.read(buffer).also { length = it } != -1) {
            os.write(buffer, 0, length)
        }
        os.close()
        isFile.close()
    }

    private fun processFile(filePath: String) {
        try {
            val shpath = "upload/turnLocate.sh"
            val runtime = Runtime.getRuntime()
            val arrayListOf = arrayOf<String>("$filePath$shpath", "${filePath}upload")
            // val pro: Process = runtime.exec(filePath +File.separator + shpath)
            val pro: Process = runtime.exec(arrayListOf)
            val status = pro.waitFor()
            if (status != 0) {
                logger.info { "Failed to call shell's command" }
                //println("Failed to call shell's command")
            }
            val br = BufferedReader(InputStreamReader(pro.inputStream))
            val strbr = StringBuffer()
            var line: String?
            while (br.readLine().also { line = it } != null) {
                strbr.append(line).append("\n")
            }
            val result = strbr.toString()
            logger.info { "result $result" }
            //println("result $result")


        } catch (e: java.lang.Exception) {
            e.printStackTrace()
        }
    }

    private fun deleteExcelFile(filePath: String) {
        val file = File(filePath)
        if (file.delete()) {
            logger.info { "delete $filePath" }
            println("delete $filePath")
        } else {
            logger.info { "no exists $filePath" }
            println("no exists $filePath")
        }
    }

}