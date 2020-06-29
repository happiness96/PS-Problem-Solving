# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 29                   | #
# | 3895 그리고 하나가 남았다   | #
# ---------------------------- #


def run():
    while True:
        n, k, m = map(int, r_input().split())

        if not n:
            break
        
        save = list(range(1, n + 1))
        save.pop(m - 1)

        last_ind = m - 1
        maxi = n - 1

        while maxi != 1:
            last_ind += k - 1

            while last_ind >= maxi:
                last_ind -= maxi
            
            save.pop(last_ind)
            maxi -= 1
        
        print(save[0])


if __name__ == "__main__":
    run()
