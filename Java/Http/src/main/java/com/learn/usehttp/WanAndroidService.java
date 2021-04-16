package com.learn.usehttp;

import com.learn.usehttp.pojo.JsonRootBean;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.POST;
import retrofit2.http.Path;

public interface WanAndroidService {
    @POST("user/login")
    @FormUrlEncoded
    Call<ResponseBody> loginPost(@Field("username") String username, @Field("password") String password);

    @POST("user/login")
    @FormUrlEncoded
    Call<JsonRootBean> loginPost2(@Field("username") String username, @Field("password") String password);

    @POST("m/lg/collect/list/{pageNum}/json")
    Call<ResponseBody> getArticle(@Path("pathNum") int pageNum);


}
