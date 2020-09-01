package Baekjoon_Online_Judge.NO_02739;

import java.util.Scanner;

/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 구구단                              | 
 -------------------------------------- 
*/
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        for (int i = 1; i <= 9; i ++) System.out.printf("%d * %d = %d\n", N, i, N * i);
        sc.close();
    }
}