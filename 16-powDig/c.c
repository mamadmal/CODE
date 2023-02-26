#include <stdio.h>
#include <math.h>

int main(){
    int num;
    num = pow(2, 15);
    printf("\n %d\n", num);

    int sumOfPow = 0;
    while (num > 0 )
    {
        int mod = num % 10;
        printf("the mod: %d\n", mod);
        sumOfPow = sumOfPow + mod;

        num = num / 10;
          
    }
    printf("the sum is: %d", sumOfPow);

}