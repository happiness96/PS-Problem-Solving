# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 14                             | #
# | 1038 감소하는 수                    | #
# -------------------------------------- #


def run():
    N = int(r_input()) + 1

    save = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    while N and save:
        new_save = []

        for num in save:
            N -= 1

            if not N:
                print(num)
                sys.exit()
            
            for plu in range(int(str(num)[0]) + 1, 10):
                new_save.append((int(str(plu) + str(num))))
            
        save = sorted(new_save)

    print(-1)


if __name__ == "__main__":
    run()
