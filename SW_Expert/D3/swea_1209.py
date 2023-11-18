# 1209. [S/W 문제해결 기본] 2일차 - Sum
# 행의 합, 열의 합, 대각선의 합 중 가장 큰 값을 출력하는 문제
for test_case in range(1, 10 + 1):
    tc = int(input())
    num = [list(map(int, input().split())) for i in range(100)]
    row = 0
    max = 0

    for i in range(100):
        col = 0
        dia = 0
        row = sum(num[i])
        for j in range(100):
            col += num[j][i]
            dia += num[j][j]
        if col > max:
            max = col
        if dia > max:
            max = dia
        if row > max:
            max = row
    print(f"#{tc} {max}")

# 다른 사람 풀이
for _ in range(10):
    Count = int(input())
    List = [list(map(int,input().split())) for _ in range(100)]
    Max = 0
    for y in range(100):
        Answer1 = Answer2 = Answer3 = 0
        for x in range(100):
            Answer1 += List[y][x] # 가로 합
            Answer2 += List[x][y] # 세로 합
            Answer3 += List[x][x] # 대각선 합
        Max = max(Answer1,Answer2,Max)
    print("#{} {}".format(Count,Max))
