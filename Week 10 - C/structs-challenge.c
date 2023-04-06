#include <stdio.h>

struct position
{
    //char name[20];
    char name;
    char address[20];
    char city[20];
    char postcode[20];
    char* decision;
};

int modifyName(struct position* b, char* new_name);

int main()
{
    struct position e;
    char* change;

    printf("Please enter your name: \n");
    gets(e.name);
    printf("Please enter your address: \n");
    gets(e.address);
    printf("Please enter your city: \n");
    gets(e.city);
    printf("Please enter your postcode: \n");
    gets(e.postcode);

    printf("you entered %s, %s, %s, %s \n", e.name, e.address, e.city, e.postcode);
    change = modifyName(&e, "tom");
    printf("%s\n", e.name);
    
    
    return 0;
}

int modifyName(struct position* b, char* new_name)
{
    b->name = new_name;    
}