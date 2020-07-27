#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 27                   | 
 | 16968 차량 번호판 1        | 
 ---------------------------- 
*/

int main(){
    string form;

    cin >> form;

    int len = form.length();
    int save[len], res = 1;

    for(int i = 0; i < len; i ++){
        if(form[i] == 'd') save[i] = 10;
        else save[i] = 26;
    }

    for(int i = 0; i < len - 1; i ++){
        if(form[i] == form[i + 1]) save[i] -= 1;
    }

    for(int i = 0; i < len; i ++) res *= save[i];

    cout << res;
    return 0;
}
