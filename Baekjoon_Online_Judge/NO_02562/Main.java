package Baekjoon_Online_Judge.NO_02562;

import java.util.Scanner;

/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 최댓값                              | 
 -------------------------------------- 
*/
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int result = 0, result_ind = 0;

        for (int ind = 1; ind < 10; ind ++){
            int number = sc.nextInt();

            if (number > result){
                result = number;
                result_ind = ind;
            }
        }
        
        System.out.println(result);
        System.out.println(result_ind);

        sc.close();
    }
}