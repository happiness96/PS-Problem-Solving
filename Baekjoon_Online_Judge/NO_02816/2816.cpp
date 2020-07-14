#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 2816 디지털 티비           | 
 ---------------------------- 
*/

int main(){
    int N, KBS1, KBS2, flag = 0;

    cin >> N;

    for(int ind = 0; ind < N; ind ++){
        string channel;

        cin >> channel;

        if(channel == "KBS1") KBS1 = ind;
        else if(channel == "KBS2") KBS2 = ind;
    }

    if(KBS2 < KBS1) KBS2 += 1;

    for(int i = 0; i < KBS1; i++) printf("1");
    for(int i = 0; i < KBS1; i++) printf("4");
    for(int i = 0; i < KBS2; i++) printf("1");
    for(int i = 0; i < KBS2 - 1; i++) printf("4");

    return 0;
}
