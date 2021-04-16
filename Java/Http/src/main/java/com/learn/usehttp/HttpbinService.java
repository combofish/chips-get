package com.learn.usehttp;

import okhttp3.FormBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.*;

import java.util.Map;

public interface HttpbinService {
    // https://www.httpbin.org/post/xxx
    @POST("post")
    @FormUrlEncoded
    Call<ResponseBody> post(@Field("username") String username, @Field("password") String password);

    @GET("get")
    Call<ResponseBody> get(@Query("username") String username, @Query("password") String password, @QueryMap Map<String,String> map);

    @HTTP(method = "GET")
    Call<ResponseBody> http(@Query("username") String username, @Query("password") String password);

    @POST("post")
    Call<ResponseBody> postBody(@Body FormBody body);

    @POST("{id}")
    Call<ResponseBody> postPath(@Path("id") String path);

    @POST("{id}")
    @FormUrlEncoded
    Call<ResponseBody> postPath(@Path("id") String path, @Field("username") String username, @Field("password") String password);

    @Headers({"os:android","version:1.0"})
    @POST("post")
    Call<ResponseBody> postWithHeader();

    @POST
    Call<ResponseBody> postUrl(@Url String url);

}
