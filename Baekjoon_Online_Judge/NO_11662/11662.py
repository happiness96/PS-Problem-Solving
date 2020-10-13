# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 11                             | #
# | 11662 민호와 강호                   | #
# -------------------------------------- #


def run():
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, r_input().split())

    result = sys.maxsize
    negative_flag = 0

    start_distance = ((Cx - Ax) ** 2 + (Cy - Ay) ** 2) ** 0.5
    dest_distance = ((Dx - Bx) ** 2 + (Dy - By) ** 2) ** 0.5

    result = min(start_distance, dest_distance)

    while True:
        minho_midx = (Ax + Bx) / 2
        minho_midy = (Ay + By) / 2
        gangho_midx = (Cx + Dx) / 2
        gangho_midy = (Cy + Dy) / 2

        mid_dist = ((gangho_midx - minho_midx) ** 2 + (gangho_midy - minho_midy) ** 2) ** 0.5
        
        if start_distance > dest_distance:
            Ax = minho_midx
            Ay = minho_midy
            Cx = gangho_midx
            Cy = gangho_midy
            
            start_distance = mid_dist
        
        else:
            Bx = minho_midx
            By = minho_midy
            Dx = gangho_midx
            Dy = gangho_midy
            
            dest_distance = mid_dist
        
        if abs(dest_distance - start_distance) < 0.0000001:
            print(mid_dist)
            break


if __name__ == "__main__":
    run()
