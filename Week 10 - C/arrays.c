#include <stdio.h>

int main()
{
    int a1[3];

    a1[0] = 5;
    a1[1] = 99;
    a1[2] = 76;

    printf("...%d\n", a1[1]);

    a1[4] = 111;
    printf("...%d\n", a1[4]);

    //looks at the memory of something that doesn't exist
    printf("...%d", a1[9]);
}