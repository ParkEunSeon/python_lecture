select, answer, numStr, num1, num2 =0,0,"",0,0

select = int(input("1. 입력한 수식계산 2. 두수사이의 합계:"))

if select == 1:
    numStr = input("*** 수식을 입력하세요 : ")
    answer = eval(numStr) # eval () 함수를 사용하면 입력한 값을 숫자로 바꿔줌
    print(f"{numStr} 결과는 {answer}입니다.")
elif select == 2:
    num1 = int(input("*** 첫번째 숫자를 입력하세요 : "))
    num2 = int(input("*** 두번째 숫자를 입력하세요 : "))
    if num1 < num2:
        for i in range(num1,num2+1):
            answer += i
        print(f"{num1}+...+{num2}는 {answer}입니다.")
    else:
        for i in range(num2,num1+1):
            answer += i
        print(f"{num2}+...+{num1}는 {answer}입니다.")
else:
    print("1또는 2만 입력해야합니다.")