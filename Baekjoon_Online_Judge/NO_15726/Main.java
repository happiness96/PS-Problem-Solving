package Baekjoon_Online_Judge.NO_15726;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 15726 이칙연산             | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double A = sc.nextDouble(), B = sc.nextDouble(), C = sc.nextDouble();
        double res1 = A * B / C, res2 = A / B * C;

        if(res1 > res2) System.out.println((int)res1);
        else System.out.println((int)res2);

        sc.close();
    }
}