package com.learn.usehttp;

import okhttp3.MultipartBody;
import okhttp3.ResponseBody;
import org.intellij.lang.annotations.Flow;
import retrofit2.Call;
import retrofit2.http.*;

public interface UploadService {
    @POST("post")
    @Multipart
    Call<ResponseBody> upload(@Part MultipartBody.Part file);

    @Streaming
    @GET
    Call<ResponseBody> download(@Url String url);

    @GET
    Call<ResponseBody> rx_download(@Url String url);
}
