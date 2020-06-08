/**
 * For Serial_master.
 * Modified in 6/8/2020.
 * Modified by combofish.
 * Work on @11.0592 MHz, Baud: 9600bps,
 */
 
#include "serial_master.h"

unsigned char RXData;
unsigned int RXstart;
int j;
unsigned char serial_master_temp[10] = {0};


void UART_init(){
  
  TMOD = 0x20; //定时器1，工作方式2：8位、自动重装
  TH1 = 0xfd; //fd: 9600bps @ 11.0592M
  TL1 = 0xfd; //e8: 1200bps @ 11.0592M
  //f4: 2400bps @ 11.0592M
  REN = 1; //允许串口接收
  SM0 = 1;
  SM1 = 1; //SM0和SM1：串口工作模式3，主从模式 + 波特率可变
  //  SM2 = 1; //只接收地址(从机如此配置，主机不需要)

  //
  SM2 = 0;
  //
	
  ES = 1; //开串口中断
  TR1 = 1; //启动定时器1
  EA = 1; //中断 总开关
}

void chuan() interrupt 4 //串口中断服务函数
{
  ES = 0; //关闭串口中断
  if(RI) //再次判断，是否接收到数据(接收到数据后，RI会置1，需手动清0)
    {
      RXData = SBUF;
      if(RXstart) //判断是否接收到过本地址
	{
	  if(RXData != '$') //判断是否接收到 数据结束 标志 $
	    {
	      serial_master_temp[j] = RXData; //没有接收到结束标志，正常保存数据至数组
	      j++;
	    }
	  else //接收到 结束标志 $
	    {
	      RXstart= 0; //本次接收结束
	      //SM2 = 1; //重新 配置为：只接收地址 模式，下次发送TB8=1才中断
	      j = 0;
	    }
	}

      if(RXData == '0') //判断是否呼叫本机，地址范围：000 – 254(00 - FE)
	{
	  RXstart = 1; //开始接收数据
	  SM2 = 0; //配置为：接收数据 模式
	}
    }

  RI = 0; //清除接收标志位
  ES = 1; //重新开启串口中断
}

void TXdata(uchar addr,uchar *str)
{
  TB8 = 1; //发送地址
  SBUF = addr; //把地址发送出去
  while(!TI); //判断是否发送成功(发送成功后TI会置1，需手动清0)
  TI = 0;
  TB8 = 0; //发送数据
  while(*str != '\0') //发送数组
    {
      SBUF = (*str);
      while(!TI);
      TI = 0;
      str++;
    }
}
