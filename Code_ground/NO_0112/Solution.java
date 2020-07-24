package Code_ground.NO_0112;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 24                   | 
 | 플레이버튼                 | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        int T;
        Scanner sc = new Scanner(System.in);

        T = sc.nextInt();

        for (int testcase = 1; testcase <= T; testcase ++){
            int subscriber = sc.nextInt();

            System.out.println("Case #" + Integer.toString(testcase));
            if(subscriber < 100000) System.out.println("NONE");
            else if(subscriber < 1000000) System.out.println("SILVER");
            else if(subscriber < 10000000) System.out.println("GOLD");
            else System.out.println("DIAMOND");
        }

        sc.close();

    }
}