T = int(input())

for test_case in range(1, T + 1):
    if T%test_case == 0: # 입력받은 값을 나누었을 때 0으로 나누떨어지는 약수 출력
        print(test_case, end=' ')
