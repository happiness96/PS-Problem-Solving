# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 06                             | #
# | 5577 RBY팡!                          | #
# -------------------------------------- #


def run():
    N = int(r_input())

    origin = [int(r_input()) for _ in range(N)]

    result = N

    for change_ind in range(N):
        if change_ind:
            left = change_ind - 1
            save = origin[left]

            while left and save == origin[left - 1]:
                left -= 1
            
            right = change_ind + 1

            while right < N and save == origin[right]:
                right += 1
            
            if right - left >= 4:
                pang_list = origin[: left] + origin[right: ]

                while pang_list:
                    left = 0
                    right = 0
                    dup = 0
                
                    for ind, val in enumerate(pang_list):
                        if dup == val:
                            right = val + 1
                            continue

                        if ind - left >= 4:
                            right = ind
                            break
                        
                        left = ind
                        dup = val
                    
                    if right - left < 4:
                        break

                    pang_list = pang_list[: left] + pang_list[right:]

                result = min(result, len(pang_list))
        
        if change_ind < N - 1:
            right = change_ind + 1
            save = origin[right]

            while right < N and save == origin[right]:
                right += 1
            
            left = change_ind

            while left and save == origin[left - 1]:
                left -=1
            
            if right - left >= 4:
                pang_list = origin[: left] + origin[right: ]
                
                while pang_list:
                    left = 0
                    right = 0
                    dup = 0
                
                    for ind, val in enumerate(pang_list):
                        if dup == val:
                            right = val + 1
                            continue

                        if ind - left >= 4:
                            right = ind
                            break
                        
                        left = ind
                        dup = val
                    
                    if right - left < 4:
                        break

                    pang_list = pang_list[: left] + pang_list[right:]
                
                result = min(result, len(pang_list))
            
    print(result)


if __name__ == "__main__":
    run()
