# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 14                             | #
# | 17269 이름궁합 테스트               | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())
    A, B = map(str, r_input().rstrip().split())

    cnt = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    save = []
    tmp = ''

    for ind in range(min(N, M)):
        tmp += A[ind] + B[ind]
    
    for ind in range(min(N, M), N):
        tmp += A[ind]
    
    for ind in range(min(N, M), M):
        tmp += B[ind]

    for alpha in tmp:
        save.append(cnt[ord(alpha) - 65])
    
    while len(save) > 2:
        new_save = []

        for i in range(len(save) - 1):
            new_save.append((save[i] + save[i + 1]) % 10)
        
        save = new_save
    
    print(str(save[0] * 10 + save[1]) + '%')
