# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 28                   | #
# | 배드민턴                  | #
# ---------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for testcase in range(1, T + 1):
        res = r_input().rstrip()

        a_score = b_score = win = 0

        for val in res:
            if val == 'A':
                a_score += 1

                if a_score == 21:
                    win = 1
                    break
            
            else:
                b_score += 1

                if b_score == 21:
                    win = 2
                    break
        
        print('Case #' + str(testcase))
        print(['Playing', 'Alice', 'Bob'][win])
