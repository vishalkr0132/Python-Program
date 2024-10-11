#include<stdio.h>

int main(){

    int i,j,k,r,c;

    printf("Enter the number of rows:");
    scanf("%d",&r);
    printf("Enter the number of columns:");
    scanf("%d",&c);

    for (i = 1; i <= r; i++){
        k= 1;
        for (j = 1; j <= c; j++){
            if (j >= (c/2 + 1) - (i - 1) && j <= (c/2 + 1) + (i - 1) && k ==1){
                printf("*");
                k = 0;
            }
            else{
                printf(" ");
                k = 1;
            }
        }
        printf("\n");
    }
    return 0;
}