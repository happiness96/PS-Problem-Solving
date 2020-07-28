#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 근로 시간                  | 
 ---------------------------- 
*/

int main(){
    int T;

    cin >> T;

    for(int testcase = 1; testcase <= T; testcase ++){
        int start_hour, start_min, end_hour, end_min;

        scanf("%d:%d %d:%d", &start_hour, &start_min, &end_hour, &end_min);
        cout << "Case #" << testcase << endl;

        int res_hour = end_hour - start_hour, res_min = end_min - start_min;

        if(res_min < 0){
            res_hour --;
            res_min += 60;
        }

        printf("%02d:%02d\n", res_hour, res_min);
        
    }
    return 0;
}
