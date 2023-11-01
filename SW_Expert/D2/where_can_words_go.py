# 1979. 어디에 단어가 들어갈 수 있을까
# 행과 열 모두 고려하여 k개의 단어가 들어갈 수 있는 공간의 개수를 찾아야한다.
# 행과 열을 따로 검사하여 개수를 더한다.
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    list_n = [list(map(int, input().split())) for _ in range(N)]

    # 행 검사
    for i in range(N):
        count = 0
        for j in list_n[i]:
            # if count > K: # 해당 부분이 있으면 N값이 큰 행렬에서 break가 걸려 for문을 빠져나가게 된다.
            #     count = 0
            #     break
            if j == 1: # 1인 값의 개수를 측정
                count += 1
            elif j == 0: # 행렬에서 중간에 0이 있을 경우
                if count == K: # 1의 개수가 문자의 길이인 k와 같다면
                    result += 1 # 들어갈 수 있는 자리 개수에 +1을 하고
                    count = 0 # count를 초기화
                else: # 같지 않다면 그냥 초기화
                    count=0
        if count == K: # 한 행을 마지막까지 반복 후 1의 개수가 k와 같다면 자리 개수 +1
            result += 1

    # 열 검사 (행과 동일)
    for i in range(N):
        count = 0
        for j in range(N):
            k = list_n[j][i] # 열을 고정시키고 행을 바꾼다.
            if k == 1:
                count += 1
            elif k == 0:
                if count == K:
                    result += 1
                    count = 0
                else:
                    count=0
        if count == K:
            result += 1

    print('#{} {}'.format(test_case, result))

# 다른 사람 풀이
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    list_n = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N): # 해당 반복안에 행, 열 검사 모두 넣음
        count = 0
        # 행 검사
        for j in range(N):
          if puzzle[i][j] == 1:
            count += 1
          if puzzle[i][j] == 0 or j == n-1: # 해당 인덱스의 값이 행에서 0이거나 마지막 요소일 경우
            if count == k: # 1의 개수가 k와 같으면
              result += 1
            count = 0

        # 열 검사 (행과 동일)
        for j in range(N):
          if puzzle[j][i] == 1:
            count += 1
          if puzzle[j][i] == 0 or j == n-1: # 해당 인덱스의 값이 행에서 0이거나 마지막 요소일 경우
            if count == k: # 1의 개수가 k와 같으면
              result += 1
            count = 0
print('#{} {}'.format(test_case, result))
