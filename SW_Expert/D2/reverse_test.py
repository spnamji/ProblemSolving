# 1989. 초심자의 회문 검사
T = int(input())

for test_case in range(1, T + 1):
    text = input()
    text_reverse = text[::-1]

    if text == text_reverse:
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))

# 다른 사람 풀이
t = int(input())

for tc in range(1, t + 1) :
    data = input()
    temp = '' # 거꾸로한 문자열을 삽입
    for i in range(len(data)-1, -1, -1) : # 맨 끝 인덱스부터 -1씩 -1번(끝까지)까지
        temp += data[i] # temp에 문자를 추가(문자열이라 가능)

    if data == temp : # 두 문자열이 같다면 1을 출력
        print('#%d %d' % (tc, 1))
    else :
        print('#%d %d' % (tc, 0))
