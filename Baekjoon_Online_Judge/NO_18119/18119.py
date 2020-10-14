# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 13                             | #
# | 18119 단어 암기                     | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    known_word = []
    unknown_word = []
    fixed_cnt = 0

    only_vowel = ['0'] * 26

    for ch in 'aeiou':
        only_vowel[ord(ch) - 97] = '1'
    
    only_vowel = int(''.join(only_vowel), 2)
    
    for _ in range(N):
        bits = ['0'] * 26
        word = set(r_input().rstrip())

        for ch in word:
            bits[ord(ch) - 97] = '1'
        
        bits = int(''.join(bits), 2)

        if only_vowel & bits == bits:
            fixed_cnt += 1
        
        else:
            known_word.append(bits)
    
    check_bit = ['1'] * 26
    
    for _ in range(M):
        o, x = map(str, r_input().rstrip().split())

        if o == '1':
            check_bit[ord(x) - 97] = '0'
            check = int(''.join(check_bit), 2)

            new_known_word = []

            for ch in known_word:
                if check & ch != ch:
                    unknown_word.append(ch)
                
                else:
                    new_known_word.append(ch)
            
            known_word = new_known_word
        
        else:
            check_bit[ord(x) - 97] = '1'
            check = int(''.join(check_bit), 2)

            new_unknown_word = []

            for ch in unknown_word:
                if check & ch == ch:
                    known_word.append(ch)
                
                else:
                    new_unknown_word.append(ch)
            
            unknown_word = new_unknown_word
        
        print(fixed_cnt + len(known_word))


if __name__ == "__main__":
    run()
