#include <stdio.h>

int main()
{

    int n, x;
    char s[20];

    
    printf("Enter two numbers: \n");
    scanf("%d %d", &n, &x);
    printf("You entered %d %d\n", n, x);
    

    //user input using scanf
    //stops reading at first space
    /*
    printf("enter your name: ");
    scanf("%s", s);
    printf("You entered %s\n", s);
    */

    printf("Enter your name: ");
    gets(s);
    printf("You entered %s", s);
    
    return 0;
}