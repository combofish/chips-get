#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
int main()
{
    pid_t pid;
    int status, i;
    if((pid=fork()) == 0)
    {
        printf("This is the child process. pid =%4d\n", getpid());
        exit(5);
     }
    else
    {
        sleep(1);
        printf("This is the parent process: %4d, wait for child...\n",getpid());
        pid = wait(&status);
        i = WEXITSTATUS(status);
        printf("child's pid =%4d . exit status=^d\n", pid, i);
    }
    return 0;
}
