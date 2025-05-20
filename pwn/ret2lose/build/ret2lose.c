#include <stdio.h>

void lose(void){
	char flag[57];
	printf("You lost! Here is your flag\n");
	FILE *f = fopen("flag.txt","r");
       	if(!f){
		printf("Error. If this happens on the server, contact an admin\n");
		return;
	}
	if (fgets(flag, sizeof(flag),f)==NULL){
		printf("Error. If this happens on the server, contact an admin\n");
		fclose(f);
		return;
	}
	printf("%s\n",flag);
	fclose(f);
}
void Securefunc(void){
	char buf[48];
	read(0,buf,64);
}
int main(){
	printf("Hey Loser say something\n");
	fflush(stdout);
	Securefunc();
	return 0;
}
