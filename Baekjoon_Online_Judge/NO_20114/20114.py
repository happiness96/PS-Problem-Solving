# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 01                             | #
# | 20114 미아 노트                     | #
# -------------------------------------- #


if __name__ == "__main__":
    N, H, W = map(int, r_input().split())

    word = [r_input().rstrip() for _ in range(H)]

    for ind in range(N):
        flag = 0

        for row in range(H):
            for col in range(ind * W, (ind + 1) * W):
                if word[row][col] != '?':
                    print(word[row][col], end='')
                    flag = 1
                    break
            
            if flag:
                break
        
        if not flag:
            print('?', end='')
