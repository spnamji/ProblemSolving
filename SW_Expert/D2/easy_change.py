T = int(input())

for test_case in range(1, T + 1):
    money_num = [0 for _ in range(8)]
    money = int(input())

    while money>=50000:
        money_num[0] = money//50000
        money %= 50000
    while money>=10000:
        money_num[1] = money//10000
        money %= 10000
    while money>=5000:
        money_num[2] = money//5000
        money %= 5000
    while money>=1000:
        money_num[3] = money//1000
        money %= 1000
    while money>=500:
        money_num[4] = money//500
        money %= 500
    while money>=100:
        money_num[5] = money//100
        money %= 100
    while money>=50:
        money_num[6] = money//50
        money %= 50
    while money>=10:
        money_num[7] = money//10
        money %= 10
    print('#{} \n{}'.format(test_case, ' '.join(map(str, money_num)))) # 문자열로 변환 후 join을 사용해 공백으로 구분된 문자열을 생성

    # 만약 출력하는 리스트가 문자의 요소를 가지는 경우 : *money_num 으로 한 번에 출력 가능


# 다른 사람 풀이
T = int(input())

for t in range(1, T+1) :
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 사용하는 돈의 단위를 리스트에 추가
    list = [0] * 8 # 개수를 넣을 리스트
    for i in range(8) :
        if N//money[i] != 0 :# 나누었을 때 몫이 0이 아니라
            list[i] = N//money[i] # 값을 정수로 나누었을 때의 몫을 리스트에 추가한다.
            N = N%money[i] # 나눈 나머지를 가지고 다시 반복
    print("#{}".format(t))
    print(*list) # 리스트 출력
