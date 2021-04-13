package com.atuse.test;

import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

import org.junit.Test;

import com.mysql.cj.jdbc.Driver;

public class TestConnect {

	@Test
	public void testConnection1() throws SQLException {
		Driver driver = new com.mysql.cj.jdbc.Driver();
		String url = "jdbc:mysql://localhost:3306/test";
		// Properties 封装数据库的用户名和密码
		Properties info = new Properties();
		info.setProperty("user", "larry");
		info.setProperty("password", "Confidence*1234");

		Connection connect = driver.connect(url, info);
		System.out.println(connect);
	}

	@Test
	public void getConnection() throws Exception {
		InputStream inputStream = TestConnect.class.getClassLoader().getResourceAsStream("jdbc.properties");
		Properties properties = new Properties();
		properties.load(inputStream);

		String user = properties.getProperty("user");
		String password = properties.getProperty("password");
		String urlString = properties.getProperty("url");
		String driverClassString = properties.getProperty("driverClass");

		Class.forName(driverClassString);
		Connection connection = DriverManager.getConnection(urlString, user, password);
		System.out.println(connection);
	}
}
