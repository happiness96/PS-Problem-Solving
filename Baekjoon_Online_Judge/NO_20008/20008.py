# -*- encoding: utf-8 -*-
import sys
from collections import deque
from copy import deepcopy
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 10                             | #
# | 20008 몬스터를 처치하라!             | #
# -------------------------------------- #


def run():
    N, HP = map(int, r_input().split())
    
    queue = deque([[[0] * N, HP]])
    skills = []
    result = 0

    for _ in range(N):
        C, D = map(int, r_input().split())
        skills.append((C, D))
    
    visit = []

    while queue:
        for _ in range(len(queue)):
            cool_times, rem_HP = queue.popleft()

            if rem_HP <= 0:
                print(result)
                sys.exit()
            
            for ind, rem_time in enumerate(cool_times):
                if rem_time:
                    cool_times[ind] -= 1

            if 0 in cool_times:
                for ind, cool_time in enumerate(cool_times):
                    if cool_time == 0:
                        copied_cool_times = deepcopy(cool_times)
                        copied_cool_times[ind] = skills[ind][0]
                        
                        if [copied_cool_times, rem_HP - skills[ind][1]] not in visit:
                            queue.append([copied_cool_times, rem_HP - skills[ind][1]])
                            visit.append([copied_cool_times, rem_HP - skills[ind][1]])
                
            else:
                copied_cool_times = deepcopy(cool_times)
                queue.append([copied_cool_times, rem_HP])
        
        result += 1


if __name__ == "__main__":
    run()
