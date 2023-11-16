# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다. 
# 주어진 횟수만큼 평탄화를 진행했을 때 최고점과 최저점의 차는?
# 포인트 : 평탄화를 모두 마치고나서 차이를 구한다.

# 제출한 코드
for test_case in range(1, 11):
    N = int(input()) # 평탄화 횟수
    h = list(map(int, input().split())) # 길이 100 고정

    for _ in range(N): # 평탄화 횟수 만큼 반복한다.
        h[h.index(max(h))] -= 1 # 배열 h에서 가장 큰 값의 인덱스의 값을 하나 뺀다
        h[h.index(min(h))] += 1 # 가장 작은 값의 인덱스의 값을 하나 더한다
    print(f"#{test_case}", max(h)-min(h)) # 평탄화 종료 후 차이를 출력한다. 
