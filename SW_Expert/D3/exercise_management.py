# 3431. 준환이의 운동관리
T = int(input())

for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    print('#{}'.format(test_case), end =' ')
    if X < L :
        print(abs(X-L))
    elif X > U:
        print(-1)
    elif X >= L and X <=U:
        print(0)

# 다른 사람 풀이
t = int(input())

for tc in range(1, t + 1) :
    l, u, x = map(int, input().split())
    result = 0 # 기본 값을 생성해서 if문 하나 줄임
    if x < l :
        result = l - x
    elif x > u :
        result = -1

    print('#%d %d' % (tc, result))
