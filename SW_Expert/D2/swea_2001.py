# 2001. 파리 퇴치
# n*n크기의 배열안에 m*m만큼의 크기에서 존재하는 파리의 개수를 구하여라. (최대값)

# 내가 제출한 코드
T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    num = [list(map(int, input().split())) for i in range(n)]
    max = 0

    for i in range(n-(m-1)): # 모든 행과 열을 훑기 위한 반복문 2개
        for h in range(n-(m-1)):
            cur = 0
            for j in range(m): # m*m크기의 행렬안에서 파리의 개수
                for k in range(m):
                    cur += num[j+h][k+i]
            if cur > max: # 현재 값이 max보다 크다면 max값 변경
                max = cur

    print(f"#{test_case} {max}")

# 누적합도 있는데 나중에 공부해보자
