# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 27                   | #
# | 1290 배럭                 | #
# ---------------------------- #


if __name__ == "__main__":
    N, B, U = map(int, r_input().split())

    INF = sys.maxsize

    # result = INF

    queue = deque([(N, B, 0)])
    round_no = 1

    save = [INF] * (B + 1)
    save[B] = N

    while queue:
        # print(queue)
        for _ in range(len(queue)):
            my, barrack, enemy = queue.popleft()

            flag = 0

            for attack_barrack in range(min(my, barrack) + 1):
                after_attack = barrack - attack_barrack
                after_enemy = enemy - (my - attack_barrack)
                # print(after_attack, after_enemy)

                if after_attack == 0 and after_enemy <= 0:
                    print(round_no)
                    sys.exit()

                if after_enemy < 0:
                    continue
                
                attacked_from_enemy = my - after_enemy
                # print(attacked_from_enemy)
                if attacked_from_enemy <= 0:
                    continue
                
                if after_attack:
                    after_enemy += U
                
                if after_enemy < attacked_from_enemy * 2 and attacked_from_enemy < save[after_attack]:
                    if queue and flag > 1:
                        queue.pop()
                    flag += 1
                    queue.append((attacked_from_enemy, after_attack, after_enemy))
                    save[after_attack] = attacked_from_enemy
                
        round_no += 1
    
    print(-1)
