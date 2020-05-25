# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 4659 비밀번호 발음하기      | #
# ---------------------------- #


if __name__ == "__main__":
    while True:
        password = r_input().rstrip()

        if password == 'end':
            break

        flag1 = 0
        flag2 = 1
        flag3 = 1

        vowels = 0
        consonant = 0
        last = ''

        for ch in password:
            if ch == last:
                if last not in 'eo':
                    flag3 = 0
                    break
            
            if ch in 'aeiou':
                flag1 = 1
                vowels += 1
                consonant = 0

                if vowels == 3:
                    flag2 = 0
                    break
            
            else:
                consonant += 1
                vowels = 0
                
                if consonant == 3:
                    flag2 = 0
                    break
                    
            last = ch

        print('<' + password + '> is ', end='')

        if flag1 and flag2 and flag3:
            print('acceptable.')
        
        else:
            print('not acceptable.')
