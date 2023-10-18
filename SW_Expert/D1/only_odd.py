T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num_list = map(int, input().split())
    print('#',test_case," ",sum([i for i in num_list if i % 2 == 1]), sep="")

    # 깔끔한 print문 -> +로 이어줄 때 모두 str형이어야 한다.
    print("#"+str(test_case),str(sum([i for i in num_list if i % 2 == 1])))
