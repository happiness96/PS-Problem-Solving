# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 20                   | #
# | 2756 다트                 | #
# ---------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        shoot = list(map(float, r_input().split()))

        player1 = player2 = 0

        for ind in range(0, 5, 2):
            dist = (shoot[ind] ** 2 + shoot[ind + 1] ** 2) ** (1 / 2)
            
            for i, sc in enumerate([3, 6, 9, 12, 15]):
                if dist <= sc:
                    player1 += 20 * (5 - i)
                    break
        
        for ind in range(6, 11, 2):
            dist = (shoot[ind] ** 2 + shoot[ind + 1] ** 2) ** (1 / 2)
            
            for i, sc in enumerate([3, 6, 9, 12, 15]):
                if dist <= sc:
                    player2 += 20 * (5 - i)
                    break
        
        print('SCORE:', player1, 'to', player2, end=', ')
        print('PLAYER 1 WINS.' if player1 > player2 else 'PLAYER 2 WINS.' if player1 < player2 else 'TIE.')


if __name__ == "__main__":
    run()
