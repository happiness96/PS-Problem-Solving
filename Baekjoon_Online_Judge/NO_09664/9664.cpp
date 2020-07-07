#include <iostream>
#include <cmath>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 9664 NASLJEDSTVO         | 
 ---------------------------- 
*/

int main(){
    double N, O;

    cin >> N >> O;
    O *= N / (N - 1);

    if(fmod(O, 1)) cout << int(O) << ' ' << int(O) << '\n';
    else cout << int(O - 1) << ' ' << int(O) << '\n';

    return 0;
}
