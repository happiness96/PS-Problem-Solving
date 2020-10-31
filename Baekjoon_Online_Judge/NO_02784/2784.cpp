#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 10                           | 
 | Day 31                             | 
 | 2784 가로 세로 퍼즐                 | 
 -------------------------------------- 
*/

int main(){
    string words[6];
    string result = "ZZZZZZZZZZZZ";

    for(int i = 0; i < 6; i ++){
        cin >> words[i];
    }
    
    for(int i = 0; i < 6; i ++){
        for(int j = 0; j < 6; j ++){
            if(i == j) continue;

            for(int k = 0; k < 6; k ++){
                if(k == i or k == j) continue;
                string tmp[3] = {words[i], words[j], words[k]};

                int chk[6] = {0, };
                int flag = 0;
                chk[i] = 1;
                chk[j] = 1;
                chk[k] = 1;
                
                for(int col = 0; col < 3; col ++){
                    string save = "";

                    for(int row = 0; row < 3; row ++) save += tmp[row][col];

                    for(int chk_ind = 0; chk_ind < 6; chk_ind ++){
                        if(chk[chk_ind] == 0 and save == words[chk_ind]){
                            chk[chk_ind] = 1;
                            flag += 1;
                            break;
                        }
                    }
                }

                if(flag == 3){
                    if(result > words[i] + words[j] + words[k]) result = words[i] + words[j] + words[k];
                }

            }
        }
    }

    if(result == "ZZZZZZZZZZZZ") cout << 0;
    else{
        for(int i = 0; i < 9; i += 3){
            cout << result[i] << result[i + 1] << result[i + 2] << "\n";
        }
    }
    return 0;
}