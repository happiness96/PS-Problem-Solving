# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 17952 과제는 끝나지 않아!   | #
# ---------------------------- #


def run():
    N = int(r_input())

    score = 0

    stack = []

    for _ in range(N):
        query = r_input().rstrip()

        if query == '0':
            if stack:
                sc, rem = stack.pop()
                rem -= 1

                if rem == 0:
                    score += sc
                
                else:
                    stack.append((sc, rem))
        
        else:
            _, A, T = map(int, query.split())

            T -= 1

            if T == 0:
                score += A
            
            else:
                stack.append((A, T))
        
    print(score)


if __name__ == "__main__":
    run()
