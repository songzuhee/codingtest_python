# 바구니에는 1번 ~ N번까지의 번호
# 1 바구니 1공
#
# 도현이는 M번의 공을 넣을거임
#
# 조건
# - 바구니에 공이 이미 있는 경우에 들어있는 공 빼고 새로운 공 넣기
# - 공을 넣을 바구니는 연속되어 있어야 한다.
#
# 구해야 할 것
# - M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하삼

n, m = map(int, input().split())

# 바구니
basket = [0 for _ in range(n)]

for _ in range(1, m+1):
    i, j, k = map(int, input().split())
    for a in range(i-1, j):
        basket[a] = k
print(*basket)