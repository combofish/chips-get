#include "dht11.h"

uchar RH,RL,TH,TL;
uchar data_byte;

//***************延时函数************************************* 

 void dht11_delay(uchar ms)          //毫秒延时模块// 
{ 
  uchar i; 
  while(ms--)                 
  for(i=0;i<100;i++); 
} 

void delay1()                  //一个for循环大概需要8个多机器周期，一个机器周期为1us，晶振为12MHz，本函数延时8us 
{ 
  uchar i; 
  for(i=0;i<1;i++); 
} 

//**************************dht11测试模块*************************************// 

void start(void)//开始信号 
{ 
  io=1; 
  delay1(); 
  io=0; 
  delay(25);// 主机把总线拉低必须大于18ms保证DHT11能检测到起始信号 
  io=1;    //发送开始信号结束后拉高电平延时20-40us 
  delay1();//以下三个延时函数差不多为24us符合要求 
  delay1(); 
  delay1(); 
} 

uchar receive_byte(void)//接收一个字节// 
{ 
  uchar i,temp; 
  for(i=0;i<8;i++)//接收8bit的数据 
  { 
 	while(!io);//等待50us的低电平开始信号结束 
 	delay1();//开始信号结束之后延时26us-28us以下三个延时函数 
	delay1(); 
 	delay1(); 
 	temp=0;//时间为26us-28us表示接收的为数据'0' 
 	if(io==1) 
	 temp=1; //如果26us-28us之后还为高电平则表示接收的数据为'1' 
  while(io);//等待数据信号高电平'0'为26us-28us'1'为70us 
 	data_byte<<=1;//接收的数据为高位在前右移 
	data_byte|=temp; 
  } 
  return data_byte; 
}  

void receive(void)//接收数据// 
{ 
  uchar T_H,T_L,R_H,R_L,check,num_check,i; 
  start();//开始信号// 
  io=1;   //主机设为输入判断从机DHT11响应信号 
  if(!io)//判断从机是否有低电平响应信号// 
  {  
	while(!io);//判断从机发出 80us 的低电平响应信号是否结束// 
	while(io);//判断从机发出 80us 的高电平是否结束如结束则主机进入数据接收状态 

	R_H=receive_byte();//湿度高位 
 	R_L=receive_byte();//湿度低位 
	T_H=receive_byte();//温度高位 
	T_L=receive_byte();//温度低位 

	check=receive_byte();//校验位 
	io=0; //当最后一bit数据接完毕后从机拉低电平50us// 
	for(i=0;i<7;i++)//差不多50us的延时 
	delay1(); 
	io=1;//总线由上拉电阻拉高进入空闲状态 
	num_check=R_H+R_L+T_H+T_L; 
	if(num_check==check)//判断读到的四个数据之和是否与校验位相同 
		{ 
		 RH=R_H; 
		 RL=R_L; 
		 TH=T_H; 
		 TL=T_L; 
		 check=num_check; 

		} 
  } 
}
