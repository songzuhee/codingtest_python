import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    print('#{} {}'.format(test_case, n // 3))