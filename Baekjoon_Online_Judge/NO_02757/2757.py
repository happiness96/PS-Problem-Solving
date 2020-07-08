# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 08                   | #
# | 2757 엑셀                 | #
# ---------------------------- #


if __name__ == "__main__":
    save = [1]

    for exp in range(1, 6):
        save.append(26 ** exp + save[-1])
    
    while True:
        n, m = map(str, r_input().rstrip().split('C'))
        n = n[1:]

        if n == m == '0':
            break
        
        m = int(m)
        flag = 0
        res = []

        for exp in range(5, -1, -1):
            if not flag:
                if m < save[exp]:
                    continue
            
            flag = 1
            tmp = 26 ** exp
            div = m // tmp
            
            res.append(div)

            m -= tmp * div
        
        for ind in range(len(res) - 1, 0, -1):
            if res[ind] <= 0:
                res[ind - 1] -= 1
                res[ind] += 26
        
        for val in res:
            print(chr(val + 64), end='')
        
        print(n)
