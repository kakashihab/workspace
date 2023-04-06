#include <stdio.h>
#include <string.h>

int main()
{
    //in C a string is an array of characters
    char s1[6] = {'h', 'e', 'l', 'l', 'o'};
    //is also possible to initialise a string by assigning a value to a pointer to char 
    char* s2 = "world";

    char s3[51];
    int n;
    int i;
    
    printf("Type something here...\n");
    gets(s3);
    printf("you typed %s", s3);

    //get length of the string
    n = strlen(s3);
    printf("Length : %d\n", n);

    //print a string one character at a time
    for (i = 0; i < n; i++)
    {
        printf("%d...%c\n", i, s3[i]);
    }

    //reverse a string
    strrev(s3);
    printf("reversed : %s\n", s3);

    strcpy(s3, "jackdaws");
    printf("copied...%s\n", s3);

    //concatenating strings : strcat
    //coparing strings : strcmp
    //examine characters : isalpha, isdigit, isupper...
    

     
    return 0;
}