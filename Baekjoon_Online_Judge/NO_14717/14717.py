# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 24                             | #
# | 14717 앉았다                        | #
# -------------------------------------- #


if __name__ == "__main__":
    A, B = map(int, r_input().split())

    tot = 18 * 17
    
    if A == B:
        print('%.3f' % ((tot - 2 * (10 - A)) / tot))
    
    else:
        cnt = 0
        my_rem = (A + B) % 10

        cards = []
        
        for number in range(1, 11):
            if number != A:
                cards.append(number)
            
            if number != B:
                cards.append(number)
        
        for ind1, card1 in enumerate(cards):
            for ind2, card2 in enumerate(cards):
                if card1 == card2:
                    continue
                
                if ind1 != ind2:
                    rem = (card1 + card2) % 10

                    if rem < my_rem:
                        cnt += 1

        print('%.3f' % (cnt / tot))
