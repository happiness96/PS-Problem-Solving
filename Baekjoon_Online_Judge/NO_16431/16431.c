#include <stdio.h>
#include <stdlib.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 27                   | 
 | 16431 베시와 데이지        | 
 ---------------------------- 
*/

int main(){
    int b_row, b_col, d_row, d_col, j_row, j_col, b_distance, d_distance;

    scanf("%d %d", &b_row, &b_col);
    scanf("%d %d", &d_row, &d_col);
    scanf("%d %d", &j_row, &j_col);

    b_distance = abs(b_row - j_row) + abs(b_col - j_col);
    d_distance = abs(d_row - j_row) + abs(d_col - j_col);

    int sub;

    if(abs(b_row - j_row) < abs(b_col - j_col)) sub = abs(b_row - j_row);
    else sub = abs(b_col - j_col);

    b_distance -= sub;
    
    if(b_distance < d_distance) printf("bessie");
    else if(b_distance > d_distance) printf("daisy");
    else printf("tie");

    return 0;
}
