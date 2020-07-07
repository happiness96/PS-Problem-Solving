package Baekjoon_Online_Judge.NO_09664;

import java.util.Scanner;

/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 9664 NASLJEDSTVO         | 
 ---------------------------- 
*/


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double N =sc.nextDouble(), O = sc.nextDouble();
        
        O *= N / (N - 1);

        if(O % 1 != 0) System.out.println((int)O + " " + (int)O);
        else System.out.println((int)O - 1 + " " + (int)O);

        sc.close();
    }
    
}