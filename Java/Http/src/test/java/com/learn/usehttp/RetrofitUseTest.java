package com.learn.usehttp;

import okhttp3.FormBody;
import okhttp3.ResponseBody;
import org.junit.jupiter.api.Test;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

import java.io.IOException;

public class RetrofitUseTest {
    private Retrofit retrofit1;

    @Test
    void retrofitTest() {
        retrofit1 = new Retrofit.Builder().baseUrl("http://www.httpbin.org").build();
        HttpbinService httpbinService = retrofit1.create(HttpbinService.class);
        Call<ResponseBody> call = httpbinService.post("larryLi", "password");
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                System.out.println("success");
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable throwable) {
                System.out.println("fial");
            }
        });
    }

    @Test
    void retrofitTest2() {
        retrofit1 = new Retrofit.Builder().baseUrl("http://www.httpbin.org").build();
        HttpbinService httpbinService = retrofit1.create(HttpbinService.class);
        Call<ResponseBody> call = httpbinService.post("larryLi", "password");

        try{
            Response<ResponseBody> response = call.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }

    }


    @Test
    void retrofitTest3_annotation() {
        retrofit1 = new Retrofit.Builder().baseUrl("http://www.httpbin.org").build();
        HttpbinService httpbinService = retrofit1.create(HttpbinService.class);
        FormBody formBody = new FormBody.Builder().add("user", "combofish").build();

        Call<ResponseBody> responseBodyCall = httpbinService.postBody(formBody);

        try{
            Response<ResponseBody> response =responseBodyCall.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }

    }

    @Test
    void retrofitTest3_pathTest() {
        retrofit1 = new Retrofit.Builder().baseUrl("http://www.httpbin.org").build();
        HttpbinService httpbinService = retrofit1.create(HttpbinService.class);

        Call<ResponseBody> responseBodyCall = httpbinService.postPath("post");

        try{
            Response<ResponseBody> response =responseBodyCall.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }

    }

    @Test
    void retrofitTest3_pathTest2() {
        retrofit1 = new Retrofit.Builder().baseUrl("http://www.httpbin.org").build();
        HttpbinService httpbinService = retrofit1.create(HttpbinService.class);

        Call<ResponseBody> responseBodyCall = httpbinService.postPath("post","larryLi","password");

        try{
            Response<ResponseBody> response =responseBodyCall.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }

    }

    @Test
    void retrofitTest3_postWithHeader() {
        retrofit1 = new Retrofit.Builder().baseUrl("http://www.httpbin.org").build();
        HttpbinService httpbinService = retrofit1.create(HttpbinService.class);

        Call<ResponseBody> responseBodyCall = httpbinService.postWithHeader();

        try{
            Response<ResponseBody> response =responseBodyCall.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    @Test
    void retrofitTest3_postUrl() {
        retrofit1 = new Retrofit.Builder().baseUrl("http://www.httpbin.org").build();
        HttpbinService httpbinService = retrofit1.create(HttpbinService.class);

        Call<ResponseBody> responseBodyCall = httpbinService.postUrl("http://www.httpbin.org/post");

        try{
            Response<ResponseBody> response =responseBodyCall.execute();
            System.out.println(response.body().string());
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
