#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct TAG_datastruct{
	char *string;
	int checksum;
}datastruct;

datastruct* getInput(void);
void printMessage(datastruct* todisp);

int main(void){
	int counter,maxval=0;
	datastruct* svalues[200];

	for(counter=0;counter<200;counter++){
		svalues[counter]=getInput();
		if(!svalues[counter]) break;
		maxval=counter;
	}
	printMessage(svalues[maxval/2]);
	return 0;
}

datastruct* getInput(void){
	char input[80];
	datastruct* instruct;
	int counter;

	printf("Enter a sting,or leave blank whendone:");
	fgets(input,79,stdin);
	input[strlen(input)-1]=0;
	if(strlen(input)==0) return NULL;
	instruct = malloc(sizeof(datastruct));
	instruct->string=strdup(input);
	instruct->checksum=0;
	for(counter =0;counter <strlen(instruct->string);counter++){
		instruct->checksum+=(instruct->string[counter++]);
	}
	return instruct;
}

void printMessage(datastruct* todisp){
	printf("This structure has a checknum of %d,Its string is : \n",todisp->checksum);
	puts(todisp->string);
}
