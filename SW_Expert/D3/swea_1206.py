# 1206. [S/W 문제해결 기본] 1일차 - View
# 거리 2이상에서 조망권이 확보되는 세대수를 구하라

# 제출한 코드
for test_case in range(1, 10 + 1):
    n = int(input())
    height = list(map(int, input().split()))
    result = 0

    for i in range(2, n-2): # 맨 앞과 끝에 2개씩은 건물이 없음
        if height[i] > height[i-1] and height[i] > height[i+1] and height[i] > height[i-2] and height[i] > height[i+2]: # 양 옆에 2개씩의 건물이 현재 건물보다 작은지
            a = max(height[i-1], height[i+1], height[i-2], height[i+2]) # 가장 높은 건물 높이
            result += height[i]-a # 세대수 누적

    print(f"#{test_case} {result}")

# 다른 사람 풀이
for test_case in range(1,11):
    result = 0
    houseCount = int(input())
    house = list(map(int , input().split()))
    for i in range(2, houseCount-2):
        arMax = max(house[i-1],house[i-2],house[i+1],house[i+2]) # 바로 가장 큰 값을 구함
        if house[i] > arMax: # 구한 가장 큰 값과 비교
            result += ( house[i] - arMax )

    print("#{} {}".format(test_case,result))
