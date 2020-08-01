#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 08                 | 
 | Day 02                   | 
 | 13752 히스토그램           | 
 ---------------------------- 
*/

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int n;

    cin >> n;

    for(int i = 0; i < n; i ++){
        int k;

        cin >> k;

        for(int j = 0; j < k; j ++) cout << "=";

        cout << "\n";
    }
    return 0;
}
