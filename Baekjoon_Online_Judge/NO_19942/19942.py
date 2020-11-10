# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 10                             | #
# | 19942 다이어트                       | #
# -------------------------------------- #


def run():
    N = int(r_input())

    min_c = sys.maxsize
    min_selected = []
    mp, mf, ms, mv = map(int, r_input().split())
    save = [(0, 0, 0, 0, 0, [])]

    for i in range(1, N + 1):
        p, f, s, v, c = map(int, r_input().split())
        
        new_save = []

        for sp, sf, ss, sv, sc, selected in save:
            sp += p
            sf += f
            ss += s
            sv += v
            sc += c

            if sc > min_c:
                continue

            if sp >= mp and sf >= mf and ss >= ms and sv >= mv:
                if sc < min_c:
                    min_c = sc
                    min_selected = selected + [i]
                
                elif sc == min_c:
                    min_selected = min(min_selected, selected + [i])
            
            else:
                new_save.append((sp, sf, ss, sv, sc, selected + [i]))
        
        save += new_save
    
    if min_c == sys.maxsize:
        print(-1)
    
    else:
        print(min_c)
        print(*min_selected)


if __name__ == "__main__":
    run()
