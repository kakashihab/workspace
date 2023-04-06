#include <stdio.h>
#include "functionlibrary.h" //uses another file to call a function

int square(int n)
{
    int res;
    res = n * n;
    return res;
}

int rf(int n)
{
    int x;
    printf("...%d\n", n);
    x = rf(n - 1);
}

int main()
{
    printf("...%d\n", square(5));
    printf("...%d\n", cube(5));
    
    int n;
    n = rf(99);
    

}

