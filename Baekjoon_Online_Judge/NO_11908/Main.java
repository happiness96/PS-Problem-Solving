package Baekjoon_Online_Judge.NO_11908;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 11908 카드                | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt(), total = 0, maxi = 0;

        for(int i = 0; i < n; i ++){
            int c = sc.nextInt();

            total += c;

            if (maxi < c) maxi = c;
        }

        System.out.println(total - maxi);

        sc.close();
    }
}