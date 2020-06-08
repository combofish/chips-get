/**
 * For DS18B20.
 * Modified in 6/8/2020.
 * Modified by combofish. 
 * Work @11.0592 MHz or @12 MHz.
 */

#ifndef __DS18B20_H_
#define __DS18B20_H_

#include<reg52.h>

#ifndef uchar
#define uchar unsigned char
#endif

#ifndef uint 
#define uint unsigned int
#endif

extern uchar TempData[8];
extern uchar code ASCII[15];

sbit DSPORT=P2^2;

/** useage
    datapros(Ds18b20ReadTemp());
    //DisplayOneChar(uchar X,uchar Y,uchar DData);
    DisplayOneChar(1, 1, TempData[1]);	
    DisplayOneChar(2, 1, TempData[2]);
    DisplayOneChar(3, 1, ASCII[10]);	
    DisplayOneChar(4, 1, TempData[4]);
    DisplayOneChar(5, 1, TempData[5]);	
    DisplayOneChar(6, 1, 0xdf);
    DisplayOneChar(7, 1, 0x43);
*/

void datapros(int temp);
void Delay1ms(uint );
uchar Ds18b20Init();
void Ds18b20WriteByte(uchar com);
uchar Ds18b20ReadByte();
void  Ds18b20ChangTemp();
void  Ds18b20ReadTempCom();
int Ds18b20ReadTemp();

#endif
