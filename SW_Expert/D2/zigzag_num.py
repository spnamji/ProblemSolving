# 1986. 지그재그 숫자
# 홀수는 더하고 짝수는 뺐을 때의 최종 누적 값
T = int(input())

for test_case in range(1, T+1):
    num = int(input())

    result = 0
    for i in range(1, num+1):
        if i%2 == 0: # 2로 나누었을 때의 몫이 0이면 짝
            result -= i
        else:
            result += i
    print('#{} {}'.format(test_case, result))
