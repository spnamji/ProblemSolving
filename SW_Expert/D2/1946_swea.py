# 1946. 간단한 압축 풀기
# A 10 B 7 C 5 다음과 같이 주어진 만큼 반복하여 출력하는데 너비는 10이고 마지막 줄은 왼쪽부터 채워져 있다(안 건너뜀)
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cnt = 0

    print(f"#{test_case}")
    for i in range(N): # 알파벳 순서쌍의 개수
        a, b = input().split()
        b = int(b)

        for j in range(b): # 해당 알파벳의 숫자만큼 반복
            if cnt == 9: # 해당 줄의 길이가 10이라면
                print(a) # 출력 후 다음줄로
                cnt = 0
            else:
                print(a, end='') # 아니라면 붙여서 출력함
                cnt += 1 # 너비의 길이를 재는 cnt
    print()
