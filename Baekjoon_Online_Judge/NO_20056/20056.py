# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 20                             | #
# | 20056 마법사 상어와 파이어볼         | #
# -------------------------------------- #


def run():
    N, M, K = map(int, r_input().split())

    fire_balls = {}
    mv = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    for _ in range(M):
        r, c, m, s, d = map(int, r_input().split())

        if (r, c) not in fire_balls:
            fire_balls[(r, c)] = []
        
        fire_balls[(r, c)].append((m, s, d))
    
    for _ in range(K):
        new_fire_balls = {}

        for locations, fire_ball_list in fire_balls.items():
            row, col = locations

            for fire_ball in fire_ball_list:
                m, s, d = fire_ball

                mv_row, mv_col = mv[d]

                tmp_row = row + mv_row * s
                tmp_col = col + mv_col * s

                tmp_row %= N
                tmp_col %= N

                if tmp_row == 0:
                    tmp_row = N
                
                if tmp_col == 0:
                    tmp_col = N
            
                if (tmp_row, tmp_col) not in new_fire_balls:
                    new_fire_balls[(tmp_row, tmp_col)] = []
                
                new_fire_balls[(tmp_row, tmp_col)].append((m, s, d))
        
        for locations, fire_ball_list in new_fire_balls.items():
            fire_ball_cnt = len(fire_ball_list)

            if fire_ball_cnt > 1:
                total_m = 0
                total_s = 0

                splited_fire_balls = []
                check_list = []

                for fire_ball in fire_ball_list:
                    m, s, d = fire_ball
                    total_m += m
                    total_s += s

                    check_list.append(d % 2)
                
                new_m = total_m // 5

                if new_m >= 1:
                    new_s = total_s // fire_ball_cnt
                    
                    if check_list in [[0] * fire_ball_cnt, [1] * fire_ball_cnt]:
                        for new_d in [0, 2, 4, 6]:
                            splited_fire_balls.append((new_m, new_s, new_d))
                    
                    else:
                        for new_d in [1, 3, 5, 7]:
                            splited_fire_balls.append((new_m, new_s, new_d))
                
                new_fire_balls[locations] = splited_fire_balls
        
        fire_balls = new_fire_balls

    result = 0

    for _, fire_ball_list in fire_balls.items():
        for m, _, _ in fire_ball_list:
            result += m
    
    print(result)


if __name__ == "__main__":
    run()
