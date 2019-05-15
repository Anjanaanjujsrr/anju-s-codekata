#include<stdio.h>
#include<string.h>
void main()
{
char a[10],b[10];
printf("enter a");
gets(a);
strcpy(b,a);
strrev(b);
if(strcmp(a,b)==0)
printf("palindrome");
else
printf("not a palindrome");
}