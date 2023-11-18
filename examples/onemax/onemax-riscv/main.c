#include <stdio.h>

#define TEMP_SIZE 7
#define SAVED_SIZE 12


extern void asm_call(unsigned long*, unsigned long*);

int main(){
    unsigned long temp[TEMP_SIZE];
    unsigned long saved[SAVED_SIZE];

    asm_call(saved, temp);

    unsigned long result = temp[0];
    int fitness = 0;
    for(unsigned long int b=1; b; b <<= 1)
        fitness += !!(result & b);

    printf("%d\n", fitness);
    return 0;
}