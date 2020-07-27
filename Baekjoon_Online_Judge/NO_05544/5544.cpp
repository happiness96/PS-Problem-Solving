#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 27                   | 
 | 5544 심부름 가는 길        | 
 ---------------------------- 
*/

int main(){
    int total_min = 0, total_sec = 0;

    for(int i = 0; i < 4; i ++){
        int time;

        cin >> time;
        total_sec += time;
    }

    total_min += total_sec / 60;
    total_sec %= 60;

    cout << total_min << endl;
    cout << total_sec;
    return 0;
}
