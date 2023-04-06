#include<stdio.h>

#include<ctype.h>

int main()
{
    char* test = "adv", test1;
    int key;

    for (int i = 0; test[i] != '\0'; ++i)

    test1 = test[i];
    {
    
        test1 = (test1 - 'a' - i + 26) % 26 + 'a';
    }
        
    printf("%s", test);

    return 0;

}