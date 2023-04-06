#include <stdio.h>

int square(int n);

int main()
{
    int n = 1234; // n is an integer
    int* p = &n; //p is a pointer to an integer, pointing to the address of n

    int x, y;
    int z = 5;

    // * is the "dereference operator" - it makes a variable into a pointer
    // & is the "address of operator"
    // a pointers data type must be the same type as the variable date to which it is pointing to 

    printf("n...%d\n", n);
    printf("p...%p\n", p); //pointer to the address of n (memory location where the integer is stored)

    x = n;
    printf("x...%d\n", x);

    y = *p;
    printf("y...%d\n", y);

    printf("-------------------------------\n");

    printf("%d\n", sizeof(int));
    printf("%d\n", square(z));

    return 0;
}

int square(int n)
{
    return n * n;
}