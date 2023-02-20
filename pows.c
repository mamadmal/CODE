#include <stdio.h>

int main(void){
    //part one
    int sum = 0;
    for (int i=0; i < 101; ++i){
        int x = i;
        sum = sum + x;
    }
    printf(" the sum of  0 - 100 is: %d \n", sum);

    int pow_total = sum * sum;
    printf("answer of first part is: %d \n", pow_total);

    //part 2
    int numPowlis[101];
    int num = 0;
    for (int i = 2; i < 101; i++){ //for not good work of program we staer from 2 and the we + by 1
        num = i;
        num = num * num;
        printf("number:%d ", num);
        numPowlis[i] = num;
    }

    int sumOfTotal = 1;
    for (int i = 1; i < 101; i++){
          sumOfTotal = sumOfTotal + numPowlis[i];
    }
    printf("\nthe sum of single pow is: %d\n", sumOfTotal);

    //last part
    int final_ans = pow_total - sumOfTotal;
    printf("\nfinal answer is: %d\n", final_ans);
}
