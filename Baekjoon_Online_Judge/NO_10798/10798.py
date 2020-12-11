# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 11                             | #
# | 10798 세로읽기                      | #
# -------------------------------------- #


if __name__ == "__main__":
    max_length = 0
    save = []
    lengths = []

    for _ in range(5):
        word = r_input().rstrip()
        length = len(word)

        max_length = max(max_length, length)
        save.append(word)
        lengths.append(length)
    
    for col in range(max_length):
        for row in range(5):
            if col < lengths[row]:
                print(save[row][col], end='')
