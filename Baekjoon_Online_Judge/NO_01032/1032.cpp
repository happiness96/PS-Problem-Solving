#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 02                             | 
 | 명령 프롬프트                       | 
 -------------------------------------- 
*/

int main(){
    string form;
    int N, length;

    cin >> N >> form;
    length = form.length();

    for (int i = 1; i < N; i ++){
        string str;
        cin >> str;

        for (int ind = 0; ind < length; ind ++){
            if (str[ind] != form[ind]) form[ind] = '?';
        }
    }

    cout << form;
    
    return 0;
}