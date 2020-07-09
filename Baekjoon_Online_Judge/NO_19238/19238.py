# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 08                   | #
# | 19238 스타트 택시          | #
# ---------------------------- #


def run():
    N, M, fuel = map(int, r_input().split())
    board = [[0] * (N + 1)]

    for _ in range(N):
        board.append([0] + list(map(int, r_input().split())))

    taxi_row, taxi_col = map(int, r_input().split())
    dest_loc = {}

    for _ in range(M):
        passenger_row, passenger_col, dest_row, dest_col = map(int, r_input().split())
        board[passenger_row][passenger_col] = 2

        dest_loc[(passenger_row, passenger_col)] = (dest_row, dest_col)

    while M:
        visit = [[0] * (N + 1) for _ in range(N + 1)]
        visit[taxi_row][taxi_col] = 1
        
        queue = deque([(taxi_row, taxi_col)])
        mv = 0

        passenger = []
        
        if board[taxi_row][taxi_col] == 2:
            passenger.append((taxi_row, taxi_col))

        while queue and not passenger:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    tmp_row = row + dx
                    tmp_col = col + dy

                    if 0 < tmp_row <= N and 0 < tmp_col <= N:
                        if not visit[tmp_row][tmp_col]:
                            visit[tmp_row][tmp_col] = 1

                            if board[tmp_row][tmp_col] == 2:
                                passenger.append((tmp_row, tmp_col))
                            
                            elif board[tmp_row][tmp_col] == 0:
                                queue.append((tmp_row, tmp_col))
        
            mv +=1
        
        passenger.sort()
        fuel -= mv
        
        if fuel < 0 or not passenger:
            print(-1)
            break
        
        passenger_row, passenger_col = passenger[0]
        board[passenger_row][passenger_col] = 0

        taxi_row, taxi_col = passenger_row, passenger_col

        queue = deque([(taxi_row, taxi_col)])
        visit = [[0] * (N + 1) for _ in range(N + 1)]
        visit[taxi_row][taxi_col] = 1

        mv = 0
        dest = dest_loc[(passenger_row, passenger_col)]
        flag = 1

        while queue and flag:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if (row, col) == dest:
                    flag = 0
                    break

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    tmp_row = row + dx
                    tmp_col = col + dy

                    if 0 < tmp_row <= N and 0 < tmp_col <= N:
                        if not visit[tmp_row][tmp_col]:
                            visit[tmp_row][tmp_col] = 1

                            if board[tmp_row][tmp_col] != 1:
                                queue.append((tmp_row, tmp_col))

            if flag:
                mv +=1

        fuel -= mv

        if fuel < 0 or flag:
            print(-1)
            break

        fuel += mv * 2
        taxi_row, taxi_col = dest

        M -= 1

    if not M:
        print(fuel)


if __name__ == "__main__":
    run()
