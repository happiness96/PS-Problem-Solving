package Baekjoon_Online_Judge.NO_14659;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 14659 한조서열정리하고옴ㅋㅋ | 
 ---------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), max_height = 0, result = 0, cnt = 0;

        for(int i = 0; i < N; i ++){
            int height = sc.nextInt();

            if(height > max_height){
                max_height = height;
                
                result = Math.max(result, cnt);

                cnt = 0;
            }

            else cnt ++;
        }

        System.out.println(Math.max(result, cnt));

        sc.close();
    }
}