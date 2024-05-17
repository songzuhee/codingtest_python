import sys
input = sys.stdin.readline

t = int(input())
result = 0

for test_case in range(1, t+1):
    line = str(input().rstrip())

    # 역순으로 뒤집었을 때 일치하면 1 아니면 0
    r_line = line[::-1]

    if line == str(r_line):
        result = 1
    else:
        result = 0

    print('#{} {}'.format(test_case, result))

