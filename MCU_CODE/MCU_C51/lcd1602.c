#include "lcd1602.h"
#include  <INTRINS.H>

void initLcd()				
{			
  WriteCommandLCM(0x38,1);	
  WriteCommandLCM(0x08,1);	
  WriteCommandLCM(0x01,1);	
  WriteCommandLCM(0x06,1);	
  WriteCommandLCM(0x0c,1);
}	


void WriteCommandLCM(uchar CMD,uchar Attribc)
{					
  if(Attribc)WaitForEnable();	
  LCM_RS=0;LCM_RW=0;_nop_();
  DataPort=CMD;_nop_();	
  LCM_EN=1;_nop_();_nop_();LCM_EN=0;
}

void WriteDataLCM(uchar dataW)
{					
  WaitForEnable();		
  LCM_RS=1;LCM_RW=0;_nop_();
  DataPort=dataW;_nop_();	
  LCM_EN=1;_nop_();_nop_();LCM_EN=0;
}

void DisplayOneChar(uchar X,uchar Y,uchar DData)
{						
  Y&=1;						
  X&=15;						
  if(Y)X|=0x40;					
  X|=0x80;			
  WriteCommandLCM(X,0);		
  WriteDataLCM(DData);		
}	

void WaitForEnable(void)	
{
  // use for sim. 
  unsigned int i,j, k = 30;
  
  DataPort=0xff;		
  LCM_RS=0;LCM_RW=1;_nop_();
  LCM_EN=1;_nop_();_nop_();

  // for sim 
  //while(DataPort&0x80);
  // delay(30);

  for(i=0;i<k;i++){			
    for(j=0;j<121;j++) {;}
  }
  
  LCM_EN=0;				
}	
