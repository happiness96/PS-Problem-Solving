#include <vector>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 02                             | 
 | 정수 N개의 합                       | 
 -------------------------------------- 
*/

long long sum(std::vector<int> &a){
    long long ans = 0;

    for (auto val: a){
        ans += val;
    }

    return ans;
}