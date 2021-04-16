package com.learn.usehttp;

import okhttp3.*;
import org.jetbrains.annotations.NotNull;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.IOException;

public class CacheTest {

    @Test
    void cacheTest() {
        OkHttpClient okHttpClient = new OkHttpClient.Builder()
                .cache(new Cache(new File("/home/larry/Desktop/"),1024 * 1024))
                .addInterceptor(new Interceptor() {
            @NotNull
            @Override
            public Response intercept(@NotNull Chain chain) throws IOException {
                // return chain.proceed(chain.request());
                Request request = chain.request().newBuilder().addHeader("OS","Android").build();
                Response response = chain.proceed(request);
                return response;
            }
        }).addNetworkInterceptor(
                new Interceptor() {
                    @NotNull
                    @Override
                    public Response intercept(@NotNull Chain chain) throws IOException {
                        System.out.println(chain.request().header("OS"));
                        return chain.proceed(chain.request());
                    }
                }
        ).build();

        Request request = new Request.Builder().url("http://www.httpbin.org/get?a=1").build();
        Call call = okHttpClient.newCall(request);

        try{
            Response response = call.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
