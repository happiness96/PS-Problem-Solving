# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 17                             | #
# | 4347 Tic Tac Toe                   | #
# -------------------------------------- #


def run():
    N = int(r_input())

    for a in range(N):
        board = [list(r_input().rstrip()) for _ in range(3)]

        x_count = 0
        o_count = 0

        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    x_count += 1
                
                elif board[row][col] == 'O':
                    o_count += 1
        
        if x_count - o_count not in (0, 1):
            print('no')
        
        else:
            correct_x = []
            correct_o = []

            for row in range(3):
                if ''.join(board[row]) =='XXX':
                    correct_x.append(row + 1)
                
                elif ''.join(board[row]) == 'OOO':
                    correct_o.append(row + 1)
            
            for col in range(3):
                save = ''

                for row in range(3):
                    save += board[row][col]
                
                if save == 'XXX':
                    correct_x.append(row + 4)
                
                elif save == 'OOO':
                    correct_o.append(row + 4)
            
            save = ''
            for dia in range(3):
                save += board[dia][dia]
            
            if save == 'XXX':
                correct_x.append(7)
            
            elif save == 'OOO':
                correct_o.append(7)
            
            save = ''
            for dia in range(3):
                save += board[dia][2 - dia]
            
            if save == 'XXX':
                correct_x.append(8)
            
            elif save == 'OOO':
                correct_o.append(8)
            
            len_x = len(correct_x)
            len_o = len(correct_o)

            if len_x and len_o:
                print('no')
            
            elif len_x and x_count == o_count or len_o and x_count > o_count:
                print('no')

            else:
                flag_x = 0
                flag_o = 0

                for check in range(1, 4):
                    if check in correct_x:
                        flag_x += 1
                    
                    if check in correct_o:
                        flag_o += 1

                if flag_x > 1 or flag_o > 1:
                    print('no')
                
                else:
                    flag_x = 0
                    flag_o = 0

                    for check in range(4, 7):
                        if check in correct_x:
                            flag_x += 1
                        
                        if check in correct_o:
                            flag_o += 1
                    
                    if flag_x > 1 or flag_o > 1:
                        print('no')
                    
                    else:
                        print('yes')
        
        r_input()


if __name__ == "__main__":
    run()
