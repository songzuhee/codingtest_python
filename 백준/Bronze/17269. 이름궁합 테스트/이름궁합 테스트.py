import sys
input = sys.stdin.readline

name = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

n, m = map(int, input().split())
a, b = input().split()

# 더 짧은 이름과 긴 이름찾기
short = min(n, m)
ab = []

for i in range(short):
    ab.append(a[i])
    ab.append(b[i])
ab += a[short:] + b[short:]
ab = list(map(lambda x : name[ord(x) - ord('A')], ab)) # 알파벳을 숫자로 변환
wordlenth = len(ab)

# 궁합 연산
for i in range(wordlenth - 2):
    for j in range(wordlenth - i - 1):
        ab[j] = (ab[j] + ab[j + 1]) % 10

print('{0}%'.format(ab[0] * 10 + ab[1]))