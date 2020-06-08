	/**
	 * For BMP085.
	 * Modified in 5/12/2020.
	 * Modified by combofish.
	 */

#ifndef __bmp085_H
#define __bmp085_H
#include  <REG51.H>	

sbit	  SCL=P1^0;     
sbit 	  SDA=P1^1;     

#define OSS 0	// Oversampling Setting (note: code is not set up to use other OSS values)
#define	BMP085_SlaveAddress   0xee
#define   uchar unsigned char
#define   uint unsigned int

typedef unsigned char  BYTE;
typedef unsigned short WORD;

extern uchar p_ge,p_shi,p_bai,p_qian,p_wan,p_shiwan;       
extern uchar t_ge,t_shi,t_bai,t_qian,t_wan,t_shiwan;  
extern short ac1,ac2,ac3,b1,b2,mb,mc,md;                
extern unsigned short ac4,ac5,ac6;


void Init_BMP085(void);
void bmp085Convert(void);

// Move to delay.h
//void Delay5us(void);
//void Delay5ms(void);

void BMP085_Start();
void BMP085_Stop();
void BMP085_SendACK(bit ack);
bit  BMP085_RecvACK();
void BMP085_SendByte(BYTE dat);
BYTE BMP085_RecvByte();
void BMP085_ReadPage();
void BMP085_WritePage();

//void conversion(long temp_data);
//void conversion(long temp_data, uchar ge,uchar shi,uchar bai,uchar qian,uchar wan,uchar shiwan); 
void conversion_pressure(long temp_data);
void conversion_temp(long temp_data); 
	
short Multiple_read(uchar ST_Address);
long bmp085ReadTemp(void);
long bmp085ReadPressure(void);

void  Single_Write(uchar SlaveAddress,uchar REG_Address,uchar REG_data);  
uchar Single_Read(uchar REG_Address);                                     

#endif
