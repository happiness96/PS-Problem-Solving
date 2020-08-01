#include <iostream>
#include <vector>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 08                 | 
 | Day 02                   | 
 | 10773 제로                | 
 ---------------------------- 
*/

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    vector <int> v;

    int K;

    cin >> K;

    for(int i = 0; i < K; i ++){
        int num;

        cin >> num;
        
        if(num) v.push_back(num);
        else v.pop_back();
    }

    int total = 0;
    for(auto val : v) total += val;

    cout << total;

    return 0;
}
