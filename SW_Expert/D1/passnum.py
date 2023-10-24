P, K = map(int, input().split())
count = 0

for test_case in range(K, P+1):
    count += 1
    if P == K:
        print(count)
    K += 1

# 다른 풀이
P, K = map(int, input().split())
print(P-K+1) # 주어진 숫자가 작다면 P-K에서 K번째 숫자를 입력하는 것을 포함하여 +1을 한 횟수
