package com.learn.usehttp;

import okhttp3.*;
import org.jetbrains.annotations.NotNull;
import org.junit.jupiter.api.Test;

import java.io.IOException;


class LearnTest {
    OkHttpClient okHttpClient = new OkHttpClient();

    @Test
    public void Test(){
        Request request = new Request.Builder().url("http://httpbin.org/get?a=1").build();
        Call call = okHttpClient.newCall(request);
        try {
            Response response = call.execute();
            System.out.println("getSync" + response.body().string());
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    @Test
    public void getSync(){
        Request request = new Request.Builder().url("http://httpbin.org/get?a=1").build();
        Call call = okHttpClient.newCall(request);
        try {
            Response response = call.execute();
            System.out.println(response.body().string());
        }catch (Exception e){
            e.printStackTrace();
        }
    }


    @Test
    public void getAsync(){
        Request request = new Request.Builder().url("http://www.httpbin.org/get?a=1").build();
        Call call = okHttpClient.newCall(request);
        call.enqueue(new Callback() {
            @Override
            public void onFailure(@NotNull Call call, @NotNull IOException e) {
                System.out.println("fail");
            }

            @Override
            public void onResponse(@NotNull Call call, @NotNull Response response) throws IOException {
                if (response.isSuccessful()){
                    System.out.println("success");
                    System.out.println(response.body().string());
                }
                System.out.println("success");
            }
        });
    }

    @Test
    public void postSync(){
        FormBody formBody = new FormBody.Builder().add("user", "combofish").build();
        Request request = new Request.Builder().url("http://www.httpbin.org/post").post(formBody).build();
        Call call = okHttpClient.newCall(request);
        new Thread(){
            @Override
            public void run() {
                try {
                    Response response = call.execute();
                    System.out.println(response.body().string());
                    System.out.println("success");
                }catch (IOException e){
                    e.printStackTrace();
                }
            }
        }.start();

    }

    @Test
    public void postSync1(){
        FormBody formBody = new FormBody.Builder().add("user", "combofish").build();
        Request request = new Request.Builder().url("http://www.httpbin.org/post").post(formBody).build();
        Call call = okHttpClient.newCall(request);
                try {
                    Response response = call.execute();
                    System.out.println(response.body().string());
                    System.out.println("success");
                }catch (IOException e){
                    e.printStackTrace();
                }

    }

    @Test
    public void postAsync(){
        FormBody formBody = new FormBody.Builder().add("user", "combofish").build();
        Request request = new Request.Builder().url("http://www.httpbin.org/post").post(formBody).build();
        Call call = okHttpClient.newCall(request);
        call.enqueue(new Callback() {
            @Override
            public void onFailure(@NotNull Call call, @NotNull IOException e) {
                System.out.println("Fail");
            }

            @Override
            public void onResponse(@NotNull Call call, @NotNull Response response) throws IOException {
                System.out.println("success");
            }
        });
    }
}