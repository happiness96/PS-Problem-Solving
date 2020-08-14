# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 14                             | #
# | 1268 임시 반장 정하기              | #
# -------------------------------------- #


def run():
    N = int(r_input())

    classes = [list(map(int, r_input().split())) for _ in range(N)]
    res = 0
    max_friends = 0

    for stu_num, s_class in enumerate(classes):
        total = set()

        for ind in range(N):
            if stu_num != ind:
                for grade in range(5):
                    if classes[ind][grade] == s_class[grade]:
                        total.add(ind)
        
        cnt = len(total)
        
        if max_friends < cnt:
            max_friends = cnt
            res = stu_num
    
    print(res + 1)


if __name__ == "__main__":
    run()
