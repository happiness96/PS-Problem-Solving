# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 22                             | #
# | 9763 마을의 친밀도                   | #
# -------------------------------------- #


def run():
    N = int(r_input())
    INF = sys.maxsize

    dist = [[(INF, -1), (INF, -1)] for _ in range(N)]
    locs = []

    res = sys.maxsize
    
    for ind1 in range(N):
        x, y, z = map(int, r_input().split())
        locs.append((x, y, z))

        for ind2 in range(ind1):
            m_x, m_y, m_z = locs[ind2]
        
            val = abs(x - m_x) + abs(y - m_y) + abs(z - m_z)

            if val <= dist[ind1][0][0]:
                dist[ind1][0], dist[ind1][1] = (val, ind2), dist[ind1][0]
            
            if val <= dist[ind2][0][0]:
                dist[ind2][0], dist[ind2][1] = (val, ind1), dist[ind2][0]

            tmp_val, tmp_node = dist[ind2][0]

            if tmp_node == ind1:
                tmp_val, tmp_node = dist[ind2][1]
            
            res = min(res, val + tmp_val)

            tmp_val, tmp_node = dist[ind1][0]

            if tmp_node == ind2:
                tmp_val, tmp_node = dist[ind1][1]
            
            res = min(res, val + tmp_val)

    print(res)


if __name__ == "__main__":
    run()
