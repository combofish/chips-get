/**
  * Copyright 2021 bejson.com 
  */
package com.learn.usehttp.pojo;
import java.util.List;

/**
 * Auto-generated: 2021-04-16 20:16:12
 *
 * @author bejson.com (i@bejson.com)
 * @website http://www.bejson.com/java2pojo/
 */
public class Data {

    private boolean admin;
    private List<String> chapterTops;
    private int coinCount;
    private List<Integer> collectIds;
    private String email;
    private String icon;
    private long id;
    private String nickname;
    private String password;
    private String publicName;
    private String token;
    private int type;
    private String username;
    public void setAdmin(boolean admin) {
         this.admin = admin;
     }
     public boolean getAdmin() {
         return admin;
     }

    public void setChapterTops(List<String> chapterTops) {
         this.chapterTops = chapterTops;
     }
     public List<String> getChapterTops() {
         return chapterTops;
     }

    public void setCoinCount(int coinCount) {
         this.coinCount = coinCount;
     }
     public int getCoinCount() {
         return coinCount;
     }

    public void setCollectIds(List<Integer> collectIds) {
         this.collectIds = collectIds;
     }
     public List<Integer> getCollectIds() {
         return collectIds;
     }

    public void setEmail(String email) {
         this.email = email;
     }
     public String getEmail() {
         return email;
     }

    public void setIcon(String icon) {
         this.icon = icon;
     }
     public String getIcon() {
         return icon;
     }

    public void setId(long id) {
         this.id = id;
     }
     public long getId() {
         return id;
     }

    public void setNickname(String nickname) {
         this.nickname = nickname;
     }
     public String getNickname() {
         return nickname;
     }

    public void setPassword(String password) {
         this.password = password;
     }
     public String getPassword() {
         return password;
     }

    public void setPublicName(String publicName) {
         this.publicName = publicName;
     }
     public String getPublicName() {
         return publicName;
     }

    public void setToken(String token) {
         this.token = token;
     }
     public String getToken() {
         return token;
     }

    public void setType(int type) {
         this.type = type;
     }
     public int getType() {
         return type;
     }

    public void setUsername(String username) {
         this.username = username;
     }
     public String getUsername() {
         return username;
     }

    @Override
    public String toString() {
        return "Data{" +
                "admin=" + admin +
                ", chapterTops=" + chapterTops +
                ", coinCount=" + coinCount +
                ", collectIds=" + collectIds +
                ", email='" + email + '\'' +
                ", icon='" + icon + '\'' +
                ", id=" + id +
                ", nickname='" + nickname + '\'' +
                ", password='" + password + '\'' +
                ", publicName='" + publicName + '\'' +
                ", token='" + token + '\'' +
                ", type=" + type +
                ", username='" + username + '\'' +
                '}';
    }
}