package Baekjoon_Online_Judge.NO_04344;

import java.util.Scanner;

/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 평균은 넘겠지                       | 
 -------------------------------------- 
*/
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int C = sc.nextInt();

        for (int i = 0; i < C; i ++){
            int N = sc.nextInt(), total = 0;
            int scores[] = new int[N];
            
            for (int j = 0; j < N; j ++){
                scores[j] = sc.nextInt();
                total += scores[j];
            }

            double avg = total / N;
            int over_avg = 0;

            for (int j = 0; j < N; j ++){
                if (scores[j] > avg) over_avg ++;
            }

            System.out.printf("%.3f%%\n", (double)over_avg / N * 100);
        }

        sc.close();
    }
}