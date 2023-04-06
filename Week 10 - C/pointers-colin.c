#include <stdio.h>

int square(int* p);
int change_value(int*p, int newval);

int main()
{
    int n = 1234;    // n is an integer
    int* p = &n;     // p is a pointer to an integer, pointing to the address of n

    // all of these are valid...
    // int* p = &n;
    // int *p = &n;
    // int * p = &n;

    int x, y;
    int z = 5;
    int r; 

    // * is the "dereference operator" - it makes a variable into a pointer
    // & is the "address of operator"
    // a pointer's data type must be the same as the data type of the variable it points to

    // print the variable
    printf("n...%d\n", n);
    // print the pointer to the variable - this will be a hexadecimal number
    printf("p...%p\n", p);

    // x becomes the value of n
    x = n;
    printf("x...%d\n", x);

    // y becomes the thing pointed to by p
    y = *p;
    printf("y...%d\n", y);

    printf("---------------------------------------------\n");

    // an integer takes up a few bytes of memory
    // every time we pass by value, a new copy of the integer is created
    // (takes up more memory)
    printf("%d\n", sizeof(int));
    printf("%d\n", square(n));

    printf("---------------------------------------------\n");
    
    // pass by reference - no new copy of the value is created
    // (no new memory is used)
    printf("%d\n", z);
    r = change_value(&z, 100);
    printf("%d\n", z);

    return 0;
}


int square(int n)
{
    return n * n;
}


int change_value(int* p, int newval)
{
    // when you use a pointer without the * operator, the pointer is an address
    // when you use a pointer with the * operator, the pointer represents the value at its address
    *p = newval;
    return 0;
}
