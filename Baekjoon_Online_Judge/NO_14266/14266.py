# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 03                             | #
# | 14266 나는 가르친다 스위핑을         | #
# -------------------------------------- #


def run():
    n = int(r_input())

    start = []
    end = []

    for _ in range(n):
        x1, y1, x2, y2 = map(int, r_input().split())

        inc1 = y1 / x1
        inc2 = y2 / x2

        if inc1 >= inc2:
            start.append(inc1)
            end.append(inc2)
        
        else:
            start.append(inc2)
            end.append(inc1)
        
    start.sort()
    end.sort()

    cnt = 0
    result = 0

    save = sys.maxsize
    cur = 0

    while start:
        cur = start.pop()
        cnt += 1

        while start and start[-1] == cur:
            start.pop()
            cnt += 1
        
        while end and cur < end[-1] <= save:
            end.pop()
            cnt -= 1
        
        result = max(result, cnt)

        save = cur
    
    print(result)


if __name__ == "__main__":
    run()
