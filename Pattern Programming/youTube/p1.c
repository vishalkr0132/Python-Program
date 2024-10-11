
// *    
// **   
// ***
// ****
// *****
#include <stdio.h>
#include <conio.h>

/* int main(){
    int i,j,n;

    printf("Enter the number of rows: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++){
        for (j = 1; j <= n; j++){
            if(j <= i){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
} */


// Function to print the left-aligned triangle pattern
void pattern1(int r){
    for (int i = 1; i < r; i++){
        for (int j = 1; j < r; j++){
            if (j <= i){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
}
int main() {
    int rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    pattern1(rows);

    return 0;
}
