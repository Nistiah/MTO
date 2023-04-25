#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
	char answers_line[2048],output_line[2048],cmd_line[2048];
	FILE *answers,*output;
	int ans=0,total=0;
	if(argc < 2){
		puts("No app specified as parameter!");
		exit(-1);
	}
	sprintf(cmd_line,"%s < input.txt > output.txt",argv[1]);
	system(cmd_line);
	answers=fopen("answers.txt","r");
	output=fopen("output.txt","r");
	if(answers && output){
		while(fgets(answers_line,2048,answers) && fgets(output_line,2048,output)){
			if(!strcmp(answers_line,output_line)){
				ans++;
			}
			total++;
		}
		fclose(answers);
		fclose(output);
	}
	printf("%d/%d\n",ans,total);
	return 0;
}
