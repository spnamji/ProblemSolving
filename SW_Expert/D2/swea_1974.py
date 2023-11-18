# 1974. 스도쿠 검증
# 행, 렬, 3*3크기의 블럭에서 1~9사이의 값이어야 한다.

T = int(input())
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for test_case in range(1, T + 1):
    sdocu = [list(map(int, input().split())) for i in range(9)]
    current = [0 for i in range(9)]
    status = True

    # 행 검사
    for i in range(9):
        cur_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in sdocu[i]:
            if j in cur_num:
                cur_num.remove(j)
            else:
                status = False
                break

    # 열 검사
    for i in range(9):
        cur_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if sdocu[j][i] in cur_num:
                cur_num.remove(sdocu[j][i])
            else:
                status = False
                break

    # 3*3의 격자
    for i in range(9):
        cur_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(3):
            for k in range(3):
                if sdocu[j][k] in cur_num:
                    cur_num.remove(sdocu[j][k])
                else:
                    status = False
                    break

    if status == True:
        print(f"#{test_case} 1")
    elif status == False:
        print(f"#{test_case} 0")
