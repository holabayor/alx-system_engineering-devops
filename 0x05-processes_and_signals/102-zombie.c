#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>

/**
 * main - function that creates 5 zombie process
 * Return: 0 always
 */
int main(void)
{
	int pid, i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			exit(0);
		sleep(20);
	}
	return (0);
}
