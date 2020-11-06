# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 06                             | #
# | 1941 소문난 칠공주                  | #
# -------------------------------------- #

def find_way(loc, cnt_S, cnt_Y, visited):
    r, c = loc
    tmp = board[r][c]

    if tmp == 'S':
        cnt_S += 1
    
    else:
        cnt_Y += 1
    
    if cnt_Y > 3:
        return
    
    if cnt_S + cnt_Y == 7:
        save = []

        for v_r, v_c in visited + [(r, c)]:
            save.append(locs[(v_r, v_c)])
        
        save.sort()
        result.add(' '.join(save))
        return
    
    visit[r][c] = 1
    can_go = set()

    for v_r, v_c in visited + [(r, c)]:
        for mv_r, mv_c in mv:
            tmp_r = v_r + mv_r
            tmp_c = v_c + mv_c
            
            if 0 <= tmp_r < 5 and 0 <= tmp_c < 5:
                if not visit[tmp_r][tmp_c]:
                    can_go.add(tuple([tmp_r, tmp_c]))

    for tmp_r, tmp_c in can_go:
        if 0 <= tmp_r < 5 and 0 <= tmp_c < 5:
            if not visit[tmp_r][tmp_c]:
                find_way((tmp_r, tmp_c), cnt_S, cnt_Y, visited + [(r, c)])

    visit[r][c] = 0


if __name__ == "__main__":
    board = [list(r_input().rstrip()) for _ in range(5)]

    locs = {}
    tmp = 0

    for row in range(5):
        for col in range(5):
            locs[(row, col)] = str(tmp)
            tmp += 1

    result = set()
    mv = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visit = [[0] * 5 for _ in range(5)]

    for row in range(5):
        for col in range(5):
            find_way((row, col), 0, 0, [])
    
    print(len(result))
