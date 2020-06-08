/**
 * For Serial_master.
 * Modified in 6/8/2020.
 * Modified by combofish.
 * Work on @11.0592 MHz, Baud: 9600bps,
 */

#ifndef __serial_master_H
#define __serial_master_H
#include <reg52.h>

#ifndef uchar
#define   uchar unsigned char
#endif

// Master address "0"

extern unsigned char serial_master_temp[10];

/** Usage:
    void main(){

    UART_init();

    while(1){
    
    TXdata(1,"1234$");	
    }

*/

void UART_init();
void chuan();// interrupt 4; //串口中断服务函数
void TXdata(uchar addr,uchar *str);

#endif

