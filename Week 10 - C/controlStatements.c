#include <stdio.h>

int main()
{
    int n = 4;

    if(n == 5)
    {
        printf("Yes\n");
    }
    else if (n == 3)
    {
        printf("No\n");
    }
    else
    {
        printf("Maybe\n");    
    }

    switch (n)
    {
        case 3:
            printf("Three\n");
            break;
        case 4:
            printf("Four\n");
            break;
        case 5:
            printf("Five\n");
            break;
        default:
            printf("None of the above\n");
    }

    //for loops
    for (int i = 0; i <10; i++)
    {
        printf("...%d\n", i);
    }

    printf("---------------------\n");

    //while loop
    int z = 10;
    while (z > 0)
    {
        printf("...%d\n", z);
        z--;
    }

    printf("---------------------\n");


    //do while loop
    int y = 10;
    do 
    {
        printf("...%d\n", y);
        y--;
    }
    while(y > 10);



    return 0;
}