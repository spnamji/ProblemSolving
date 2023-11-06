# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱
# 재귀함수를 이용해서 푸는 문제
# 2 5라는 값이 주어지면 2*2*2*2*2 = 32 출력

# 재귀함수란? : 자기 자신을 다시 호출해 작업을 수행하는 방식
# 종료하는 조건이 필수적으로 필요.

def power_fun(n, m):
    if m == 0:
        return 1
    return n*power_fun(n, m-1)

for _ in range(10):
    T = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(T, power_fun(N, M)))
