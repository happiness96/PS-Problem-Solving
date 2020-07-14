#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 14659 한조서열정리하고옴ㅋㅋ | 
 ---------------------------- 
*/

int main(){
    int N, max_height = 0, result = 0, cnt = 0;

    cin >> N;

    for(int i = 0; i < N; i ++){
        int height;

        cin >> height;

        if(height > max_height){
            max_height = height;
            
            if(cnt > result) result = cnt;

            cnt = 0;
        }

        else cnt ++;
    }

    if(cnt > result) result = cnt;

    cout << result;

    return 0;
}
