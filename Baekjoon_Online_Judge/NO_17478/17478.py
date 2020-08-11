# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 11                             | #
# | 17478 재귀함수가 뭔가요?            | #
# -------------------------------------- #


def dormammu(rem):
    print('____' * (N - rem) + '"재귀함수가 뭔가요?"')

    if rem == 0:
        print('____' * N + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    
    else:
        print('____' * (N - rem) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____' * (N - rem) + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____' * (N - rem) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        dormammu(rem - 1)

    print('____' * (N - rem) + '라고 답변하였지.')

if __name__ == "__main__":
    N = int(r_input())

    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

    dormammu(N)
