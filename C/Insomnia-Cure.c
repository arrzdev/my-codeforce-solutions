#include <stdio.h>
#include <stdlib.h>

int main(){
    int k,l,m,n,d,i,s;

    printf("%f", 6 % 10 == 0);

    //get values
    scanf("%d", &k);
    scanf("%d", &l);
    scanf("%d", &m);
    scanf("%d", &n);
    scanf("%d", &d);

    s = 0;

    for (i=0; i<d; i++){
        if (i % k == 0 || i % l == 0 || i % m == 0 || i % n == 0){
            s++;
        }
    }

    printf("%d", s);

    return 0;

}