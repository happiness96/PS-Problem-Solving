# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 28                   | #
# | 3412 Darts               | #
# ---------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        n = int(r_input())
        score = 0

        for _ in range(n):
            x, y = map(int, r_input().split())

            x = abs(x)
            y = abs(y)

            hit = (x ** 2 + y ** 2) ** 0.5
            
            for sc in range(1, 11):
                if hit <= 20 * (11 - sc):
                    score += 1
                
                else:
                    break
        
        print(score)


if __name__ == "__main__":
    run()
