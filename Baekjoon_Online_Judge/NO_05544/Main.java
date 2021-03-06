package Baekjoon_Online_Judge.NO_05544;

import java.util.Scanner;

/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 27                   | 
 | 5544 심부름 가는 길        | 
 ---------------------------- 
*/

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int total_min = 0, total_sec = 0;

        for(int i = 0; i < 4; i ++){
            int time = sc.nextInt();

            total_sec += time;
        }

        total_min += total_sec / 60;
        total_sec %= 60;

        System.out.println(total_min);
        System.out.println(total_sec);
        sc.close();
    }
}
