#include <stdio.h>

int main(){
    int i,j,r,c;

    printf("Enter the number of rows : ");
    scanf("%d",&r);
    printf("Enter the number of columns : ");
    scanf("%d",&c);

    for (i = 1; i <= 9; i++){
        for (j = 1; j <= 5; j++){
            if (j >= (c + 1) / 2 - (i - 1) && j >= i - (r - c)){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
}