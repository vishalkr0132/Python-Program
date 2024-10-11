#include <stdio.h>
void pattern(int r, int c){
    int val = 1;
    for (int i = 1; i <= r; i++){
        for (int j = 1; j <= c; j++){
            printf("%d ",val);
        }
        printf("\n");
        val++;
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