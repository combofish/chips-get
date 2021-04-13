package com.atuse.transaction;

import java.sql.Connection;

import org.junit.Test;

import com.atuse.util.JDBCUtils;

public class ConnectionTest {

	@Test
	public void testConnection() throws Exception {
		Connection connection = JDBCUtils.getConnection();
		System.out.println(connection);
	}
}
