# 평균값 구하기 : 소수점 첫째 자리 반올림한 정수출력 
T = int(input())

for test_case in range(1, T + 1):
    result = 0
    num_list = list(map(int, input().split())) # 리스트의 형태로 값을 받아옴

    for i in num_list: # 리스트의 값을 하나씩 더함
        result += i
    print("#"+str(test_case),str(round(result/10))) # round로 반올림
