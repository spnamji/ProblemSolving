# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
# 1~5까지 맨 앞의 숫자를 감소 후 맨 뒤로 보낸다. 숫자가 감소할 때 0보다 작아지거나 0인 경우 맨 뒤로 보내고 종료
for t in range(10):
    T = int(input())
    data = list(map(int, input().split()))
    state = True

    while True: # 무한 반복 
        for i in range(1, 6):
            cur = data.pop(0)
            if cur-i <= 0: # 뺀 값이 0보다 작거나 같으면
                data.append(0) # 무조건 0을 맨 뒤로 보내고
                state = False # state를 false로 바꾼다.
                break
            else:
                data.append(cur - i)
        if state == False: # state가 false면 바깥 while문까지 종
            break
    print('#{}'.format(T), end=' ')
    print(*data)

# 다른 사람 코드
for tc in range(10):
    T = int(input())
    arr = list(map(int, input().split()))
    while arr[-1] != 0: # 리스트의 마지막 인덱스 값이 0이 아닐 때까지 반복
        for i in range(1, 6):
            arr.append(arr.pop(0) - i)
            if arr[-1] <= 0:
                arr[-1] = 0
                break
    print('#{0}'.format(T), *arr)
