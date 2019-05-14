#include <stdio.h>
int main()
{
    int n, i, s = 0;
    
    printf("Enter a positive integer: ");
    scanf("%d",&n);

    for(i=1; i <= n; ++i)
    {
        s+= i;  
    printf("S = %d",s);

    return 0;
}
