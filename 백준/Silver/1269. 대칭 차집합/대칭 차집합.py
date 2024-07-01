import sys
input = sys.stdin.readline

a, b = map(int, input().split())

aArr = set(list(map(int, input().split())))
bArr = set(list(map(int, input().split())))

print(len(aArr-bArr)+len(bArr-aArr))