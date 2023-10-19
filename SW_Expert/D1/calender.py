# 2056. 연월일 달력
T = int(input())
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 월에 따른 마지막 날짜를 리스트로 생성
for test_case in range(1, T + 1):
    date = str(input()) # 문자로 값을 받음

    month = int(date[4:6]) # 슬리이싱 후 정수형 변환 (정수형은 슬리이싱x)
    day = int(date[6:])
    if month >= 1 and month <= 12: # 조건 확인
        if day >= 1 and day <= day_list[month - 1]:
            # 문자 0101을 정수로 변환시 010이 된다.
            print("#" + str(test_case), str(date[0:4]) + "/" + str(date[4:6]) + "/" + str(date[6:]))
        else:
            print("#" + str(test_case), str(-1))
    else:
        print("#" + str(test_case), str(-1))


# 좀 더 효율적인 코드 (딕셔너리)
n = int(input())
days= {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #딕셔너리를 사용

for i in range(1,n+1):
  x = str(input())
  
  year = x[0:4]
  month = x[4:6]
  day = x[6:]
  fail = -1

  # 1~12달 사이에 맞는지 확인하고 딕셔너리를 사용해 일이 딕셔너리에 들어있는 일보다 작거나 같은지 확인 둘다 같으면 유효하므로 출력
  if 0 < int(month) < 13 and int(day) <= days[int(month)]: 
    print("#{} {}/{}/{}".format(i,year,month,day))
  else:
    print('#{} {}'.format(i,fail))
