/**
 * For DHT11.
 * Modified in 5/12/2020.
 * Modified by combofish.
 */
 
#ifndef __dht11_H
#define __dht11_H
#include <REG51.h>

#define uint unsigned int
#define uchar unsigned char

sbit io = P2^7;
extern uchar RH,RL,TH,TL;

void receive(void);

void start(void);
uchar receive_byte(void);
void delay1();
void dht11_delay(uchar ms); 

#endif
