# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 03                             | #
# | 1326 폴짝폴짝                       | #
# -------------------------------------- #


def run():
    N = int(r_input())

    numbers = list(map(int, r_input().split()))
    a, b = map(int, r_input().split())
    a -= 1
    b -= 1

    save = [-1] * N

    if not 0 <= a < N or not 0 <= b < N:
        print(-1)
        sys.exit()

    if a == b:
        print(0)
        sys.exit()
    
    queue = deque([(a, 0)])
    save[a] = 0

    while queue:
        start_loc, cnt = queue.popleft()
        number = numbers[start_loc]

        tmp_loc = start_loc - number

        while tmp_loc >= 0:
            tmp = save[tmp_loc]

            if tmp < 0:
                save[tmp_loc] = cnt + 1
                queue.append((tmp_loc, cnt + 1))
            
            elif cnt + 1 < tmp:
                save[tmp_loc] = cnt + 1
                queue.append((tmp_loc, cnt + 1))
            
            tmp_loc -= number

        tmp_loc = start_loc + number

        while tmp_loc < N:
            tmp = save[tmp_loc]

            if tmp < 0:
                save[tmp_loc] = cnt + 1
                queue.append((tmp_loc, cnt + 1))
            
            elif cnt + 1 < tmp:
                save[tmp_loc] = cnt + 1
                queue.append((tmp_loc, cnt + 1))

            tmp_loc += number
        
    print(-(save[a] - save[b]))


if __name__ == "__main__":
    run()
