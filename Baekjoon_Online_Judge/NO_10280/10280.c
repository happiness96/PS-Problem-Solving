#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 10280 Pizza voting       | 
 ---------------------------- 
*/

int main(){
    int n, p, start, end;

    scanf("%d %d", &n, &p);

    start = n / 3 + 1;
    end = start + (n - 1) / 3;

    if(start <= p && p <= end) printf("YES");
    else printf("NO");

    return 0;
}
