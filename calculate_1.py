a = 5; b = 3
print(a + b, a-b,a*b,a/b,a//b,a%b,a**b)

a, b, c = 2, 3, 4
print(a + b - c, a + b * c, a * b / c)

# 숫자를 문자열로 변환하려며 str()함수 사용

# a= 100; b= 100.123
# str(a) + '1'; str(b) + '1'

a = 10
a += 5; print(a)
a -= 5; print(a)
a *= 5; print(a)
a /= 5; print(a)
a //=5; print(a)
a %= 5; print(a)
a **= 5; print(a)

## 변수 선언 부분
money, c500, c100, c50, c10 = 0,0,0,0,0

## 메인코드 부분
money = int(input("교환할 돈은 얼마입니까?"))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10
print(f"500원짜리는 {c500}이고 100원 짜리는 {c100}이며 50원짜리는 {c50}이며 10원짜리는 {c10}이므로 바꾸지 못한 잔돈은 {money}이다.")
print("\n 500원짜리 ==> %d개" % c500)
# print(" 100원짜리 ==> %d개" % c100)
print(" 100원짜리 ==> {}개".format(c100))
# print(" 50원짜리 ==> %d개" % c50)
print(f" 50원짜리 ==> {c50}개")
print(" 10원짜리 ==> %d개" % c10)
print(" 바꾸지 못한 잔돈 ==> %d원\n" % money)
# 0 : 거짓, 1: 참, 1보다 큰 수라면 있다, 비어있지 않다는 뜻
if(1234) : print("참이면 보여요")