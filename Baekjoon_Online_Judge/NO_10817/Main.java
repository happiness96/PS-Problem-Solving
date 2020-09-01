package Baekjoon_Online_Judge.NO_10817;

import java.util.Arrays;
import java.util.Scanner;

/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 세 수                              | 
 -------------------------------------- 
*/
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numbers[] = new int[3];

        for (int i = 0; i < 3; i ++){
            numbers[i] = sc.nextInt();
        }

        Arrays.sort(numbers);
        
        System.out.println(numbers[1]);

        sc.close();
    }
}