aa = []
bb = []
value = 0

for i in range(0,100):
    aa.append(value)
    value += 2

for i in range(0, 100):
    bb.append(aa[99 - i])

print(f"bb[0]에는 {bb[0]}이, bb[99]에는 {bb[99]}값이 입력됩니다.")

a = [1,2,3,4,5,6,7]

print(a[2:5])

b = (1,2,3)
print(tuple(a))
print(list(b))