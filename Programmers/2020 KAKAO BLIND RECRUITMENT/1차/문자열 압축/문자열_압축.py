# -*- encoding: utf-8 -*-
import sys

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 29                             | #
# | 문자열 압축                         | #
# -------------------------------------- #


def solution(s):
    length = len(s)
    result = length

    for l in range(1, length // 2 + 1):
        stack = []

        save = []

        for ch in s:
            save.append(ch)

            if len(save) == l:
                sp = ''.join(save)

                if not stack:
                    stack.append((sp, 1))
                
                elif sp == stack[-1][0]:
                    _, cnt = stack.pop()

                    stack.append((sp, cnt + 1))
                
                else:
                    stack.append((sp, 1))
                
                save = []
        
        if save:
            stack.append((''.join(save), 1))
        
        tot = 0

        for string, cnt in stack:
            tot += len(string)

            if cnt != 1:
                tot += len(str(cnt))

        result = min(result, tot)
        
    return result
