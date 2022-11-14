#include<stdio.h>
#include<string.h>
int main(void)
{
    char s1[100];
    char s2[100];
    int i;
    printf("Enter the first string\n");
    scanf("%s",s1);
    for (i=0;i<strlen(s1);i++)
    {
        s2[i]=s1[i];
    }
    s2[strlen(s1)]='\0';
    //"\0" indicates a null character, that is it indicates the end of the string. It is the last character of a string.
    // printf("%s\n",s1);
    printf("%s\n",s2);
    return 0;
}
