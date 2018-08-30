#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>

int main(void){
	pid_t pid=vfork();
	if(pid <0) {
		printf("Error\n");
		exit(1);
	}else if(pid == 0) {
	
		printf("child process PID: %d.\n",getpid());
		setenv("PS1","CHILD\\$",1);
		printf("Process%4d: calling exec.\n",getpid());
		if(execl("/bin/zsh","/bin/zsh","arg2",NULL)<0){
			printf("Process%4d: execle error!\n",getpid());
			exit(0);
		}
		printf("Process%d: You should never see this because the child is aleardy gone.\n",getpid());
		printf("Precess%4d: The chile process is exiting.\n");
	}else{
		printf("Parent process PID:%4d.\n",getpid());
		printf("Process%4d: The parent has fork proceess %4d.\n",pid);
		printf("Process%4d:The child has called exec or has exited.\n",getpid());
	}
	return 0;
}
