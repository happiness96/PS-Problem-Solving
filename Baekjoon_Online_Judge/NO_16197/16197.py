# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 16                   | #
# | 16197 두 동전             | #
# ---------------------------- #


def run():
    N, M = map(int, r_input().split())

    board = []
    coins = []

    for row in range(N):
        line = list(r_input().rstrip())

        for col in range(M):
            if line[col] == 'o':
                coins.append((row, col))
        
        board.append(line)

    mv_cnt = 1
    queue = deque([coins])

    mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visit = []

    while queue:
        for _ in range(len(queue)):
            coin_statement = queue.popleft()
            
            if coin_statement in visit:
                continue

            visit.append(coin_statement)
            
            for ind in range(4):
                new_coin_statement = []
                f_cnt = 0

                for row, col in coin_statement:
                    new_row = row + mv[ind][0]
                    new_col = col + mv[ind][1]

                    if 0 <= new_row < N and 0 <= new_col < M:
                        if board[new_row][new_col] == '#':
                            new_coin_statement.append((row, col))
                        
                        else:
                            new_coin_statement.append((new_row, new_col))

                    else:
                        f_cnt += 1
                
                if f_cnt == 1:
                    print(mv_cnt)
                    sys.exit()

                if f_cnt > 1 or new_coin_statement == coin_statement:
                    continue
                
                queue.append(new_coin_statement)

        mv_cnt += 1

        if mv_cnt == 11:
            break
    
    print(-1)


if __name__ == "__main__":
    run()
