#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 08                 | 
 | Day 02                   | 
 | 10987 모음의 개수          | 
 ---------------------------- 
*/

int main(){
    string word;
    int cnt = 0;

    cin >> word;

    for(auto ch: word){
        if(ch =='a' or ch =='e' or ch =='i' or ch =='o' or ch =='u') cnt += 1;
    }

    cout << cnt;
    return 0;
}
