# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 24                             | #
# | 1796 신기한 키보드                  | #
# -------------------------------------- #


if __name__ == "__main__":
    S = r_input().rstrip()

    alpha_locs = {alpha: [] for alpha in 'abcdefghijklmnopqrstuvwxyz'}
    
    for ind, ch in enumerate(S):
        alpha_locs[ch].append(ind)
    
    
    queue = [(0, 0)]

    for alpha, val in alpha_locs.items():
        if val:
            new_queue = []
            len_val = len(val)

            if len_val == 1:
                for loc, cost in queue:
                    new_queue.append((val[0], cost + abs(val[0] - loc) + 1))

            else:
                min_val = min(val)
                max_val = max(val)

                for loc, cost in queue:
                    if loc >= max_val:
                        new_queue.append((min_val, cost + loc - min_val + len_val))
                    
                    elif loc <= min_val:
                        new_queue.append((max_val, cost + max_val - loc + len_val))
                    
                    else:
                        new_queue.append((min_val, cost + max_val - loc + max_val - min_val + len_val))
                        new_queue.append((max_val, cost + loc - min_val + max_val - min_val + len_val))

            queue = new_queue
    
    print(min(x[1] for x in queue))
