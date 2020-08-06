# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 06                             | #
# | 3967 매직 스타                     | #
# -------------------------------------- #


def print_result():
    print('.' * 4 + magic_star[0] + '.' * 4)
    print('.' + magic_star[1] + '.' + magic_star[2] + '.' + magic_star[3] + '.' + magic_star[4] + '.')
    print('.' * 2 + magic_star[5] + '.' * 3 + magic_star[6] + '.' * 2)
    print('.' + magic_star[7] + '.' + magic_star[8] + '.' + magic_star[9] + '.' + magic_star[10] + '.')
    print('.' * 4 + magic_star[11] + '.' * 4)

    sys.exit()


def make_star(ind):
    if ind == 12:
        print_result()

    if ind in fixed:
        make_star(ind + 1)
    
    else:
        for alphabet_num in range(1, 27):
            flag = 0

            for chk in chk_list:
                if ind in chk:
                    alphabet = chr(64 + alphabet_num)

                    if alphabet in magic_star:
                        continue

                    total = alphabet_num
                    blank_cnt = 0

                    for chk_ind in chk:
                        if magic_star[chk_ind] == 'x':
                            blank_cnt += 1
                        
                        else:
                            total += ord(magic_star[chk_ind]) - 64
                    
                    if blank_cnt != 1 and total >= 26:
                        break

                    if blank_cnt == 1 and total != 26:
                        break
                    
                    flag += 1
            
            if flag == 2:
                magic_star[ind] = alphabet
                make_star(ind + 1)
                magic_star[ind] = 'x'


if __name__ == "__main__":
    magic_star = []
    fixed = {}
    chk_list = [[0, 2, 5, 7], [0, 3, 6, 10], [1, 2, 3, 4], [1, 5, 8, 11], [7, 8, 9, 10], [4, 6, 9, 11]]

    for _ in range(5):
        for val in r_input().rstrip():
            if val != '.':
                if val != 'x':
                    fixed[len(magic_star)] = val

                magic_star.append(val)
    
    make_star(0)
    