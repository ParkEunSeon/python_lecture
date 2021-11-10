a = 99
if a < 100 :
    print("100보다 작군요.")


b = int(input("숫자를 입력하세요."))
if a < b:
    print(f"{b}가 99보다 크군요.")
elif a > b:
    print(f"{b}가 99부터 작군요.")
else:
    print(f"{b}가 99와 같군요.")