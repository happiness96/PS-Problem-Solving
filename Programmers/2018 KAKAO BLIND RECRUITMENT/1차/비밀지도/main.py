def solution(n, arr1, arr2):
    board = [[' '] * n for _ in range(n)]

    for row, number in enumerate(arr1):
        b_n = bin(number)[2:]
        b_n = '0' * (n - len(b_n)) + b_n

        for col, val in enumerate(b_n):
            if val == '1':
                board[row][col] = '#'
    
    for row, number in enumerate(arr2):
        b_n = bin(number)[2:]
        b_n = '0' * (n - len(b_n)) + b_n

        for col, val in enumerate(b_n):
            if val == '1':
                board[row][col] = '#'
        
    for ind, val in enumerate(board):
        board[ind] = ''.join(val)
        
    return board


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))