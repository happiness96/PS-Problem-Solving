#include <iostream>
#include <algorithm>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 15                   | 
 | 2993 세 부분              | 
 ---------------------------- 
*/

int main(){
    string word;

    cin >> word;

    int size = word.length();
    string result = "";

    for(int i = 0; i < size; i ++) result += 'z';
    
    for(int i = 1; i < size - 1; i ++){
        string str1 = "";

        for(int ind1 = i - 1; ind1 >= 0; ind1 --) str1 += word[ind1];
        
        for(int j = i + 1; j < size; j ++){
            string str2 = "", str3 = "";

            for(int ind2 = j - 1; ind2 >= i; ind2 --) str2 += word[ind2];
            for(int ind3 = size - 1; ind3 >= j; ind3 --) str3 += word[ind3];

            string tmp = str1 + str2 + str3;

            if(tmp.compare(result) < 0) result = tmp;
        }
    }

    cout << result;
    return 0;
}
