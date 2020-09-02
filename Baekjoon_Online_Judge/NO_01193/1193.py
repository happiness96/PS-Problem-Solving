# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | 분수 찾기                           | #
# -------------------------------------- #


if __name__ == "__main__":
    X = int(r_input())

    flag = 0
    acc = 0
    plu = 1

    while True:
        if acc < X <= acc + plu:
            X -= acc

            if flag:
                print(str(str(X) + '/' + str(plu - X + 1)))
            
            else:
                print(str(str(plu - X + 1) + '/' + str(X)))
            
            break
        
        acc += plu
        plu += 1
        flag = abs(flag - 1)
