import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(1, t+1):
    L, U, X = map(int, input().split())

    if X > U:
        print('#{} {}'.format(test_case, -1))
    elif L < X < U:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, L - X))