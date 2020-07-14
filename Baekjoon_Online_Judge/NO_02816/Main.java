package Baekjoon_Online_Judge.NO_02816;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 2816 디지털 티비           | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), KBS1 = 0, KBS2 = 0;

        for(int ind = 0; ind < N; ind ++){
            String channel = sc.next();
            
            if(channel.equals("KBS1")) KBS1 = ind;
            else if(channel.equals("KBS2")) KBS2 = ind;
        }

        for(int i = 0; i < KBS1; i ++) System.out.print("1");
        for(int i = 0; i < KBS1; i ++) System.out.print("4");

        if(KBS2 < KBS1) KBS2 += 1;

        for(int i = 0; i < KBS2; i ++) System.out.print("1");
        for(int i = 0; i < KBS2 - 1; i ++) System.out.print("4");

        sc.close();
    }
}