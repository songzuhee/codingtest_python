import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
true = [1, 2, 3, 4, 5, 6, 7, 8]

if arr == true:
    print('ascending')
elif arr[::-1] == true:
    print('descending')
else:
    print('mixed')