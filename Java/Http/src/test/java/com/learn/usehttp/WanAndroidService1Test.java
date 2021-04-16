package com.learn.usehttp;

import com.learn.usehttp.pojo.JsonRootBean;
import org.junit.jupiter.api.Test;
import retrofit2.Call;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

class WanAndroidService1Test {

    @Test
    void loginTest2_with_Convert() throws IOException {
        Retrofit retrofit2 = new Retrofit.Builder()
                .baseUrl("https://www.wanandroid.com")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        WanAndroidService1 wanAndroidService1 = retrofit2.create(WanAndroidService1.class);
        Call<JsonRootBean> call = wanAndroidService1.loginPost("larryLi", "password");
        Response<JsonRootBean> response = call.execute();
        JsonRootBean jsonRootBean = response.body();
        System.out.println(jsonRootBean);

    }


}