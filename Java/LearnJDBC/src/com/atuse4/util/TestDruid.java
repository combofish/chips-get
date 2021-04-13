package com.atuse4.util;

import java.io.InputStream;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.Properties;

import javax.sql.DataSource;

import org.junit.Test;

import com.alibaba.druid.pool.DruidDataSourceFactory;

public class TestDruid {
	private static DataSource source1;
	static {
		try {
			Properties pros = new Properties();

			InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream("druid.properties");

			pros.load(is);

			source1 = DruidDataSourceFactory.createDataSource(pros);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static Connection getConnection3() throws SQLException {

		Connection conn = source1.getConnection();
		return conn;
	}

	@Test
	public void getT() {
		try {
			Connection connection = getConnection3();
			System.out.println(connection);
			connection.close();
		} catch (Exception e) {
			// TODO: handle exception
		}
	}
}
