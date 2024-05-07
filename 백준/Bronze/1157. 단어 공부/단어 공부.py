import sys
input = sys.stdin.readline

word = input().upper().rstrip()

# 중복없이 저장된 리스트
set_word = list(set(word))
cnt_list = []

for i in set_word:
    cnt_list.append(word.count(i))

if cnt_list.count(max(cnt_list)) >= 2:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(set_word[max_index])
