package Baekjoon_Online_Judge.NO_15964;

import java.util.Scanner;

/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 15964 이상한 기호          | 
 ---------------------------- 
*/


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        long A, B;

        A = sc.nextLong();
        B = sc.nextLong();

        System.out.println((A + B) * (A - B));
        sc.close();
    }
}