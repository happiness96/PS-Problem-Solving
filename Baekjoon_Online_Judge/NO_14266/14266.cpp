#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 11                           | 
 | Day 03                             | 
 | 14266 나는 가르친다 스위핑을         | 
 -------------------------------------- 
*/

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, result = 0, count = 0;
    double x1, y1, x2, y2, inc1, inc2, save = 2147483647, cur;
    vector <double> start, end;

    cin >> n;

    for(int i = 0; i < n; i ++){
        cin >> x1 >> y1 >> x2 >> y2;

        inc1 = y1 / x1;
        inc2 = y2 / x2;

        if(inc1 >= inc2){
            start.push_back(inc1);
            end.push_back(inc2);
        }

        else{
            end.push_back(inc1);
            start.push_back(inc2);
        }
    }

    sort(start.begin(), start.end());
    sort(end.begin(), end.end());

    while(!start.empty()){
        cur = start.back();
        start.pop_back();
        count ++;
        
        while(!start.empty() and start.back() == cur){
            count ++;
            start.pop_back();
        }

        while(!end.empty() and cur < end.back() and end.back() <= save){
            end.pop_back();
            count --;
        }

        if(count > result) result = count;

        save = cur;
    }

    cout << result;

    return 0;
}