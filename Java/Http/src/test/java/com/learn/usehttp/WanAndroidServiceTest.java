package com.learn.usehttp;

import com.google.gson.Gson;
import com.learn.usehttp.pojo.JsonRootBean;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import org.junit.jupiter.api.Test;
import retrofit2.Call;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

class WanAndroidServiceTest {
    private Retrofit retrofit1;

    @Test
    void loginTestWithGson() throws IOException{
        retrofit1 = new Retrofit.Builder().baseUrl("https://www.wanandroid.com").build();
        WanAndroidService wanAndroidService = retrofit1.create(WanAndroidService.class);
        Call<ResponseBody> call = wanAndroidService.loginPost("larryLi", "password");

        Response<ResponseBody> response = call.execute();
        String result = response.body().string();
        System.out.println(result);

        JsonRootBean rootBean = new Gson().fromJson(result, JsonRootBean.class);
        System.out.println(rootBean);

    }

}