import sys
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, a*b))