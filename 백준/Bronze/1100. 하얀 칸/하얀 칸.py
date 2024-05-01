import sys
input = sys.stdin.readline

chess = []
result = 0

for _ in range(8):
    chess.append(input())
# print(chess)
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and chess[i][j] == 'F':
            result += 1
        if i % 2 == 1 and j % 2 == 1 and chess[i][j] == 'F':
            result += 1
print(result)