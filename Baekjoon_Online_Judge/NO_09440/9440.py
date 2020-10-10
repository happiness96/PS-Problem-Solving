# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 10                             | #
# | 9440 숫자 더하기                    | #
# -------------------------------------- #


if __name__ == "__main__":
    while True:
        numbers = list(map(int, r_input().split()))
        
        if numbers[0] == 0:
            break
        
        N, *numbers = numbers
        numbers.sort()
        
        zero_count = numbers.count(0)

        res1 = ''
        res2 = ''

        res1 += str(numbers[zero_count]) + '0' * (zero_count // 2 + zero_count % 2)
        res2 += str(numbers[zero_count + 1]) + '0' * (zero_count // 2)

        for ind in range(zero_count + 2, N):
            if ind % 2:
                res2 += str(numbers[ind])
            
            else:
                res1 += str(numbers[ind])

        print(int(res1) + int(res2))
