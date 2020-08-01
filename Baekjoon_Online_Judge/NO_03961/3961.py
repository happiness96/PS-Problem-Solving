# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 01                   | #
# | 3961 터치스크린 키보드      | #
# ---------------------------- #


def run():
    keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    key_loc = {}

    for row, key_line in enumerate(keyboard):
        for col, key in enumerate(key_line):
            key_loc[key] = [row, col]
    
    t = int(r_input())

    for _ in range(t):
        word, l = map(str, r_input().rstrip().split())

        save = {}

        for _ in range(int(l)):
            input_word = r_input().rstrip()

            distance = 0

            for ind, w in enumerate(word):
                distance += abs(key_loc[w][0] - key_loc[input_word[ind]][0]) + abs(key_loc[w][1] - key_loc[input_word[ind]][1])

                if distance not in save:
                    save[distance] = []
                
            save[distance].append(input_word)

        for cnt in sorted(save):
            for res in sorted(save[cnt]):
                print(res, cnt)


if __name__ == "__main__":
    run()
