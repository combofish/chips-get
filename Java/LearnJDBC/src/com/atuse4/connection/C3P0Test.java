package com.atuse4.connection;

import java.sql.Connection;
import java.sql.SQLException;

import org.junit.Test;

import com.mchange.v2.c3p0.ComboPooledDataSource;

public class C3P0Test {
	// 方式一：
	@Test
	public void testGetConnection() throws Exception {
		// 获取c3p0数据库连接池
		ComboPooledDataSource cpds = new ComboPooledDataSource();
		cpds.setDriverClass("com.mysql.cj.jdbc.Driver");
		cpds.setJdbcUrl("jdbc:mysql://localhost:3306/test");
		cpds.setUser("root");
		cpds.setPassword("abc123");
		// 通过设置相关的参数，对数据库连接池进行管理：
		// 设置初始时数据库连接池中的连接数
		cpds.setInitialPoolSize(10);

		Connection conn = cpds.getConnection();
		System.out.println(conn);

		// 销毁c3p0数据库连接池
//		DataSources.destroy( cpds );
	}

	// 方式二：使用配置文件
	@Test
	public void testGetConnection1() throws SQLException {
		ComboPooledDataSource cpds = new ComboPooledDataSource("hellc3p0");
		Connection conn = cpds.getConnection();
		System.out.println(conn);
	}
}
