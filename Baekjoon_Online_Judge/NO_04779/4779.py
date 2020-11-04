# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 05                             | #
# | 4779 칸토어 집합                    | #
# -------------------------------------- #


def run():
    for val in sys.stdin:
        val = int(val)

        queue = [(0, 3 ** val)]
        res = [' ' for _ in range(3 ** val)]
        
        while True:
            if queue[0][1] - queue[0][0] == 1:
                break

            new_queue = []
            val -= 1
            gap = 3 ** val

            for start, end in queue:
                tot = start + end
                mid1 = start + gap
                mid2 = end - gap

                new_queue.append((start, mid1))
                new_queue.append((mid2, end))
            
            queue = new_queue
        
        for start, end in queue:
            res[start] = '-'
        
        print(''.join(res))


if __name__ == "__main__":
    run()
