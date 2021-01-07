# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 07                             | #
# | 10825 국영수                       | #
# -------------------------------------- #


def run():
    N = int(r_input())

    scores = {}

    for _ in range(N):
        name, lang, eng, math = map(str, r_input().split())

        lang = int(lang)
        eng = int(eng)
        math = int(math)

        if lang not in scores:
            scores[lang] = {}
        
        if eng not in scores[lang]:
            scores[lang][eng] = {}
        
        if math not in scores[lang][eng]:
            scores[lang][eng][math] = []
        
        scores[lang][eng][math].append(name)
    
    for l in sorted(scores, reverse=True):
        for e in sorted(scores[l]):
            for m in sorted(scores[l][e], reverse=True):
                for n in sorted(scores[l][e][m]):
                    print(n)


if __name__ == "__main__":
    run()
