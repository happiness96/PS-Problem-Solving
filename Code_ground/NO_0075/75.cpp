#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 08                           | 
 | Day 07                             | 
 | 회문인 수의 합                      | 
 -------------------------------------- 
*/

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    vector <int> palindrome;

    for(int number = 1; number <= 10000; number ++){
        string str_num = to_string(number);
        string reverse_str = str_num;

        reverse(reverse_str.begin(), reverse_str.end());
        
        if(str_num == reverse_str) palindrome.push_back(number);
    }

    int T;

    cin >> T;

    for(int testcase = 1; testcase <= T; testcase ++){
        int K, result = 100;
        vector <int> result_v;

        cin >> K;

        for(auto num1: palindrome){
            if(num1 == K){
                result = 1;
                result_v.clear();
                result_v.push_back(num1);
                break;
            }
            
            for(auto num2: palindrome){
                if(result < 2) break;

                if(num1 + num2 == K){
                    result = 2;
                    result_v.clear();
                    result_v.push_back(num1);
                    result_v.push_back(num2);
                    break;
                }

                for(auto num3: palindrome){
                    if(result < 3) break;

                    if(num1 + num2 + num3 == K){
                        result = 3;
                        result_v.clear();
                        result_v.push_back(num1);
                        result_v.push_back(num2);
                        result_v.push_back(num3);
                        break;
                    }
                }
            }
        }

        sort(result_v.begin(), result_v.end());
        reverse(result_v.begin(), result_v.end());

        cout << "Case #" << testcase << "\n";
        cout << result_v.size() << " ";

        for(auto v: result_v) cout << v << " ";
        cout << "\n";
    }
    
    return 0;
}