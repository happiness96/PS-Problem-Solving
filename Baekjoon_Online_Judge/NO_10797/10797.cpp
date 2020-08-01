#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 08                 | 
 | Day 02                   | 
 | 10797 10부제              | 
 ---------------------------- 
*/

int main(){
    int day, result = 0;

    cin >> day;

    for(int i = 0; i < 5; i ++){
        int number;
        cin >> number;

        if(day == number) result += 1;
    }

    cout << result;
    return 0;
}
