package Baekjoon_Online_Judge.NO_02884;

import java.util.Scanner;

/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 08                           | 
 | Day 31                             | 
 | 알람 시계                          | 
 -------------------------------------- 
*/
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int H = sc.nextInt(), M = sc.nextInt();

        M -= 45;

        if (M < 0){
            M += 60;
            H --;
        }

        if (H < 0) H += 24;

        System.out.printf("%d %d", H, M);
        sc.close();
    }
}