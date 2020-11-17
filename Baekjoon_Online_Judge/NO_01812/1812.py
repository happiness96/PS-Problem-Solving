# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 17                             | #
# | 1812 사탕                          | #
# -------------------------------------- #


def run():
    N = int(r_input())

    tot_candies = [int(r_input()) for _ in range(N)]
    
    for num in range(tot_candies[0] + 1):
        save = tot_candies[0] - num
        save_list = [num, save]
        flag = 1

        for ind in range(1, N):
            save = tot_candies[ind] - save
            if save < 0:
                flag = 0
                break
            
            save_list.append(save)
        
        if flag and save == num:
            save_list.pop()

            print(*save_list, sep='\n')
            sys.exit()


if __name__ == "__main__":
    run()
