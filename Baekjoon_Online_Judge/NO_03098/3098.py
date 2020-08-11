# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 11                             | #
# | 3098 소셜네트워크                   | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    con = {node: set() for node in range(1, N + 1)}

    for _ in range(M):
        A, B = map(int, r_input().split())

        con[A].add(B)
        con[B].add(A)
    
    res = []

    while True:
        new_connection = set()

        for start in range(1, N + 1):
            for friend in con[start]:
                for friend_friends in con[friend]:
                    if start != friend_friends and friend_friends not in con[start]:
                        new_connection.add(tuple(sorted([start, friend_friends])))
        
        if not new_connection:
            break
        
        res.append(len(new_connection))

        for A, B in new_connection:
            con[A].add(B)
            con[B].add(A)
    
    print(len(res))
    print(*res, sep='\n')


if __name__ == "__main__":
    run()
