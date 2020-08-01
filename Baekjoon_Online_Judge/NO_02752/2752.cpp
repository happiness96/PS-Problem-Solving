#include <iostream>
#include <algorithm>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 08                 | 
 | Day 02                   | 
 | 2752 세수정렬              | 
 ---------------------------- 
*/

int main(){
    int numbers[3];

    for(int i = 0; i < 3; i ++) cin >> numbers[i];

    sort(numbers, numbers + 3);

    for(int i = 0; i < 3; i ++) cout << numbers[i] << " ";
    
    return 0;
}
