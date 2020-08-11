#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 08                           | 
 | Day 11                             | 
 | 2257 화학식량                      | 
 -------------------------------------- 
*/

string formula;
int length, index;

int recursion(){
    int acc = 0, pre = 0;

    while(index < length){
        char val = formula[index];

        if(val == '('){
            index ++;
            pre = recursion();
            acc += pre;
        }

        else if(val == ')'){
            index ++;
            return acc;
        }

        else if(val == 'H'){
            acc ++;
            pre = 1;
            index ++;
        }

        else if(val == 'C'){
            acc += 12;
            pre = 12;
            index ++;
        }
        
        else if(val == 'O'){
            acc += 16;
            pre = 16;
            index ++;
        }
        
        else{
            acc += pre * ((int)val - '0' - 1);
            index ++;
        }
    }

    return acc;
}

int main(){
    cin >> formula;

    length = formula.length();
    index = 0;

    cout << recursion();
    return 0;
}
