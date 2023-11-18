# 1961. 숫자 배열 회전
# n*n행렬을 90도, 180도, 270도 회전한 모양을 출력하는 문제
# 1열에 90도 회전한 값, 2열에 180도 회전한 값, 3열에 270도 회전한 값이 출력된다
# 741 987 369
# 852 654 258
# 963 321 147

# 제출한 코드
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    num = [list(input().split()) for i in range(n)]
    num_cur = [['0']*n for i in range(n)]
    new_lsit = [['']*n for i in range(n)]

    for i in range(n): # 90도 회전
        for j in range(n):
            num_cur[i][j] = num[n-1-j][i]
            new_lsit[i][0] += num_cur[i][j]

    for i in range(n): # 180도 회전
        for j in range(n):
            num[i][j] = num_cur[n-1-j][i]
            new_lsit[i][1] += num[i][j]

    for i in range(n): # 270도 회전
        for j in range(n):
            num_cur[i][j] = num[n-1-j][i]
            new_lsit[i][2] += num_cur[i][j]

    print(f"#{test_case}")
    for i in range(n):
        print(' '.join(new_lsit[i]))

# 다른 사람 풀이
# 함수를 적용하여 반복되는 문장을 줄인다음 zip을 이용하여 전치행렬 형태로 출력
def rotation(a, N):
    new_arr = [[0] * N for _ in range(N)]  # NxN 빈 배열 만들기
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = a[N-1-j][i]
    return new_arr

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(input().split() for _ in range(n))

    arr90 = rotation(arr, n)
    arr180 = rotation(arr90, n)
    arr270 = rotation(arr180, n)

    print(f"#{test_case}")
    for i, j, k in zip(arr90, arr180, arr270):
        print(f"{''.join(i)} {''.join(j)} {''.join(k)}")
