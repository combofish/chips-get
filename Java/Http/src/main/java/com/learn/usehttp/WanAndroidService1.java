package com.learn.usehttp;

import com.learn.usehttp.pojo.JsonRootBean;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.POST;

public interface WanAndroidService1 {
    @POST("user/login")
    @FormUrlEncoded
    Call<JsonRootBean> loginPost(@Field("username") String username, @Field("password") String password);
}