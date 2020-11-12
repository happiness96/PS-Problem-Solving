# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 12                             | #
# | 7789 텔레프라임                     | #
# -------------------------------------- #


def run():
    phone_number, new_number = map(str, r_input().rstrip().split())
    new_phone_number = int(new_number + phone_number)
    phone_number = int(phone_number)

    for num in range(3, phone_number // 2 + 1, 2):
        if not phone_number % num:
            print('No')
            sys.exit()

    for num in range(3, new_phone_number // 2 + 1, 2):
        if not new_phone_number % num:
            print('No')
            sys.exit()
        
    if not phone_number % 2 or not new_phone_number % 2 or phone_number == 1 or new_phone_number == 1:
        print('No')
        sys.exit()
    
    print('Yes')


if __name__ == "__main__":
    run()
