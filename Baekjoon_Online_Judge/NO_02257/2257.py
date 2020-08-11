# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 11                             | #
# | 2257 화학식량                      | #
# -------------------------------------- #


if __name__ == "__main__":
    chemical_formula = r_input().rstrip()
    amount_of_atom = {'H': 1, 'C': 12, 'O': 16}

    stack = []
    acc = 0

    for ch in chemical_formula:
        if ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack[-1] != '(':
                acc += stack.pop()
            
            stack.pop()
            stack.append(acc)
            acc = 0
        
        elif ch in '23456789':
            stack.append(stack.pop() * int(ch))
        
        else:
            stack.append(amount_of_atom[ch])
    
    print(sum(stack))
