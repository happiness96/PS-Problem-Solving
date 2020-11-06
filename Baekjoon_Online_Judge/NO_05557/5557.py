# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 06                             | #
# | 5557 1학년                          | #
# -------------------------------------- #


def run():
    N = int(r_input())
    numbers = list(map(int, r_input().split()))
    result = 0

    left_numbers = numbers[: -1]
    right_number = numbers[-1]
        
    left_dp = [0] * 21
    left_dp[left_numbers[0]] = 1

    for val in left_numbers[1:]:
        new_left_dp = [0] * 21

        for ind, cnt in enumerate(left_dp):
            tmp = ind - val
            
            if 0 <= tmp:
                new_left_dp[tmp] += cnt
            
            tmp = ind + val

            if tmp < 21:
                new_left_dp[tmp] += cnt
        left_dp = new_left_dp
        
    result = left_dp[right_number]
    
    print(result)


if __name__ == "__main__":
    run()
