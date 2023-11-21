# 2577 숫자의 개수
# 제출한 코드
s_list = [int(input()) for _ in range(3)]
num = [0 for i in range(10)];
sum = s_list[0] * s_list[1] * s_list[2]
new_sum = list(map(int, str(sum))) # 정수를 리스트로 변환
# [int(new_sum) for new_sum in str(sum)]

for i in new_sum:
    num[i] += 1

for j in num:
    print(j)


# 다른 사람 풀이
a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c))

for i in range(10):
    print(result.count(str(i)))
