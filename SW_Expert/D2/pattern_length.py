# 2007. 패턴 마디의 길이
# 반복되는 단어(마디)의 길이를 출력
T = int(input())

for test_case in range(1, T + 1):
    string_input = list(input())

    count = 1;
    for i in range(1, 11): # 마디의 최대 길이는 10이다.
        # 중간에 첫 번째 인덱스 문자와 같은 문자가 있으므로 2번째 인덱스 문자까지 비교
        if string_input[0] != string_input[i] or string_input[1] != string_input[i+1]:
            count += 1
        elif string_input[0] == string_input[i]: # 위의 케이스에 해당이 되지 않고 같은 단어가 반복되면 반복문 중지
            break

    print('#{} {}'.format(test_case, count))

# 다른 풀이
T = int(input())

for tc in range(1, T+1):
    
    text = input()
    pattern =[]
    next_pattern=[]
    ans = 0
    for i in range(11):					# 마디의 최대 길이가 10이므로 range(11)
        pattern = text[:i]				# patten리스트에 패턴 입력
        next_pattern = text[i:i*2]		# 다음 패턴 입력
        if i!=0 and pattern == next_pattern :	# 다음 패턴과 이번 패턴이 같은경우 ex) i가 3인경우 0~2번째 문자와 3~5번째 문자가 같으면 한 문자로 취급
            ans = len(pattern)			# 길이 출력
            break
    print('#{} {}'.format(tc, ans))

# 다른 풀이2
T = int(input())
for test_case in range(1, T + 1):
    s=input()
    for j in range(1,10):
        if s[:j]==s[j:2*j]:
            print(f'#{test_case} {j}')
            break
