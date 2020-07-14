package Baekjoon_Online_Judge.NO_18247;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 18247 겨울왕국 티켓 예매    | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for(int i = 0; i < T; i ++){
            int N = sc.nextInt(), M = sc.nextInt();

            if(N < 12 || M < 4) System.out.println(-1);
            else System.out.println(11 * M + 4);
        }

        sc.close();
    }
}