#a> Thứ tự tăng dần a,b,c:
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
min=min(a,b,c)
max=max(a,b,c)
mid=a+b+c-min-max
print("Thứ tự tăng dần a,b,c là: ",min,",",mid,",",max)

#b> Thứ tự tăng dần N:
N = int(input("Nhập vào số nguyên N: "))
sorted_N = ''.join(sorted(N))
print(f"Số có các con số theo thứ tự tăng dần: {sorted_N}")