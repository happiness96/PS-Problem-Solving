# -*- encoding: utf-8 -*-
import sys

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 29                             | #
# | 자물쇠와 열쇠                       | #
# -------------------------------------- #


def spin(M, old_key):
    new_key = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            new_key[i][j] = old_key[M - j - 1][i]
    
    return new_key


def solution(key, lock):
    hole = 0

    for row in lock:
        hole += row.count(0)
    
    N = len(lock)
    M = len(key)
    
    for _ in range(4):
        for start_row in range(-M, N):
            for start_col in range(-M, N):
                flag = 1
                solved = 0
                
                for key_row in range(M):
                    hole_row = start_row + key_row

                    if hole_row >= N or hole_row < 0:
                        continue

                    for key_col in range(M):
                        hole_col = start_col + key_col

                        if hole_col >= N or hole_col < 0:
                            continue

                        if not key[key_row][key_col] ^ lock[hole_row][hole_col]:
                            flag = 0
                            break

                        elif not lock[hole_row][hole_col]:
                            solved += 1

                            if solved > hole:
                                break

                    if not flag:
                        break
                
                if solved == hole:
                    return True

        key = spin(M, key)

    return False
