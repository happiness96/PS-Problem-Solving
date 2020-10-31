# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 31                             | #
# | 2784 가로 세로 퍼즐                | #
# -------------------------------------- #


def run():
    words = [r_input().rstrip() for _ in range(6)]

    result = []

    for ind1, word1 in enumerate(words):
        for ind2, word2 in enumerate(words):
            if ind1 != ind2:
                for ind3, word3 in enumerate(words):
                    if ind1 != ind3 and ind2 != ind3:
                        save = [word1, word2, word3]

                        chk = list(range(6))
                        chk.remove(ind1)
                        chk.remove(ind2)
                        chk.remove(ind3)

                        for col in range(3):
                            string = ''

                            for row in range(3):
                                string += save[row][col]
                            
                            for k in chk:
                                if string == words[k]:
                                    chk.remove(k)
                                    break
                        
                        if not chk:
                            result.append(word1 + word2 + word3)
    
    result.sort()
    
    if not result:
        print(0)
        sys.exit()

    for res in range(0, 9, 3):
        print(result[0][res: res + 3])


if __name__ == "__main__":
    run()
