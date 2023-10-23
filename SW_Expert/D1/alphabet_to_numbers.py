number =input()

for i in number: # 문자열의 값이 하니씩 들어감
    print(ord(i)-64, end=' ') # ord() : 하나의 문자를 유니코드 정수로 반환
                              # 대문자 'A'가 정수로 65임.
