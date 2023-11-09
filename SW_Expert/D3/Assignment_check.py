# 5431. 민석이의 과제 체크하기
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))

    print('#{}'.format(test_case), end=' ')
    for i in range(1, N+1):
        if i not in num:
            print(i, end=' ')
    print()

# 다른 사람 코드
t = int(input())

for tc in range(1, t + 1) :
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    result = []

    for i in range(1, n + 1) :
        if i not in data :
            result.append(i) # 리스트에 없는 값을 추가

    print(f'#{tc}', *result) # 리스트로 출력
