hap = 0
# for i in range(501, 1001,2):
#     hap += i

# for i in range(500, 1000):
#     if i % 2 != 0:
#         hap += i
a = 0
sum = 0
b = 0
temp = [i for i in range(500, 1000) if i % 2 == 1]
for i in range(len(temp)):
    hap += temp[i]
print(f"500과 1000사이에 있는 홀수의 합계 : {hap}")
