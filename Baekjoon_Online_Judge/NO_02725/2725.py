# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 03                             | #
# | 2725 보이는 점의 개수               | #
# -------------------------------------- #


def get_gcd(num1, num2):
    mod = num2 % num1

    if mod == 0:
        return num1
    
    else:
        return get_gcd(mod, num1)


def run():
    C = int(r_input())

    save = [0, 3, 5]

    for n in range(3, 1001):
        tmp = 1

        for k in range(2, n):
            tmp += int(get_gcd(k, n) == 1)
        
        save.append(save[-1] + tmp * 2)


    for _ in range(C):
        N = int(r_input())

        print(save[N])

if __name__ == "__main__":
    run()
