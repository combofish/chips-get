#include<stdlib.h>
#include<stdio.h>
#include<sys/types.h> 
#include<unistd.h>

int main(){
	pid_t pid=vfork();
	if(pid<0) {
		printf("Error");
		exit(1);
	}else if (pid ==0) 
		printf("Child process is printing....\n");
	else 
		printf("Parent process is printing....\n");

	exit(0);
//	return  0;
}
