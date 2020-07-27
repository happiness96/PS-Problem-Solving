package Baekjoon_Online_Judge.NO_16431;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 27                   | 
 | 16431 베시와 데이지        | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int b_row = sc.nextInt(), b_col = sc.nextInt(), d_row = sc.nextInt(),d_col = sc.nextInt(),
        j_row = sc.nextInt(), j_col = sc.nextInt(), b_distance, d_distance;

        b_distance = Math.abs(b_row - j_row) + Math.abs(b_col - j_col);
        d_distance = Math.abs(d_row - j_row) + Math.abs(d_col - j_col);

        b_distance -= Math.min(Math.abs(b_row - j_row), Math.abs(b_col - j_col));

        if(b_distance < d_distance) System.out.println("bessie");
        else if(b_distance > d_distance) System.out.println("daisy");
        else System.out.println("tie");

        sc.close();
    }
}
