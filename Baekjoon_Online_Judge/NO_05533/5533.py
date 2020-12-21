# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 5533 유니크                        | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    cards = [list(map(int, r_input().split())) for _ in range(N)]
    result = [0] * N

    for player1 in range(N):
        for game_no in range(3):
            flag = 1

            for player2 in range(N):
                if player1 != player2 and cards[player1][game_no] == cards[player2][game_no]:
                    flag = 0
                    break
            
            if flag:
                result[player1] += cards[player1][game_no]
    
    print(*result, sep='\n')
