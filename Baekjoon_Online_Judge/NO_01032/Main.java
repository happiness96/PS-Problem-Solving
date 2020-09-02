package Baekjoon_Online_Judge.NO_01032;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 02                             | 
 | 명령 프롬프트                       | 
 -------------------------------------- 
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N, len;
        String form;

        N = sc.nextInt();
        sc.nextLine();
        form = sc.nextLine();
        
        len = form.length();

        for (int i = 1; i < N; i ++){
            String str;
            str = sc.nextLine();

            for (int ind = 0; ind < len; ind ++){
                if (str.charAt(ind) != form.charAt(ind)) form = form.substring(0, ind) + '?' + form.substring(ind + 1);
            }
        }

        System.out.println(form);
        sc.close();
    }
}
