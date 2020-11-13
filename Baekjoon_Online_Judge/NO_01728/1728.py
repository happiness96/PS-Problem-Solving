# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 13                             | #
# | 1728 구슬 굴리기                    | #
# -------------------------------------- #


def find_result(node, next_node, result):
    if node == N:
        for l, v in result:
            print(l, v)
        
        sys.exit()
    
    for val, rem in location_list[0].items():
        if rem:
            gap = val - start_loc[node]
            save = [(0, val)]
            flag = 1

            for step in range(1, N):
                val += gap

                if val in location_list[step] and location_list[step][val]:
                    save.append((step, val))
                
                else:
                    flag = 0
                    break
            
            if flag:
                for step, rm_val in save:
                    location_list[step][rm_val] -= 1
                
                find_result(node + 1, next_node, result + [(start_loc[node], gap)])

                for step, rm_val in save:
                    location_list[step][rm_val] += 1


if __name__ == "__main__":
    N = int(r_input())

    location_list = []
    start_loc = sorted(map(int, r_input().split()))

    for _ in range(N):
        locations = {}

        for x_loc in map(int, r_input().split()):
            locations[x_loc] = locations.get(x_loc, 0) + 1
        
        location_list.append(locations)
    
    find_result(0, 0, [])
