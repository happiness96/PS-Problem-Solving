# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 20529 가장 가까운 세 사람의 심리적 거리| #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())
        mbti_cnt = {}

        for mbti in map(str, r_input().rstrip().split()):
            mbti_cnt[mbti] = mbti_cnt.get(mbti, 0) + 1
        
        mbti_list = []

        for mbti, cnt in mbti_cnt.items():
            mbti_list += [mbti] * min(3, cnt)
        
        length = len(mbti_list)
        result = sys.maxsize

        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    distance = 0

                    for ind in range(4):
                        if mbti_list[i][ind] != mbti_list[j][ind]:
                            distance += 1
                        
                        if mbti_list[j][ind] != mbti_list[k][ind]:
                            distance += 1

                        if mbti_list[k][ind] != mbti_list[i][ind]:
                            distance += 1
                    
                    result = min(result, distance)
        
        print(result)


if __name__ == "__main__":
    run()
