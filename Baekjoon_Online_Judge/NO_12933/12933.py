# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 11                             | #
# | 12933 오리                          | #
# -------------------------------------- #


if __name__ == "__main__":
    sound = r_input().rstrip()
    tmp = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}

    save = []

    flag = 1

    for ch in sound:
        tmp_ind = tmp[ch]
        
        if tmp_ind not in save:
            if tmp_ind != 0:
                flag = 0
                break

            save.append(1)
        
        else:
            loc = save.index(tmp_ind)
            
            save[loc] = (save[loc] + 1) % 5
    result = len(save)

    if save != [0] * result:
        flag = 0

    print(-1 if not flag else result)
