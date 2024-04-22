import sys
input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    r, s = input().split()
    r = int(r)
    for j in range(len(s)):
        print(s[j] * r, end ='')
    print()