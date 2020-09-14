# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 13                             | #
# | 1283 단축키 지정                    | #
# -------------------------------------- #


def run():
    N = int(r_input())

    visit = [0] * 26

    for _ in range(N):
        option = r_input().rstrip()

        option_list = map(str, option.split())

        res = -1

        for ch in option_list:
            first = ch[0]

            if 'A' <= first <= 'Z':
                ind = ord(first) - ord('A')

                if not visit[ind]:
                    visit[ind] = 1
                    res = option.index(ch)
                    break
            
            elif 'a' <= first <= 'z':
                ind = ord(first) - ord('a')

                if not visit[ind]:
                    visit[ind] = 1
                    res = option.index(ch)
                    break
        
        if res == -1:
            for ch_ind, ch in enumerate(option):
                if 'A' <= ch <= 'Z':
                    ind = ord(ch) - ord('A')

                    if not visit[ind]:
                        visit[ind] = 1
                        res = option.index(ch)
                        break

                elif 'a' <= ch <= 'z':
                    ind = ord(ch) - ord('a')

                    if not visit[ind]:
                        visit[ind] = 1
                        res = option.index(ch)
                        break
        
        for ch_ind, ch in enumerate(option):
            if res != -1 and ch_ind == res:
                print('[' + ch + ']', end='')
            
            else:
                print(ch, end='')
        
        print()


if __name__ == "__main__":
    run()
