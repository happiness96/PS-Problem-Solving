# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 15                             | #
# | 2660 회장뽑기                       | #
# -------------------------------------- #


def run():
    N = int(r_input())
    INF = 100

    friends_score = [[INF] * (N + 1) for _ in range(N + 1)]

    while True:
        A, B = map(int, r_input().split())

        if A == B == -1:
            break
        
        friends_score[A][B] = 1
        friends_score[B][A] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                tmp = friends_score[k][i] + friends_score[i][j]

                if friends_score[k][j] > tmp:
                    friends_score[k][j] = tmp
    
    for i in range(1, N + 1):
        friends_score[i][i] = 0

    min_score = sys.maxsize
    result = []

    for num, f in enumerate(friends_score):
        tmp = max(f[1:])

        if tmp == min_score:
            result.append(num)
        
        elif tmp < min_score:
            min_score = tmp
            result = [num]
    
    print(min_score, len(result))
    print(*result)


if __name__ == "__main__":
    run()
