package Baekjoon_Online_Judge.NO_03507;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 20                   | 
 | 3507 Automated Telephone Exchange| 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), cnt = 0;

        for(int num1 = 0; num1 < 100; num1 ++){
            for(int num2 = 0; num2 < 100; num2 ++){
                if(n - num1 - num2 == 0) cnt ++;
            }
        }

        System.out.println(cnt);
        sc.close();
    }
}