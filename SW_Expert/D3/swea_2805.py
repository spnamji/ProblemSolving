# 2805. 농작물 수확하기
# n*n크기의 농장이고 크기는 항상 홀수이다. 수확은 정사각형 마름모 형태로만 가능하다. 이때 얻는 수익은?
T = int(input())

# 시작 지점과 끝 지점을 지정하여 푸는 문제
for test_case in range(1, T + 1):
    n = int(input())
    sum = 0
    s, e = n//2, n//2 # 정사각 마름모형태이므로 맨 처음에는 정 가운데에서 시작

    for i in range(n):
        area = list(input()) # 문자열을 그냥 입력받아 list로 변환시 요소 하나하나 저장됨

        for j in range(s, e+1): # 시작 지점부터 끝 지점까지 값을 더한다.
            sum += int(area[j])

        if i < n//2: # 가운데 줄 기준으로 윗 부분이면 시작 지점은 줄어들고 끝지점은 커진다
            s -= 1
            e += 1
        else: # 아랫 부분인 경우 시작 지점은 다시 커지고 끝 지점은 작아진다.
            s += 1
            e -= 1

    print(f"#{test_case} {sum}")

# 다른 사람 풀이
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)] # n줄만큼 입력을 받는다.(하나씩 입력받아 리스트로 변경)
    ans = 0  # output 변수

    # s: 시작포인트, e: 끝포인트
    s, e = N // 2, N // 2
    for i in range(N):
        for j in range(s, e+1):
            ans += a[i][j]
        # 행의 인덱스가 mid 전까지는 s-e 간격 늘리고 mid 이후로는 간격 줄임
        if i < N // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print("#{} {}".format(tc, ans))
