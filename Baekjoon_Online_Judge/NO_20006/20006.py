# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 10                             | #
# | 20006 랭킹전 대기열                 | #
# -------------------------------------- #


if __name__ == "__main__":
    p, m = map(int, r_input().split())

    rooms = []

    for _ in range(p):
        level, name = map(str, r_input().rstrip().split())
        level = int(level)
        
        if not rooms:
            rooms.append([(name, level)])
        
        else:
            flag = 0

            for ind, members in enumerate(rooms):
                if len(members) == m:
                    continue
                
                if abs(members[0][1] - level) <= 10:
                    rooms[ind].append((name, level))
                    flag = 1
                    break
            
            if not flag:
                rooms.append([(name, level)])
    
    for members in rooms:
        if len(members) == m:
            print('Started!')
        
        else:
            print('Waiting!')
        
        for name, level in sorted(members):
            print(level, name)
