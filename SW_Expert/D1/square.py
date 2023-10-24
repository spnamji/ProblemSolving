# 2019. 더블더블
T = int(input())
num = 1

for test_case in range(T+1):
    print(num, end=' ')
    num *= 2

# 다른 풀이
T = int(input())
for test_case in range(T+1):
    print(2**i, end=' ')
