# 1984. 중간 평균값 구하기
# 10개의 값 중에서 최대, 최소값 빼고 평균갑을 구하는 문제. (소수점 1째 자리까지)
T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    num.sort()
    print('#{} {}'.format(test_case, round(sum(num[1:9])/8),1))

# 다른 사람 풀이
T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
  
    nums.sort()
    min_n = nums.pop(0) # 맨 처음 들어있는 값을 제거
    max_n = nums.pop()

    avg = sum(nums)/len(nums)
