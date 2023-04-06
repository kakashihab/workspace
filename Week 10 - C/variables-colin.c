#include <stdio.h>
#include <limits.h>
#include <math.h>

int main()
{
    int n = 5;   // an integer value
    float f = 1.234;     // accurate to 6dp
    double d = 2.3456789;    // accurate to 10dp
    char c = 'A';      // a single letter
    int a = 97;

    int x, y, z;    // can create multiple variables of the same type on one line

    long int l;
    short int s;

    unsigned int u;       // changes range to 0..4 billion ish

    // check the size and range of different types of variable
    /*
    printf("int takes up : %d\n", sizeof(int));
    printf("max int is : %d\n", INT_MAX);
    printf("min int is : %d\n", INT_MIN);

    printf("long int takes up : %d\n", sizeof(long int));
    printf("max long int is : %d\n", LONG_MAX);
    printf("min long int is : %d\n", LONG_MIN);

    printf("short int takes up : %d\n", sizeof(short int));
    printf("max short int is : %d\n", SHRT_MAX);
    printf("min short int is : %d", SHRT_MIN);
    */
    
    // casting from a float to an int just truncates the value
    printf("...%d\n", (int)f); 

    // cast from a double to a float - the value is rounded
    printf("...%f\n", (float)d);

    // cast from character to integer
    printf("...%d\n", (int)c);

    // cast from int to char
    printf("...%c\n", (char)a);

    // do some sums
    x = 33;
    y = 7;
    z = 0;

    // adding up
    z = x + y;
    // subtracting
    z = x - y;
    // multiplying
    z = x * y;
    // division
    z = x / y;
    printf("...%d\n", z);
    z = x % y;
    printf("...%d\n", z);

    x = 625;
    z = sqrt(x);
    printf("...%d\n", z);


    return 0;
}