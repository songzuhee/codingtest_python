import sys
input = sys.stdin.readline

i = 1
while True:
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break

    a = (l * (v//p)) + min((v%p), l)

    print('Case %d:' % i, a)
    i += 1