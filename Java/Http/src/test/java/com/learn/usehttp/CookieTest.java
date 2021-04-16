package com.learn.usehttp;

import okhttp3.*;
import org.jetbrains.annotations.NotNull;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CookieTest {
    // List<Cookie> cookies = new ArrayList<>();
    Map<String, List<Cookie>> cookies = new HashMap<>();

    @Test
    void cookieTest() {
        OkHttpClient okHttpClient = new OkHttpClient.Builder()
                .cookieJar(new CookieJar() {
                    @Override
                    public void saveFromResponse(@NotNull HttpUrl httpUrl, @NotNull List<Cookie> list) {
                        // cookies.clear();
                        // cookies.addAll(list);
                        cookies.put(httpUrl.host(),list);
                    }

                    @NotNull
                    @Override
                    public List<Cookie> loadForRequest(@NotNull HttpUrl httpUrl) {
                        List<Cookie> cookies = CookieTest.this.cookies.get(httpUrl.host());
                        return cookies==null?new ArrayList<>():cookies;
                        /**cn
                        if (httpUrl.host().equals("https://www.wanandroid.com")){
                            return cookies;
                        }
                        // return null;
                        return new ArrayList<>();
                         */
                    }
                }).build();
        FormBody formBody = new FormBody.Builder().add("username", "larryLi")
                .add("password", "password").build();
        Request request = new Request.Builder().url("https://www.wanandroid.com/user/login").post(formBody).build();
        Call call = okHttpClient.newCall(request);

        try{
            Response response = call.execute();
            System.out.println(response.isSuccessful());
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }

        request = new Request.Builder().url("https://www.wanandroid.com/lg/collect/list/0/json").build();
        call = okHttpClient.newCall(request);

        try{
            Response response = call.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
