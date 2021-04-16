package com.learn.usehttp.bean;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class User {

    @Expose
    private String userName;
    @Expose
    private String password;
    @Expose
    private int age;
    @Expose
    private boolean isStudent;
    @Expose
    private Job job;

    @Expose(serialize = false,deserialize = true)
    private int test1;

    private transient int test2;

    @Override
    public String toString() {
        return "User{" +
                "userName='" + userName + '\'' +
                ", password='" + password + '\'' +
                ", age=" + age +
                ", isStudent=" + isStudent +
                ", job=" + job +
                ", test1=" + test1 +
                ", test2=" + test2 +
                ", cls=" + cls +
                '}';
    }

    public int getTest2() {
        return test2;
    }

    public void setTest2(int test2) {
        this.test2 = test2;
    }

    @Expose
    @SerializedName("class")
    private int cls;

    public User() {
    }

    public User(String userName, String password, int age, boolean isStudent) {
        this.userName = userName;
        this.password = password;
        this.age = age;
        this.isStudent = isStudent;
    }

    public int getTest1() {
        return test1;
    }

    public void setTest1(int test1) {
        this.test1 = test1;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public boolean isStudent() {
        return isStudent;
    }

    public void setStudent(boolean student) {
        isStudent = student;
    }

    public Job getJob() {
        return job;
    }

    public void setJob(Job job) {
        this.job = job;
    }

    public int getCls() {
        return cls;
    }

    public void setCls(int cls) {
        this.cls = cls;
    }

}
