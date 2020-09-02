#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 02                             | 
 | 단어 공부                          | 
 -------------------------------------- 
*/

int main(){
    string s;
    int save[26] = {0,};

    cin >> s;
    
    for (auto ch: s){
        if (ch >= 'a') ch -= 32;

        save[ch - 'A'] ++;
    }

    int max_cnt = 0;
    char res;

    for (int i = 0; i < 26; i ++){
        if (save[i] > max_cnt){
            max_cnt = save[i];
            res = i + 'A';
        }

        else if (save[i] == max_cnt) res = '?';
    }

    cout << res;

    return 0;
}