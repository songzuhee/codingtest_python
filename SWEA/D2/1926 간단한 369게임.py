import sys
input = sys.stdin.readline

n = int(input())
result = 0
answer = []

for i in range(1, n+1):
    # i를 문자열 처리
    clap = list(str(i))

    if clap.count('3') == 0 and clap.count('6') == 0 and clap.count('9') == 0:
        answer.append(i)
    else:
        result += clap.count('3')
        result += clap.count('6')
        result += clap.count('9')
        answer.append('-' * result)
        result = 0

print(*answer, end='')