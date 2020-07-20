/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 19                   | 
 | 5522 카드 게임             | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int total = 0;

        Scanner sc = new Scanner(System.in);

        for(int i = 0; i < 5; i ++){
            int number = sc.nextInt();
            total += number;
        }

        System.out.println(total);
        sc.close();
    }
}