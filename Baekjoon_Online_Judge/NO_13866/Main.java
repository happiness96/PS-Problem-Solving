package Baekjoon_Online_Judge.NO_13866;

import java.util.Scanner;

/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 13866 팀 나누기            |  
 ---------------------------- 
*/
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A, B, C, D;
        
        A =  sc.nextInt();
        B =  sc.nextInt();
        C =  sc.nextInt();
        D =  sc.nextInt();

        System.out.println(Math.abs(D + A - C - B));
        sc.close();
    }
}
