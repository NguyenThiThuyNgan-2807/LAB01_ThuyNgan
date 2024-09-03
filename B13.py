a = int(input("Nhập ngày: "))
b = int(input("Nhập tháng: "))
c = int(input("Nhập năm: "))
d = c%100
print("a> Ngày/tháng/năm: ",f"{a}/{b}/{c}")
print("b> Ngày/tháng/năm: ",f"{a}/{b}/{d}")
print("c> Năm/tháng/ngày: ",f"{c}/{b}/{a}")
