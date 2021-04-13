package com.atuse.exer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.util.Scanner;

import org.junit.Test;

import com.atuse.test.JDBCUtils;

public class Exer1Test {

	@Test
	public void testInsert() {
		Scanner scanner = new java.util.Scanner(System.in);
		System.out.println("请输入用户名： ");
		String nameString = scanner.next();
		System.out.println("请输入邮箱： ");
		String emailString = scanner.next();
		System.out.println("请输入生日： ");
		String birString = scanner.next();

		String sqlString = "insert into customers(name,email,birth) values(?,?,?)";
		// update(sqlString, "王五", "666@139.com", "1999-09-07");
		int insertCount = update(sqlString, nameString, emailString, birString);
		if (insertCount > 0) {
			System.out.println("添加成功");
		} else {
			System.out.println("添加成功");
		}
	}

	// 通用的增删改操作
	public int update(String sql, Object... args) {// sql中占位符的个数与可变形参的长度相同！
		Connection conn = null;
		PreparedStatement ps = null;
		try {
			// 1.获取数据库的连接
			conn = JDBCUtils.getConnection();
			// 2.预编译sql语句，返回PreparedStatement的实例
			ps = conn.prepareStatement(sql);
			// 3.填充占位符
			for (int i = 0; i < args.length; i++) {
				ps.setObject(i + 1, args[i]);// 小心参数声明错误！！
			}
			// 4.执行
			// ps.execute();
			return ps.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			// 5.资源的关闭
			JDBCUtils.closeResource(conn, ps);

		}
		return 0;

	}
}
