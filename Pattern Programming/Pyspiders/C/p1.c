#include <stdio.h>

void pattern(int r,int c){
    for (int i = 1; i <= r; i++){
        for (int j = 1; j <= c; j++){
            printf("*");
        }
        printf("\n");
    }
}
int main(){
    int rows, cols;
    printf("Enter the number of rows :");
    scanf("%d",&rows);
    printf("Enter the number of columns :");
    scanf("%d",&cols);
    pattern(rows,cols);
}