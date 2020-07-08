# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 08                   | #
# | 2668 숫자고르기            | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    
    integer = {ind: int(r_input()) for ind in range(1, N + 1)}
    result = []

    visit = [0] * (N + 1)

    for ind in range(1, N + 1):
        save = []

        if not visit[ind]:
            num = ind
            save.append(num)
            visit[num] = 1

            while True:
                num = integer[num]
                
                if visit[num]:
                    if num in save:
                        result += save[save.index(num):]
                    break
                
                save.append(num)
                visit[num] = 1
    
    print(len(result))
    print(*sorted(result), sep='\n')
