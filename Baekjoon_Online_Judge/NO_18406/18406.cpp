#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 27                   | 
 | 18406 럭키 스트레이트       | 
 ---------------------------- 
*/

int main(){
    string N;
    int tot1 = 0, tot2 = 0;

    cin >> N;

    int len = N.length();

    for(int i = 0; i < len / 2; i ++) tot1 += (int)N[i];
    for(int i = len / 2; i < len; i++) tot2 += (int)N[i];

    if(tot1 == tot2) cout << "LUCKY";
    else cout << "READY";
    
    return 0;
}
