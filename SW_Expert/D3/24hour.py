# 12368. 24시간
# 현재시간 a에서 b만큼 흘렀을 때 24시간제 시계에서의 현재 시간
T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    if A+B < 24:
        print('#{} {}'.format(test_case, A+B))
    elif A+B >= 24:
        print('#{} {}'.format(test_case, abs(24-A-B)))

# 다른 사람 풀이
t = int(input())

for tc in range(1, t + 1) :
    a, b = map(int, input().split())
    hour = a + b

    print('#%d %d' % (tc, hour % 24)) # (23 + 23) % 24로 나머지를 출력
