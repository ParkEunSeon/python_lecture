guguLine = ""

for i in range(2,10):
    guguLine = guguLine + (f"#  {i}단  #")
print(guguLine)

for i in range(1,10):
    guguLine = " "
    for j in range(2,10):
        guguLine = guguLine + str(f"{j} X {i} = {j*i}") 
    print(guguLine)