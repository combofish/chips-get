package com.learn.usehttp;

import okhttp3.*;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.IOException;

public class uploadFileTest {

    @Test
    public void uploadFileTest(){
        OkHttpClient okHttpClient = new OkHttpClient();
        File file = new File("/home/larry/Desktop/use.txt");
        RequestBody requestBody = RequestBody.create(file, MediaType.parse("text/plain"));
        MultipartBody multipartBody = new MultipartBody.Builder()
                .addFormDataPart("file1", file.getName(), requestBody)
                .addFormDataPart("user","combofish")
                .build();
        Request request = new Request.Builder().url("http://www.httpbin.org/post").post(multipartBody).build();
        Call call = okHttpClient.newCall(request);
        try{
            Response response = call.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    @Test
    public void jsonTest(){
        OkHttpClient okHttpClient = new OkHttpClient();
        RequestBody requestBody = RequestBody.create("{\"a\":1,\"b\":2}",MediaType.parse("application/json"));
        Request request = new Request.Builder().url("http://www.httpbin.org/post").post(requestBody).build();
        Call call = okHttpClient.newCall(request);
        try{
            Response response = call.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
