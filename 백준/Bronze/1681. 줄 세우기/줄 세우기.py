import sys
input = sys.stdin.readline

n, l = map(int, input().split())
i = 1
cnt = 0
result = []

while True:
    if str(l) not in str(i):
        result.append(i)
        cnt += 1
        i += 1
        if cnt == n:
            print(result[n-1])
            break
    else:
        i += 1