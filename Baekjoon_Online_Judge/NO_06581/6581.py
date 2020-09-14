# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 14                             | #
# | 6581 HTML                          | #
# -------------------------------------- #


if __name__ == "__main__":
    save = ''

    for line in sys.stdin:
        line = line.rstrip()

        word_list = line.split()

        for word in word_list:
            if word == '<br>':
                print(save)
                save = ''
            
            elif word == '<hr>':
                if save:
                    print(save)
                save = ''
                print('-' * 80)
            
            else:
                tmp_save = save

                if not tmp_save:
                    tmp_save = word
                
                else:
                    tmp_save += ' ' + word
                
                if len(tmp_save) > 80:
                    print(save)
                    save = word
                
                else:
                    save = tmp_save
    
    if save:
        print(save)
