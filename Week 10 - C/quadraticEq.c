#include <stdio.h>
#include <math.h>

int main()
{
    int a, b, c;
    double x, y;

    printf("Enter three numbers: \n");
    scanf("%d %d %d", &a, &b, &c);

    x = (-b + sqrt((b*b) - 4 * a * c)) / (2 * a);
    y = (-b - sqrt((b*b) - 4 * a * c)) / (2 * a);

    printf("x = %f or %f\n", x, y);
   
    return 0;
}