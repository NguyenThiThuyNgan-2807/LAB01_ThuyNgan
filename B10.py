x=int(input("Số xe của bạn (gồm 4 chữ số): "))
a= x//1000
b= (x-a*1000)//100
c= (x-a*1000-b*100)//10
d= x-a*1000-b*100-c*10
print("Số nút của xe bạn: ",a+b+c+d)
