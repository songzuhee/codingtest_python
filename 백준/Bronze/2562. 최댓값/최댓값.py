import sys
input = sys.stdin.readline

arr = []

for i in range(9):
    n = int(input())
    arr.append(n)

print(max(arr), arr.index(max(arr))+1)