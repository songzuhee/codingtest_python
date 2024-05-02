import sys
input = sys.stdin.readline

n = int(input())
num = n

# 사이클
cycle = 0

while True:
    # 1의 자리 수
    a = num // 10

    # 10의 자리 수
    b = num % 10
    c = (a + b) % 10 # 더한 값의 1의 자리수
    num = (b * 10) + c

    cycle += 1
    if (num == n):
        break

print(cycle)