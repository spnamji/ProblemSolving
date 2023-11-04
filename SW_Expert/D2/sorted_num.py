# 1966. 숫자를 정렬하자
# 주어진 length의 길이의 문자를 오름차순으로 정렬.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    num = sorted(list(map(int, input().split())))
    
    print('#{}'.format(test_case), end=' ')
    for i in num:
        print(i, end=' ')
    print()
