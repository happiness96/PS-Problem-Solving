package Baekjoon_Online_Judge.NO_01157;

import java.util.Scanner;

/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 02                             | 
 | 단어 공부                           | 
 -------------------------------------- 
*/
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        char res = '?';
        int length = s.length(), max_cnt = 0, counting[] = new int[26];

        s = s.toUpperCase();
        
        for (int ind = 0; ind < length; ind ++) counting[s.charAt(ind) - 'A'] ++;

        for (int i = 0; i < 26; i ++){
            if (counting[i] > max_cnt){
                max_cnt = counting[i];
                res = (char)(65 + i);
            }

            else if (counting[i] == max_cnt) res = '?';
        }

        System.out.println(res);
        
        sc.close();
    }
    
}
