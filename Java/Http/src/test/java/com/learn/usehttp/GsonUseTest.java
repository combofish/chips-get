package com.learn.usehttp;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.learn.usehttp.bean.Job;
import com.learn.usehttp.bean.User;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Type;
import java.util.*;

public class GsonUseTest {
    Gson gson = new Gson();

    @Test
    void testObject() {
        User u1 = new User("larry","123456",11,true);
        String json = gson.toJson(u1);
        System.out.println("序列化" +json);

        User u2 = gson.fromJson(json,User.class);
        System.out.println("反序列化" + u2);

        /**
         * 序列化{"userName":"larry","password":"123456","age":11,"isStudent":true,"test1":0,"class":0}
         * 反序列化User{userName='larry', password='123456', age=11, isStudent=true, job=null, test1=0, test2=0, cls=0}
         */
    }

    @Test
    void testNestedObject() {
        User u1 = new User("larry","123456",11,true);
        Job teacher = new Job("Teacher", 1000);
        u1.setJob(teacher);

        String json = gson.toJson(u1);
        System.out.println("序列化" +json);

        User u2 = gson.fromJson(json,User.class);
        System.out.println("反序列化" + u2);

        /**
         * 序列化{"userName":"larry","password":"123456","age":11,"isStudent":true,"job":{"name":"Teacher","salary":1000},"test1":0,"class":0}
         * 反序列化User{userName='larry', password='123456', age=11, isStudent=true, job=Job{name='Teacher', salary=1000}, test1=0, test2=0, cls=0}
         */

    }

    @Test
    void testArrayObject() {
        User[] users = new User[3];
        users[0] = new User("larry","123456",11,true);
        users[1] = new User("larry1","123456",12,true);
        // users[2] = new User("larry2","123456",13,false);

        String json = gson.toJson(users);
        System.out.println(json);

        User[] users1 = gson.fromJson(json, User[].class);
        System.out.println(users1[0]);
        System.out.println(users1[1]);
        System.out.println(users1[2]);

        /**
         * [{"userName":"larry","password":"123456","age":11,"isStudent":true},{"userName":"larry1","password":"123456","age":12,"isStudent":true},null]
         * User{userName='larry', password='123456', age=11, isStudent=true, job=null}
         * User{userName='larry1', password='123456', age=12, isStudent=true, job=null}
         * null
         */
    }

    @Test
    void testListObject() {
        ArrayList<User> objects = new ArrayList<>();
        objects.add(new User("larry","123456",11,true));
        objects.add(new User("larry1","123456",12,true));
        objects.add(null);

        String json = gson.toJson(objects);
        System.out.println(json);

        Type type = new TypeToken<List<User>>(){}.getType();
        List<User> list = gson.fromJson(json,type);

        System.out.println("反序列化" + list.get(0));
        System.out.println("反序列化" + list.get(1));
        System.out.println("反序列化" + list.get(2));

        /**
         * [{"userName":"larry","password":"123456","age":11,"isStudent":true},{"userName":"larry1","password":"123456","age":12,"isStudent":true},null]
         * User{userName='larry', password='123456', age=11, isStudent=true, job=null}
         * User{userName='larry1', password='123456', age=12, isStudent=true, job=null}
         * null
         */

    }

    @Test
    void testMapObject() {
        Map<String,User> map1 = new HashMap<>();
        map1.put("1",new User("larry","123456",11,true));
        map1.put("2",new User("larry1","123456",12,true));
        map1.put("3",null);
        map1.put(null,null);

        String json = gson.toJson(map1);
        System.out.println(json);

        Type type = new TypeToken<Map<String,User>>(){}.getType();
        Map<String,User> list = gson.fromJson(json,type);

        System.out.println("反序列化" + list.get(null));
        System.out.println("反序列化" + list.get("1"));

        /**
         * {"1":{"userName":"larry","password":"123456","age":11,"isStudent":true},"2":{"userName":"larry1","password":"123456","age":12,"isStudent":true}}
         * 反序列化null
         * 反序列化User{userName='larry', password='123456', age=11, isStudent=true, job=null}
         */

    }

    @Test
    void testSetObject() {
        Set<User> objects = new HashSet<>();
        objects.add(new User("larry","123456",11,true));
        objects.add(new User("larry1","123456",12,true));
        objects.add(null);

        String json = gson.toJson(objects);
        System.out.println(json);

        Type type1 = new TypeToken<Set<User>>(){}.getType();
        Set<User> list1 = gson.fromJson(json,type1);
        Iterator<User> iterator = list1.iterator();
        while(iterator.hasNext()){
            User next = iterator.next();
            System.out.println("反序列化" + next);
        }

        /**
         * [{"userName":"larry","password":"123456","age":11,"isStudent":true},null,{"userName":"larry1","password":"123456","age":12,"isStudent":true}]
         * 反序列化User{userName='larry', password='123456', age=11, isStudent=true, job=null}
         * 反序列化null
         * 反序列化User{userName='larry1', password='123456', age=12, isStudent=true, job=null}
         */

    }

    @Test
    void testNull() {
        User u1 = new User("larry","123456",11,true);

        String json = gson.toJson(u1);
        System.out.println("序列化" +json);

        User u2 = gson.fromJson(json,User.class);
        System.out.println("反序列化" + u2);

        /**
         * 序列化{"userName":"larry","password":"123456","age":11,"isStudent":true,"test1":0,"class":0}
         * 反序列化User{userName='larry', password='123456', age=11, isStudent=true, job=null, test1=0, test2=0, cls=0}
         */
    }

    @Test
    void testGsonExpose() {
        User u1 = new User("larry","123456",11,true);

        Gson gson1 = new GsonBuilder().excludeFieldsWithoutExposeAnnotation().create();
        String json = gson1.toJson(u1);
        System.out.println("序列化" +json);

        User u2 = gson1.fromJson(json,User.class);
        System.out.println("反序列化" + u2);

        /**
         * 序列化{"userName":"larry","password":"123456","age":11,"isStudent":true,"class":0}
         * 反序列化User{userName='larry', password='123456', age=11, isStudent=true, job=null, test1=0, test2=0, cls=0}
         */
    }

}
