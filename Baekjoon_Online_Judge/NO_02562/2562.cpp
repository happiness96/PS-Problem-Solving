#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 최댓값                             | 
 -------------------------------------- 
*/

int main(){
    int result = 0, result_ind;

    for (int ind = 1; ind < 10; ind ++){
        int number;

        cin >> number;

        if (number > result){
            result = number;
            result_ind = ind;
        }
    }

    cout << result << '\n' << result_ind;
    
    return 0;
}