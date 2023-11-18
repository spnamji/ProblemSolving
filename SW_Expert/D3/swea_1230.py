# 1228. [S/W 문제해결 기본] 8일차 - 암호문1
# 첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)
# 두 번째 줄 : 원본 암호문
# 세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)
# 네 번째 줄 : 명령어
# I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.
# 다음과 같은 문제일 때 최종 암호문을 앞에서 10개 출력한다.

# 제출한 코드
T = 10

for test_case in range(1, T + 1):
    n = int(input())
    cryptogram = list(input().split())
    command_n = int(input())
    command = list(input().split())
    x = 0
    y = 0

    for i in range(command_n):
        if command[0] == 'I':
            x = int(command[1])
            y = int(command[2])
            del command[0], command[0], command[0]

        for j in range(y):
            cryptogram.insert(x+j, command[0])
            del command[0]

    print(f"#{test_case} {' '.join(cryptogram[:10])}")

# 다른 사람 풀이
for tc in range(1,11):
    N = int(input()) # 원본 암호문 길이
    o_set = list(map(str,input().split())) # 원본 암호문
    T = int(input()) #  명령어의 개수
    T_set = list(map(str,input().split())) # 명령어 문자열
  
    for i in range(len(T_set)):
        if(T_set[i] == 'I'):
            x = int(T_set[i+1]) # x의 위치부터
            y = int(T_set[i+2]) # y 개 
            for a in range(y): # y개 개수만큼 인덱스 값에 추가
                o_set.insert(x+a,T_set[i+3+a])

    print(f'#{tc}',' '.join(o_set[:10]))
