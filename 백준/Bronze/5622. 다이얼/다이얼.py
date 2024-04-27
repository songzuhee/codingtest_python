import sys
input = sys.stdin.readline

n = list(input())
arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for i in n:
    for j in arr:
        if i in str(j): 
            time = arr.index(j) + 3
            result += time
print(result)