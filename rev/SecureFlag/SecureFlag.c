#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <fcntl.h>

char* generate_key(void){
	size_t size = 27;
	char *alphabet = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
	strcpy(alphabet, "abcdefghijklmnopqrstuvwxyz");
	static char str[13];
	for(int i=0;i<13;i++){
		int sum = 0;
		if(i % 2 == 0){
			sum = (int)(alphabet[i]) + i*2;
		}else{
			sum = (int)(alphabet[i]) - i*3;
		}
		str[i] = (char)(sum % 26 + 'a');
	}
	str[13] = '\0';
	munmap(alphabet,size);
	return str;
}
unsigned char rotL(unsigned char val, int shift){
       return (val << shift) | (val >> (8 - shift));
}       
void shuffle(char *str, int pin){
	int n = strlen(str);
	for(int i=0;i<n-1;i++){
		int j = (pin + i) % n;
		char tmp = str[i];
		str[i] = str[j];
		str[j] = tmp;
	}}
unsigned char* str_obfuscate(char* str, int shift){
	for(int i=0; str[i]!='\0';i++){
		str[i] = rotL(str[i], shift);
	}
	return str;	
}
void encrypt(unsigned char* str, char* key){
	static unsigned char enc_flag[38];
	int key_len = strlen(key);
	int i;
	for(i=0; i<38;i++){
		enc_flag[i] = str[i] ^ key[i % key_len];
        	printf("%02x", (unsigned char)enc_flag[i] );
	}
       	printf("\n");
	enc_flag[i] = '\0';
}
int main(){
char flag[38];
FILE *f = fopen("fake_flag.txt","r");
if(!f){
	printf("Error opening the flag.\n");
	return 1;
}
if (fgets(flag, sizeof(flag),f)==NULL){
		printf("Error reading the flag.\n");
		fclose(f);
		return 1;
}
int pin = 0xcafe;
int shift = 7;
unsigned char *str = str_obfuscate(flag,shift);
char *key = generate_key();
shuffle(key,pin);
printf("Welcome to my very secure encryption!\n");
printf("Here is your flag: \n");
encrypt(str,key);
printf("Oh yeah you can't read it :) \n");
fclose(f);
return 0;
}
