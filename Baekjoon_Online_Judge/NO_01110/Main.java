package Baekjoon_Online_Judge.NO_01110;

import java.util.Scanner;

/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 더하기 사이클                       | 
 -------------------------------------- 
*/
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), ori, cycle_length = 0;

        ori = N;
        
        while (true){
            cycle_length ++;
            
            N = N % 10 * 10 + (N / 10 + N % 10) % 10;

            if (N == ori) break;
        }

        System.out.println(cycle_length);

        sc.close();
    }
}