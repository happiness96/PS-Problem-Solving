# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 28                   | #
# | 2848 알고스팟어            | #
# ---------------------------- #


def find_result(alphabet, string):
    global result, res_length

    str_length = len(string)

    if str_length == res_length:
        result.append(string)
    
    elif str_length > res_length:
        res_length = str_length
        result = [string]
    
    for con in connected[alphabet]:
        if con in string:
            print('!')
            sys.exit()
        
        find_result(con, string + con)


if __name__ == "__main__":
    N = int(r_input())

    algospot = {}
    words_list = []

    for _ in range(N):
        word = r_input().rstrip()
        words_list.append(word)

        for w in word:
            if w not in algospot:
                algospot[w] = len(algospot)
    
    first_word = words_list[0]
    second_word = ''

    length = len(algospot)

    connected = {node: [] for node in algospot}

    for i in range(1, N):
        second_word = words_list[i]

        chk_flag = 1

        for ind in range(min(len(first_word), len(second_word))):
            first = first_word[ind]
            second = second_word[ind]

            if first != second:
                chk_flag = 0
                if first in connected[second]:
                    print('!')
                    sys.exit()

                connected[first].append(second)
                break
        
        if chk_flag:
            if len(first_word) > len(second_word):
                print('!')
                sys.exit()
        
        first_word = second_word
    
    res_length = 0
    result = []

    for ch in algospot:
        find_result(ch, ch)

    if res_length != length:
        print('?')
    
    else:
        print(result[0])
