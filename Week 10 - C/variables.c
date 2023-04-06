#include <stdio.h>

int main()
{

    int n = 5;
    float f = 10.430;   //value accurate to 6dp
    double d = 2.3456789;  //value accurate to 10dp
    char c = '7';    //holds a single letter
    long int l;
    short int s;
    int a = 97;
    unsigned int u;  //changes range to 0..4 billion(ish)
    int x, y, z;


    //casting from a flot to an int
    printf("...%d\n", (int)f);

    //cast from a double to a float
    printf("...%f\n", (float)d);

    //cast from a character into an in 
    printf("...%d\n", (int)c);

    //cast from int to a character
    printf("...%c\n", (char)a);


    printf("Int takes up: %d\n", sizeof(int));
    printf("max int is: %d\n", __INT_MAX__);

    //do some sums
    x = 33;
    y = 7;
    z = 0;
    
    z = x + y;
    z = x - y;
    z = x * y;
    z = x / y;
    printf("...%d\n", z);

    z = x % y;

    x = 625;
    z= sqrt(x);
    printf("...%d\n", z);

    


    return 0;
}