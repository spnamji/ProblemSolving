# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
# zip 함수를 이용하여 전치행렬을 생성한다. (열번호가 같은 값끼리 엮음)
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    table = []
    answer = 0

    table = [list(map(int, input().split())) for i in range(N)]

    for i in zip(*table): # 세로열을 불러옴
        target = [j for j in i if j != 0] # 1과 2를 순서대로 저장한 target 리스트
        for j in range(len(target)-1): # 값을 저장한 target리스트의 길이만큼 반복
            if target[j:j+2] == [1,2]: # 순서 주의 (1, 2)일 때여야함
                answer += 1
    print("#"+str(test_case),answer)

# 내가 하려던 풀이(결국 돌아감)
T = 10

for test_case in range(1, T + 1):
    n = int(input())
    table = [list(map(int, input().split())) for i in range(n)]
    count = 0 # 교착 상태의 개수

    # 1. 1이 맨 밑에 있거나 2가 맨 위에 있는 경우 제거
    for i in range(100): # 세로 줄
        cur = []
        for j in range(100): # cur리스트에 1과 2가 있으면 추가한다.
            if table[j][i] == 1:
                cur.append(1)
            elif table[j][i] == 2:
                cur.append(2)

        for k in range(len(cur)-1):
            if (cur[k] == 1 and cur[k+1] == 2): # 1또는 2일때 2 또는 1일 때가 아니라 1, 2일때만을 고려해야한다.
                count += 1
    print(f"#{test_case} {count}")
