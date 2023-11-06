# 1213. [S/W 문제해결 기본] 3일차 - String
# 주어지는 문장 test에서 특정한 문자열 st의 개수를 반환하는 프로그램

for i in range(10):
    T = int(input())
    st = input()
    test = input()
    print('#{} {}'.format(T, test.count(st)))

# 다른 사람 풀이(count없이)
for i in range(10):
    index=int(input())
    find=input()
    str=input()
    result=0
    for i in range(len(str)):
        if str[i] == find[0]: # 특정 문자와 시작 문자가 같은 경우
            if str[i:i+len(find)] == find: # 특정 문자의 길이까지 문자열에서 추출해 비
                result+=1

    print("#%d %d" %(index,result))
