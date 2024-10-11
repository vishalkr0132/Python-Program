/*
    *    
   ***   
  *****  
 ******* 
*********

*/


#include<stdio.h>
#include<conio.h>

int main(){

    int i, j ,r , c;
    printf("Enter the number of rows: ");
    scanf("%d",&r);
    printf("Enter the number of columns: ");
    scanf("%d",&c);

    for (i = 1; i <= r; i++) {
        for (j = 1; j <= c; j++) {
            if (j >= (c/2 + 1) - (i - 1) && j <= (c/2 + 1) + (i - 1)) {
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }

}