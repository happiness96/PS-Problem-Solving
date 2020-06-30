# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 30                   | #
# | 19237 어른 상어           | #
# ---------------------------- #


def run():
    N, M, k = map(int, r_input().split())

    sharks = {}

    for row in range(N):
        line = list(map(int, r_input().split()))
        
        for col in range(N):
            if line[col]:
                sharks[line[col]] = [row, col]
    
    for ind, di in enumerate(map(int, r_input().split())):
        sharks[ind + 1] += [di]
    
    priority_dir = {}

    for no in range(1, M + 1):
        priority_dir[no] = [list(map(int, r_input().split())) for _ in range(4)]

    smell_loc = {}

    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    for time in range(1001):
        if len(sharks) == 1:
            print(time)
            sys.exit()

        updated_smell = {}

        for loc, val in smell_loc.items():
            val[1] -= 1
        
            if val[1]:
                updated_smell[loc] = val
        
        smell_loc = updated_smell

        location = {}


        for no, val in sharks.items():
            row, col, direction = val
            smell_loc[(row, col)] = [no, k]

        for no, val in sharks.items():
            row, col, direction = val
            flag = 0

            for next_dir in priority_dir[no][direction - 1]:
                tmp_row = row + dx[next_dir]
                tmp_col = col + dy[next_dir]

                if 0 <= tmp_row < N and 0 <= tmp_col < N:
                    if (tmp_row, tmp_col) not in smell_loc:
                        flag = 1
                        direction = next_dir

                        sharks[no] = [tmp_row, tmp_col, direction]

                        if (tmp_row, tmp_col) not in location:
                            location[tmp_row, tmp_col] = []
                        
                        location[(tmp_row, tmp_col)].append(no)
                        break
            
            if flag:
                continue
        
            for next_dir in priority_dir[no][direction - 1]:
                tmp_row = row + dx[next_dir]
                tmp_col = col + dy[next_dir]

                if 0 <= tmp_row < N and 0 <= tmp_col < N:
                    if smell_loc[(tmp_row, tmp_col)][0] == no:
                        flag = 1
                        direction = next_dir

                        sharks[no] = [tmp_row, tmp_col, direction]

                        if (tmp_row, tmp_col) not in location:
                            location[tmp_row, tmp_col] = []
                        
                        location[(tmp_row, tmp_col)].append(no)
                        break
        
        for loc, vals in location.items():
            if len(vals) != 1:
                vals.sort()
                for no in vals[1:]:
                    sharks.pop(no)
    
    print(-1)


if __name__ == "__main__":
    run()
