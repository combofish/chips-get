#include<stdio.h>

int getInput(void);
void printMessage(int ,int);

int main(void){
	int counter;
	int input;

	for(counter =0;counter <201;counter++){
		input=getInput();
		if(input == -1) exit(0);
		printMessage(counter,input);
	}
	return 0;
}

int getInput(){
	int input;

	printf("Enter an integer,or use -1 to exit:");
	scanf("%d",&input);
	return input;
}

void printMessage(int counter,int input){
	static int lastnum=0;
	counter++;

	printf("For number %d,you entered %d (%d ,more than last time)\n",counter,input,lastnum);
	lastnum=input;
}


