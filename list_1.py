aa = [10,20,30,40]
hap = 0

# aa[0] = int(input("1번째 숫자 : ")))
# aa[1] = int(input("2번째 숫자 : ")))
# aa[2] = int(input("3번째 숫자 : "))
# aa[3] = int(input("4번째 숫자 : "))

# hap = aa[0] + aa[1] + aa[2] + aa[3]

# print(f"합계 : {hap}")

for i in range(0,len(aa)):
    aa[i] = int(input(f"{i+1}번째 숫자 : "))
    hap += aa[i]
print(f"합계 : {hap}")