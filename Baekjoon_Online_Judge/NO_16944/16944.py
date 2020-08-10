# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 10                             | #
# | 16944 강력한 비밀번호               | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    password = r_input().rstrip()

    num_flag = 1
    lower_flag = 1
    upper_flag = 1
    special_flag = 1

    for ch in password:
        if ch in '0123456789':
            num_flag = 0

        elif ch in 'qwertyuiopasdfghjklzxcvbnm':
            lower_flag = 0
        
        elif ch in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            upper_flag = 0
        
        elif ch in '!@#$%^&*()-+':
            special_flag = 0
    
    total_length = len(password) + num_flag + lower_flag + upper_flag + special_flag

    print(num_flag + lower_flag + upper_flag + special_flag + max(0, 6 - total_length))
