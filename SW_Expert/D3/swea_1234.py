# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
# 같은 번호로 붙어있는 번호 쌍을 제거하는 과정 반복. 만약 더 이상 반복되지 않으면 종류 후 출력
for test_case in range(1, 11):
    n, m = input().split() # 입력 받음
    m = list(map(int, list(m))) # 리스트 형식으로 변환

    while True:
        status = False # 상태를 false로 기본값 지정
        for i in range(len(m)-1):
            if m[i] == m[i+1]: # 값이 같다면
                del m[i], m[i] # 두 값 모두 제거(제거하면 앞으로 인덱스가 땡겨져서
                status = True # stats를 true로 바꾸어 변경이 발생했다 표시
                break
        if status != True: # 변경이 발생하지 않았다면 더 이상 같은 번호가 없으므로 while문을 빠져나감
            break

    print(f"#{test_case} ", end='') # 출력
    for i in m:
        print(i, end='')
    print()

# 다른 사람 풀이
# 비밀번호
for tc in range(1, 11):
    N, arr = input().split()
    arr = list(arr)
    s = 0
    while s < len(arr): # 이전 값과 비교하여 없애고 없애면 하나 전 인덱스로 이동해 다시 확인
        if s and arr[s] == arr[s-1]:    # s가 0이 아닐 때 이전 값과 비교
            del arr[s], arr[s-1]    # 같을 땐 값을 지우고 이전 인덱스로 이동해 비교한다.
            s -= 1
        else:   # 다를 땐 다음 인덱스로 이동한다.
            s += 1
          
    print(f'#{tc} {"".join(arr)}') # join으로 리스트 값 한 번에 출력
