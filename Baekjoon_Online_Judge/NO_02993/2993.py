# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 07                   | #
# | 2993 세 부분              | #
# ---------------------------- #


if __name__ == "__main__":
    word = r_input().rstrip()
    length = len(word)

    result = word

    for i in range(1, length - 1):
        for j in range(i + 1, length):
            tmp = word[:i][::-1] + word[i: j][::-1] + word[j:][::-1]
            
            result = min(result, tmp)
    
    print(result)
