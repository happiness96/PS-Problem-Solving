# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 20                   | #
# | 2765 자전거 속도           | #
# ---------------------------- #


if __name__ == "__main__":
    test_case_cnt = 1
    PI = 3.1415927

    while True:
        diameter, rotate_cnt, time = map(float, r_input().split())

        if rotate_cnt == 0:
            break

        radius = (diameter / 2) / (5280 * 12)

        distance = PI * radius * 2 * rotate_cnt
        
        print("Trip #" + str(test_case_cnt) + ': %.2f %.2f' % (distance, distance / time * 3600))
        
        test_case_cnt += 1
