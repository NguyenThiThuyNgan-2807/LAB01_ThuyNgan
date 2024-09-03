a = input("Nhập hình (v),(n),(t): ")
if a=="v":
    x=float(input("Nhập cạnh: "))
    print("P(v) = ",x*4)
    print("S(v) = ",x*x)
elif a=="n":
    c=float(input("Nhập chiều rộng: "))
    d=int(input("Nhập chiều dài: "))    
    print("P(n) = ",(c+d)*2)
    print("S(n) = ",c*d)
else:
    r=float(input("Nhập bán kính: "))
    print("P(n) = ",r*3.14)
    print("S(n) = ",r*2*3.14)
    
