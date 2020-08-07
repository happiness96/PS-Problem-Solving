#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 소수 수열                  | 
 ---------------------------- 
*/

int main(){
    int prime[30000];
    fill_n(prime, 30000, 1);
    
    prime[0] = 0;
    prime[1] = 0;

    for(int num = 4; num < 30000; num += 2){
        prime[num] = 0;
    }

    for(int num = 3; num < 15000; num += 2){
        if(prime[num]){
            for(int ind = num * 2; ind < 30000; ind += num){
                prime[ind] = 0;
            }
        }
    }

    int T;

    cin >> T;

    for(int testcase = 1; testcase <= T; testcase ++){
        int A, B;
        vector<int> v_a, v_b;
        set<int> s_a, s_b;

        cin >> A >> B;

        if(prime[A]){
            s_a.insert(A);
            v_a.push_back(A);
        }

        if(prime[B]){
            s_b.insert(B);
            v_b.push_back(B);
        }

        int max_a = 0, min_a = 10, max_b = 0, min_b = 10;

        while(v_a.empty() == 0){
            int number = v_a.back();
            v_a.pop_back();

            string str_num = to_string(number);
            int str_length = str_num.length();
            
            max_a = max(max_a, str_length);
            min_a = min(min_a, str_length);

            if(str_num.length() > 1){
                for(int ind = 0; ind < str_num.length(); ind ++){
                    string tmp_str = str_num.substr(0, ind) + str_num.substr(ind + 1);
                    int tmp_str_size = tmp_str.size();
                    int tmp_num = 0;

                    for(int i = 0; i < tmp_str_size; i ++){
                        tmp_num += (tmp_str[i] - '0') * pow(10, tmp_str_size - i - 1);
                    }

                    if(prime[tmp_num]){
                        s_a.insert(tmp_num);
                        v_a.push_back(tmp_num);
                    }
                }
            }
        }

        while(v_b.empty() == 0){
            int number = v_b.back();
            v_b.pop_back();

            string str_num = to_string(number);
            int str_length = str_num.length();
            
            max_b = max(max_b, str_length);
            min_b = min(min_b, str_length);

            if(str_num.length() > 1){
                for(int ind = 0; ind < str_num.length(); ind ++){
                    string tmp_str = str_num.substr(0, ind) + str_num.substr(ind + 1);
                    int tmp_str_size = tmp_str.size();
                    int tmp_num = 0;

                    for(int i = 0; i < tmp_str_size; i ++){
                        tmp_num += (tmp_str[i] - '0') * pow(10, tmp_str_size - i - 1);
                    }

                    if(prime[tmp_num]){
                        s_b.insert(tmp_num);
                        v_b.push_back(tmp_num);
                    }
                }
            }
        }

        cout << "Case #" << testcase << endl;
        int res_a = max_a - min_a, res_b = max_b - min_b;

        if(res_a > res_b) cout << 1 << endl;
        else if(res_a < res_b) cout << 2 << endl;
        else cout << 3 << endl;
    }
    return 0;
}
