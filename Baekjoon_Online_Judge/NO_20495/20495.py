# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 20495 수열과 헌팅                   | #
# -------------------------------------- #


def run():
    N = int(r_input())

    left = []
    right = []
    save = []

    for _ in range(N):
        a, b = map(int, r_input().split())
        l, r = a - b, a + b

        left.append(l)
        right.append(r)
        save.append((l, r))

    left.sort()
    right.sort()

    for l, r in save:
        start, end = 0, N - 1

        while True:
            if end - start <= 1:
                if right[start] >= l:
                    print(start + 1, end=' ')
                
                else:
                    print(end + 1, end=' ')
                
                break

            mid = (start + end) // 2

            if l <= right[mid]:
                end = mid
            
            else:
                start = mid

        start, end = 0, N - 1
        
        while True:
            if end - start <= 1:
                if r >= left[end]:
                    print(end + 1)
                
                else:
                    print(start + 1)
                
                break

            mid = (start + end) // 2

            if r >= left[mid]:
                start = mid
            
            else:
                end = mid


if __name__ == "__main__":
    run()
