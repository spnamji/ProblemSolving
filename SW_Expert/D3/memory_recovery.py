# 1289. 원재의 메모리 복구하기
# 0으로 초기화가 되었을 때 원래 값과 다르다면 해당 값부터 끝까지를 해당 비트로 바꾼다.
# ex) 100 : 원래값, 111 -> 100 (2회)
T = int(input())

for test_case in range(1, T + 1):
    bit = list(map(int, input()))
    reset = [0]*len(bit)
    count = 0

    for n in range(len(reset)):
        if bit[n] != reset[n]:
            reset[n:] = [bit[n]] * len(reset[n:]) # 리스트에 넣어주려는 값을 곱해서 여러번 넣는거라 []로 감싸야함
            count += 1

    print('#{} {}'.format(test_case, count))
