# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 21                   | #
# | 2777 숫자 놀이             | #
# ---------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())

        if N < 10:
            print(1)
            continue

        queue = deque([N])

        result = -1
        cnt = 1
        flag = 0
        
        visit = set()
        visit.add(N)
        
        while queue:
            for _ in range(len(queue)):
                num = queue.popleft()
                for div in range(1, 10):
                    if num % div == 0:
                        tmp = num // div

                        if tmp not in visit:
                            if num == div:
                                result = cnt
                                flag = 1
                                break

                            queue.append(tmp)
                            visit.add(tmp)
                
                if flag:
                    break
            
            if flag:
                break

            cnt += 1
        
        print(result)


if __name__ == "__main__":
    run()
