N, M = map(int, input().split())

board = []

for i in range(N):
    row = list(input())
    board.append(row)

min_count = float('inf')

for s_row in range(N-7):
    for s_col in range(M-7):
        count_W = 0
        count_B = 0
        for i in range(s_row, s_row+8):
            for j in range(s_col, s_col+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        count_W += 1
                    if board[i][j] != 'B':
                        count_B += 1
                else:
                    if board[i][j] != 'W':
                        count_B += 1
                    if board[i][j] != 'B':
                        count_W += 1

        min_count = min(min_count, count_W, count_B)

print(min_count)