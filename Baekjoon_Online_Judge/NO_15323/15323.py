# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 23                   | #
# | 15323 ZigZag             | #
# ---------------------------- #


def run():
    K, N = map(int, r_input().split())

    words = {chr(asc): [] for asc in range(97, 123)}

    for _ in range(K):
        word = r_input().rstrip()
        words[word[0]].append(word)
    
    for st in words:
        words[st].sort()
        words[st] = deque(words[st])
    
    for _ in range(N):
        start = r_input().rstrip()

        print(words[start][0])
        words[start].append(words[start].popleft())


if __name__ == "__main__":
    run()
