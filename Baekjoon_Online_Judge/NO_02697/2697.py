# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 15                             | #
# | 2697 다음수 구하기                  | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        A = list(int(val) for val in r_input().rstrip())
        length = len(A)
        
        flag = 0
        chk = 0

        for ind in range(length - 1, 0, -1):
            if A[ind - 1] < A[ind]:
                chk = ind - 1
                flag = 1
                break

        if not flag:
            print('BIGGEST')
        
        else:
            save = A[chk + 1:]
            tmp = A[chk]
            tmp_number = 10

            for number in save:
                if tmp < number < tmp_number:
                    tmp_number = number
            
            save.pop(save.index(tmp_number))
            print(''.join(map(str, A[:chk] + [tmp_number] + sorted(save + [tmp]))))
