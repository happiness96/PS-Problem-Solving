package Baekjoon_Online_Judge.NO_14264;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 20                   | 
 | 14264 정육각형과 삼각형     | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();

        System.out.println(Math.sqrt(3) * Math.pow(L, 2) / 4);
        sc.close();
    }
}