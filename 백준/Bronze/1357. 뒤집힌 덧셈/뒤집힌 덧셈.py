import sys
input = sys.stdin.readline

def Rev(n):
    reversed_n = str(n)[::-1]
    return int(reversed_n)

x, y = map(int, input().split())

print(Rev(Rev(x)+Rev(y)))