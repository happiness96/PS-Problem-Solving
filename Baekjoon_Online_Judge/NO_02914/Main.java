package Baekjoon_Online_Judge.NO_02914;

import java.util.Scanner;

/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 13                   | 
 | 2914 저작권               | 
 ---------------------------- 
*/

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int A = sc.nextInt(), I = sc.nextInt();

        System.out.println(A * (I - 1) + 1);
        sc.close();
    }
    
}