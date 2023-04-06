#include <stdio.h>

int main()
{
    char* fb = "fizzbuzz";
    char* f = "fizz";
    char* b = "buzz";
    char* m = "meow";

    for(int i = 1; i<101; i++)
    {
        if(i % 15 == 0)
        {
            printf("%s\n", fb);
        }
        else if(i % 3 == 0)
        {
            printf("%s\n", f);
        }
        else if(i % 5 == 0)
        {
            printf("%s\n", b);
        }
        else if(i % 7 == 0)
        {
            printf("%s\n", m);
        }
        else
        {
            printf("%d\n", i);
        }
    }

    return 0;
}