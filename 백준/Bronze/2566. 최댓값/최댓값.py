import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_col, max_row = 0, 0

for i in range(9):
    for j in range(9):
        if max_num <=  arr[i][j]:
            max_num = arr[i][j]
            max_row = i + 1
            max_col = j + 1
print(max_num)
print(max_row, max_col)