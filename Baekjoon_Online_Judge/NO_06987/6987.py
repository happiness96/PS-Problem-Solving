# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 05                             | #
# | 6987 월드컵                          | #
# -------------------------------------- #


def find_result(team):
    if score_list == [[0] * 3] * 6:
        return 1

    if team == 6:
        return 0
    
    sub_flag = 0
    win, draw, lose = score_list[team]

    for fight in range(6):
        if team != fight:
            if win and score_list[fight][2] and not visit[team][fight]:
                score_list[team][0] -= 1
                score_list[fight][2] -= 1
                visit[team][fight] = 1
                visit[fight][team] = 1

                if score_list[team].count(0) == 3:
                    sub_flag = max(sub_flag, find_result(team + 1))
                
                else:
                    sub_flag = max(sub_flag, find_result(team))
                
                score_list[team][0] += 1
                score_list[fight][2] += 1
                visit[team][fight] = 0
                visit[fight][team] = 0
            
            elif draw and score_list[fight][1] and not visit[team][fight]:
                score_list[team][1] -= 1
                score_list[fight][1] -= 1
                visit[team][fight] = 1
                visit[fight][team] = 1

                if score_list[team].count(0) == 3:
                    sub_flag = max(sub_flag, find_result(team + 1))
                
                else:
                    sub_flag = max(sub_flag, find_result(team))
                
                score_list[team][1] += 1
                score_list[fight][1] += 1
                visit[team][fight] = 0
                visit[fight][team] = 0
            
            elif lose and score_list[fight][0] and not visit[team][fight]:
                score_list[team][2] -= 1
                score_list[fight][0] -= 1
                visit[team][fight] = 1
                visit[fight][team] = 1

                if score_list[team].count(0) == 3:
                    sub_flag = max(sub_flag, find_result(team + 1))
                
                else:
                    sub_flag = max(sub_flag, find_result(team))
                
                score_list[team][2] += 1
                score_list[fight][0] += 1
                visit[team][fight] = 0
                visit[fight][team] = 0

    return sub_flag


if __name__ == "__main__":
    res = []

    for _ in range(4):
        scores = list(map(int, r_input().split()))
        score_list = []
        visit = [[0] * 6 for _ in range(6)]

        for ind in range(6):
            score_list.append(scores[3 * ind: 3 * (ind + 1)])
        
        tot_win = 0
        tot_draw = 0
        tot_lose = 0

        flag = 1

        for score in score_list:
            win, draw, lose = score
            tot_win += win
            tot_draw += draw
            tot_lose += lose

            if sum(score) != 5:
                flag = 0
        
        if tot_win != tot_lose  or tot_win + tot_draw + tot_lose != 30:
            flag = 0
        
        if flag:
            flag = find_result(0)
            
        res.append(flag)
        
    print(*res)
