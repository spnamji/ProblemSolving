# 2005. 파스칼의 삼각형
# 왼쪽위의 값과 오른쪽 위의 값을 더한 값을 아래에 배치
T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    print('#{}'.format(test_case))
    pre_list = [[0]*num for i in range(num)] # num길이의 0리스트를 num개 만든다
    pre_list[0][0] = 1 # 맨 처음 줄의 값은 1 하나

    for i in range(num):
        for j in range(i+1):
            if j == 0: # 맨 앞의 값은 1을 넣는다
                pre_list[i][j] = 1
            else :
                pre_list[i][j] = pre_list[i-1][j-1] + pre_list[i-1][j] # 나보다 윗 줄의 값에서 내 앞의 인덱스 값 + 나보다 윗 줄의 값에서 나랑 같은 인덱스의 

    print('#{}'.format(test_case))
    for k in range(num):
        for l in range(num): 
            if pre_list[k][l]: # 값이 존재하면 출력
                print(pre_list[k][l], end=' ')
        print()

