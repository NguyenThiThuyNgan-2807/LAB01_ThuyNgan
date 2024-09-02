a = int(input("Nhập giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
if 0<=a<=24:
    if 0<=b<=60 and 0<=c<=60:
        print("Thời gian hợp lệ: ",f"{a}:{b}:{c}")
    else: 
        print("Thời gian không hợp lệ.")
elif 0<=b<=60:
    if 0<=a<=24 and 0<=c<=60:
        print("Thời gian hợp lệ: ",f"{a}:{b}:{c}")
    else: 
        print("Thời gian không hợp lệ.")
else:
    if 0<=a<=24 and 0<=b<=60:
        print("Thời gian hợp lệ: ",f"{a}:{b}:{c}")
    else: 
        print("Thời gian không hợp lệ.")