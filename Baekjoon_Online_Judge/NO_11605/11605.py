# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 10                             | #
# | 11605 Magic Trick                  | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    save = []

    for _ in range(n):
        operation, number = map(str, r_input().rstrip().split())

        number = int(number)

        save.append([operation, number])
    
    cnt = 0

    for k in range(1, 101):
        num = k
        
        for operation, number in save:
            if operation == 'ADD':
                num += number
            
            elif operation == 'SUBTRACT':
                num -= number
            
            elif operation == 'MULTIPLY':
                num *= number
            
            else:
                num /= number
            
            if num < 0 or num % 1:
                cnt += 1
                break
    
    print(cnt)
