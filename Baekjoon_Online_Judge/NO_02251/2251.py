# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 15                   | #
# | 2251 물통                 | #
# ---------------------------- #


if __name__ == "__main__":
    A, B, C = map(int, r_input().split())

    visit = set()
    result = set([C])

    queue = [(0, 0, C)]
    visit.add((0, 0, C))

    while queue:
        a, b, c = queue.pop()

        rem_A = A - a
        rem_B = B - b
        rem_C = C - c

        if a:
            if a >= rem_B:
                tmp = (a - rem_B, B, c)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)

                    if not tmp[0]:
                        result.add(c)
            
            else:
                tmp = (0, a + b, c)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)
                    result.add(c)
            
            if a >= rem_C:
                tmp = (a - rem_C, b, C)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)
            
            else:
                tmp = (0, b, a + c)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)
                    result.add(tmp[2])
        
        if b:
            if b >= rem_A:
                tmp = (A, b - rem_A, c)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)

            else:
                tmp = (a + b, 0, c)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)
            
            if b >= rem_C:
                tmp = (a, b - rem_C, C)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)
            
            else:
                tmp = (a, 0, b + c)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)
                    
                    if not a:
                        result.add(tmp[2])
        
        if c:
            if c >= rem_A:
                tmp = (A, b, c - rem_A)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)

            else:
                tmp = (a + c, b, 0)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)
            
            if c >= rem_B:
                tmp = (a, B, c - rem_B)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)
                
                    if not a:
                        result.add(tmp[2])
            
            else:
                tmp = (a, b + c, 0)

                if tmp not in visit:
                    visit.add(tmp)
                    queue.append(tmp)
                
                    if not a:
                        result.add(0)
    
    print(*sorted(result))
