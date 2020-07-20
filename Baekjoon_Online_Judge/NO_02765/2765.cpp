#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 20                   | 
 | 2765 자전거 속도           | 
 ---------------------------- 
*/
#define PI 3.1415927

int main(){
    int test_case_cnt = 1;

    while(true){
        double diameter, rotate_cnt, time, radius;

        cin >> diameter >> rotate_cnt >> time;

        if(rotate_cnt == 0) break;
        
        radius = diameter / 2 / (5280 * 12);
        
        double distance = 2 * PI * radius * rotate_cnt;
        double mph = distance / time * 3600;

        printf("Trip #%d: %.2lf %.2lf\n", test_case_cnt, distance, mph);

        test_case_cnt += 1;
    }
    return 0;
}
