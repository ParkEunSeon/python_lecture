a = int(input("숫자를 입력하세요."))

# if a < 100:
#     print(f"{a}는 100보다 작군요.")
# else :
#     print(f"{a}는 100보다 크군요.")

if a > 50 :
    if a < 100 :
        print(f"{a}는 50보다 크고 100보다 작군요.")
    elif a == 100:
        print(f"{a}는 100과 같군요.")
    else :
        print(f"와~ {a}는 100보다 크군요.")
else :
    print(f"{a}는 50보다 작군요.")