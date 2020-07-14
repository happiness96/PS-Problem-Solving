package Baekjoon_Online_Judge.NO_10280;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 10280 pizza voting       | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), p = sc.nextInt(), start, end;

        start = n / 3 + 1;
        end = start + (n - 1) / 3;

        if(start <= p && p <= end) System.out.println("YES");
        else System.out.println("NO");

        sc.close();

    }
}