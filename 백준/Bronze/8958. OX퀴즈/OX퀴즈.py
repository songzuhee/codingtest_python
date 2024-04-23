import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    s = list(input())
    a = 0
    result = 0
    for j in range(len(s)):
        if s[j] == 'O':
            a += 1
            result += a
        elif s[j] == 'X':
            a = 0
    print(result)