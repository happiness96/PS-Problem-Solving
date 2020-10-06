# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 06                             | #
# | 19948 음유시인 영재                 | #
# -------------------------------------- #


if __name__ == "__main__":
    content = r_input().rstrip()
    content_list = content.split()
    title = ''

    for word in content_list:
        title += word[0]
    
    title = title.upper()
    
    rem_space = int(r_input())
    rem_keyboard = list(map(int, r_input().split()))

    for ind, ch in enumerate(content):
        if ind != 0 and content[ind - 1] == ch:
            continue
        
        if 'A' <= ch <= 'Z':
            ch_ind = ord(ch) - ord('A')
            
            if not rem_keyboard[ch_ind]:
                print(-1)
                sys.exit()
            
            else:
                rem_keyboard[ch_ind] -= 1
        
        elif 'a' <= ch <= 'z':
            ch_ind = ord(ch) - ord('a')

            if not rem_keyboard[ch_ind]:
                print(-1)
                sys.exit()
            
            else:
                rem_keyboard[ch_ind] -= 1
        
        else:
            if not rem_space:
                print(-1)
                sys.exit()
            
            else:
                rem_space -= 1
    
    for ind, ch in enumerate(title):
        if ind != 0 and title[ind - 1] == ch:
            continue
        
        if 'A' <= ch <= 'Z':
            ch_ind = ord(ch) - ord('A')
            
            if not rem_keyboard[ch_ind]:
                print(-1)
                sys.exit()
            
            else:
                rem_keyboard[ch_ind] -= 1
        
        elif 'a' <= ch <= 'z':
            ch_ind = ord(ch) - ord('a')

            if not rem_keyboard[ch_ind]:
                print(-1)
                sys.exit()
            
            else:
                rem_keyboard[ch_ind] -= 1
        
        else:
            if not rem_space:
                print(-1)
                sys.exit()
            
            else:
                rem_space -= 1
    
    print(title)
