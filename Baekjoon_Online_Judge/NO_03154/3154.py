# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 11                             | #
# | 3154 알람시계                        | #
# -------------------------------------- #


def run():
    locations = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}

    h, m = map(int, r_input().rstrip().split(':'))

    res_h = 0
    res_m = 0
    res_cost = sys.maxsize

    chk1 = 0

    while True:
        hour = h + 24 * chk1

        if hour >= 100:
            break
        
        chk2 = 0

        while True:
            minute = m + 60 * chk2

            if minute >= 100:
                break

            cost = 0
            comb = '0' * (2 - len(str(hour))) + str(hour) + '0' * (2 - len(str(minute))) + str(minute)

            for i in range(1, 4):
                x1, y1 = locations[int(comb[i])]
                x2, y2 = locations[int(comb[i - 1])]

                cost += abs(x1 - x2) + abs(y1 - y2)
            
            if cost < res_cost:
                res_h = hour
                res_m = minute
                res_cost = cost

            chk2 += 1
        
        chk1 += 1

    print("%02d:%02d" % (res_h, res_m))


if __name__ == "__main__":
    run()
