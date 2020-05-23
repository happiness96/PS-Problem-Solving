# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 23                   | #
# | 13270 피보나치 치킨        | #
# ---------------------------- #


def run():
    N = int(r_input())

    fibo = [0, 1, 1]

    while True:
        fibo.append(fibo[-1] + fibo[-2])
        
        if fibo[-1] >= N:
            break
    
    INF = sys.maxsize

    min_array = [INF] * (N + 1)
    max_array = [0] * (N + 1)

    min_array[0] = 0

    for ind in range(N):
        for fibo_ind in range(3, len(fibo)):
            tmp_ind = ind + fibo[fibo_ind]

            if tmp_ind > N:
                break

            min_array[tmp_ind] = min(min_array[tmp_ind], min_array[ind] + fibo[fibo_ind - 1])
            max_array[tmp_ind] = max(max_array[tmp_ind], max_array[ind] + fibo[fibo_ind - 1])
    
    print(min_array[-1], max_array[-1])


if __name__ == "__main__":
    run()
