# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 08                   | #
# | 3187 양치기 꿍             | #
# ---------------------------- #


def run():
    R, C = map(int, r_input().split())
    board = []
    visit = [[0] * C for _ in range(R)]

    for row in range(R):
        line = list(r_input().rstrip())

        for col in range(C):
            if line[col] == '#':
                visit[row][col] = 1
            
        board.append(line)

    wolf = 0
    sheep = 0

    for row in range(R):
        for col in range(C):
            if not visit[row][col]:
                queue = [(row, col)]
                visit[row][col] = 1

                tmp_wolf = 0
                tmp_sheep = 0

                while queue:
                    r, c = queue.pop()

                    if board[r][c] == 'v':
                        tmp_wolf += 1
                    
                    elif board[r][c] == 'k':
                        tmp_sheep += 1

                    for mv_r, mv_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        tmp_row = r + mv_r
                        tmp_col = c + mv_c

                        if 0 <= tmp_row < R and 0 <= tmp_col < C:
                            if not visit[tmp_row][tmp_col]:
                                visit[tmp_row][tmp_col] += 1
                                queue.append((tmp_row, tmp_col))
                
                if tmp_sheep > tmp_wolf:
                    sheep += tmp_sheep
                
                else:
                    wolf += tmp_wolf
    
    print(sheep, wolf)


if __name__ == "__main__":
    run()
