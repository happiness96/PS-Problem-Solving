/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 02                             | 
 | 정수 N개의 합                       | 
 -------------------------------------- 
*/

long long sum(int *a, int n){
    long long ans = 0;

    for (int i = 0; i < n; i ++) ans += a[i];

    return ans;
}