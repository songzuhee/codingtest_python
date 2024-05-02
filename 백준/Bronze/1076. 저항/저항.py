import sys
input = sys.stdin.readline

data = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue',
        'violet', 'grey', 'white']

a = str(data.index(input().rstrip()))
b = str(data.index(input().rstrip()))
c = str(10 ** data.index(input().rstrip()))

print(int(a + b + c[1:]))