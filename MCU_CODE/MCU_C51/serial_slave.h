/**
 * For Serial_slave.
 * Modified in 6/8/2020.
 * Modified by combofish.
 * Work on @11.0592 MHz, Baud: 9600bps,
 */

#ifndef __serial_slave_H
#define __serial_slave_H
#include <reg52.h>

#define uchar unsigned char

#define Slave_addr 1 // 地址范围：000 – 254(00 - FE)

extern unsigned char serial_slave_temp[10];
extern unsigned char serial_slave_send[10];
/** Usage:
    void main(){
    while(1){
    UART_init();
    }
    }

*/

void UART_init();
void TXData(uchar *str);
void chuan();// interrupt 4; //串口中断服务函数

#endif
