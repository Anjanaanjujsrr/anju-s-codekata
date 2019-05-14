#include<stdio.h>
int main()
{
char c;
int islc,isuc;
printf("enter an alphabet");
scanf("%c",&c);
isuc=(c=='A'||c=='E'||c=='I'||c=='O'||c=='U')
islc=(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
if(isuc||islc)
printf("%c is vowel",c);
else
printf("%c is a consonant",c);
return 0;
}