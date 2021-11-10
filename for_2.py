# for i in range(0,3): #3개 : 0이상 3미만
#     print("안녕하세요? for문을 공부중입니다.^^")

# for i in range(0,10,2): # 5개(0이상 10미만 2씩 증가), 0,2,4,6,8
#     print("안녕하세요? for문을 공부중입니다.^^")
# str = ""
# for i in range(10):
#     str = str + "*"
#     print(str)
# str = "**********"
# for i in range(10,0,-1):
    
#     print(f"{str[0:i]}")
str = ""
for i in range(0,20):
    if i < 10:
        str = str + "*"
        print(str)
    else:
        print(f"{str[0:i]}")