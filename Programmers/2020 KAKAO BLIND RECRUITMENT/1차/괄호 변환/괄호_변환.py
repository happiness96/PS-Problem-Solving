# -*- encoding: utf-8 -*-
import sys

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 29                             | #
# | 괄호 변환                           | #
# -------------------------------------- #


def split_bracket(u, v):
    u_check = 0
    u_stack = []

    for sp in u:
        if sp == ')':
            if u_stack: u_stack.pop()
        
        else:
            u_stack.append(sp)
    
    if not u_stack:
        u_check = 1
    
    if u_check:
        v_length = len(v)

        if v_length == 0:
            return u
        
        for ind in range(2, v_length + 1, 2):
            r = v[: ind].count('(')
            l = v[: ind].count(')')

            if r == l:
                return u + split_bracket(v[:ind], v[ind:])
    
    else:
        v_length = len(v)

        u = u[1:-1]
        new_u = ''

        for br in u:
            new_u += ')' if br == '(' else '('

        for ind in range(2, v_length + 1, 2):
            r = v[: ind].count('(')
            l = v[: ind].count(')')

            if r == l:
                return '(' + split_bracket(v[:ind], v[ind:]) + ')' + new_u
        
        return '()' + new_u


def solution(p):
    return split_bracket('', p)
