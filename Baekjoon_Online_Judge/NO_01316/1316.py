# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | 그룹 단어 체커                      | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    res = 0

    for _ in range(N):
        word = r_input().rstrip()

        save = [word[0]]
        flag = 1

        for ind in range(1, len(word)):
            if word[ind] == word[ind -1]:
                continue
        
            if word[ind] in save:
                flag = 0
                break
            
            save.append(word[ind])
        
        res += flag
    
    print(res)
