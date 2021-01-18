# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 18                             | #
# | 1021 회전하는 큐                    | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    array = list(range(1, N + 1))
    order = list(map(int, r_input().split()))

    result = 0

    for find in order:
        ind = array.index(find)

        left = ind
        right = len(array) - ind

        if left < right:
            result += left
        
        else:
            result += right
        
        array = array[left + 1:] + array[: left]
    
    print(result)
