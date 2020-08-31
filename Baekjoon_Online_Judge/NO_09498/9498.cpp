#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 08                           | 
 | Day 31                             | 
 | 시험 성적                          | 
 -------------------------------------- 
*/

int main(){
    int score;

    cin >> score;

    if (90 <= score and score <= 100) cout << 'A';
    else if (80 <= score and score <= 89) cout << 'B';
    else if (70 <= score and score <= 79) cout << 'C';
    else if (60 <= score and score <= 69) cout << 'D';
    else cout << 'F';

    return 0;
}