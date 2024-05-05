import sys
input = sys.stdin.readline

coins = [500, 100, 50, 10, 5, 1]

n = int(input())
joi = 1000 - n
answer = 0

for i in coins:
    answer += joi // i
    joi %= i
print(answer)