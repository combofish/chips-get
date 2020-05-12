/**
 * For LCD1602.
 * Modified in 5/12/2020.
 * Modified by combofish.
 */

#ifndef __lcd1602_H
#define __lcd1602_H
#include  <REG51.H>	

#define   uchar unsigned char
#define   uint unsigned int
	
#define   DataPort P0  
sbit      LCM_RS=P2^0; 
sbit      LCM_RW=P2^1; 
sbit      LCM_EN=P2^2;

void InitLcd();
void DisplayOneChar(uchar X,uchar Y,uchar DData);

void WaitForEnable();
void WriteDataLCM(uchar dataW);
void WriteCommandLCM(uchar CMD,uchar Attribc);

#endif
