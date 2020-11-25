# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 24                             | #
# | 11747 수열                          | #
# -------------------------------------- #


def run():
    N = int(r_input())
    save = [0] * 1000
    acc = [0] * 1000

    for str_input_list in sys.stdin:
        input_list = list(map(int, str_input_list.split()))

        for number in input_list:
            new_save = [0] * 1000

            new_save[number] = 1
            acc[number] = 1

            for i, val in enumerate(save):
                if val:
                    new_ind = int(str(i) + str(number))

                    if new_ind < 1000:
                        new_save[new_ind] = 1
                        acc[new_ind] = 1

            save = new_save
    
    print(acc.index(0))


if __name__ == "__main__":
    run()
