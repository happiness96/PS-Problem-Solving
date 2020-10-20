# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 20                             | #
# | 20058 마법사 상어와 파이어스톰       | #
# -------------------------------------- #


def run():
    N, Q = map(int, r_input().split())
    size = 2 ** N
    A = [list(map(int, r_input().split())) for _ in range(size)]

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    for L in map(int, r_input().split()):
        new_A = [[0] * size for _ in range(size)]

        step_size = 2 ** L

        for start_row in range(0, size, step_size):
            for start_col in range(0, size, step_size):
                for mv_row in range(step_size):
                    for mv_col in range(step_size):
                        row, col = start_row + mv_row, start_col + mv_col
                        new_A[row][col] = A[start_row + step_size - mv_col - 1][start_col + mv_row]

        dec = []

        for row in range(size):
            for col in range(size):
                if new_A[row][col]:
                    ice_cnt = 0

                    for k in range(4):
                        tmp_row = row + dx[k]
                        tmp_col = col + dy[k]

                        if 0 <= tmp_row < size and 0 <= tmp_col < size:
                            if new_A[tmp_row][tmp_col]:
                                ice_cnt += 1
                    
                    if ice_cnt < 3:
                        dec.append((row, col))
        
        for row, col in dec:
            new_A[row][col] -= 1
        
        A = new_A

    maxi = 0
    res = 0

    visit = [[0] * size for _ in range(size)]

    for row in range(size):
        res += sum(A[row])

        for col in range(size):

            if A[row][col] and not visit[row][col]:
                visit[row][col] = 1
                cnt = 1

                queue = [(row, col)]

                while queue:
                    r, c = queue.pop()

                    for k in range(4):
                        tmp_row = r + dx[k]
                        tmp_col = c + dy[k]

                        if 0 <= tmp_row < size and 0 <= tmp_col < size:
                            if A[tmp_row][tmp_col] and not visit[tmp_row][tmp_col]:
                                cnt += 1
                                visit[tmp_row][tmp_col] = 1
                                queue.append((tmp_row, tmp_col))

                maxi = max(maxi, cnt)
    
    print(res)
    print(maxi)


if __name__ == "__main__":
    run()
