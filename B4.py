N = int(input("Số nguyên dương N: "))
x = N//10
y = N%10
if 9<N<100:
    print("Tổng các chữ số của N: ", x+y)
else:
    print("Số nguyên N không hợp lệ.")
