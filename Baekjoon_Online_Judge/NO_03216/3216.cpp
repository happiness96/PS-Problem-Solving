#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 11                           | 
 | Day 17                             | 
 | 3216 다운로드                       | 
 -------------------------------------- 
*/

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, tot_D = 0, tot_V = 0, last = 0;

    cin >> N;

    for(int i = 0; i < N; i ++){
        int D, V, tmp;

        cin >> D >> V;

        tot_V += V;
        tmp = tot_V - tot_D;

        if(tmp > last) last = tmp;

        tot_D += D;
    }

    cout << last;
    
    return 0;
}