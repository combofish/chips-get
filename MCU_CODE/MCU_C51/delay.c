#include "delay.h"

// 5us in (STC90C52RC@12M)
void Delay5us()
{
  _nop_();_nop_();_nop_();_nop_();_nop_();
  /**  
       _nop_();_nop_();_nop_();
       _nop_();_nop_();_nop_();_nop_();
       _nop_();_nop_();_nop_();_nop_();
  */
}

// 5ms in (STC90C52RC@12M)
void Delay5ms()
{
  unsigned short n = 560;

  while (n--);
}

void delay(unsigned int k)	
{						
  unsigned int i,j;				
  for(i=0;i<k;i++)
    {			
      for(j=0;j<121;j++)			
	{;}}						
}
