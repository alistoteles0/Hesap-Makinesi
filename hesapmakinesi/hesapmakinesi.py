
while True:
    try:
        num1 = float(input("1. sayıyı giriniz: "))
        num2 = float(input("2. sayıyı giriniz: "))
        break
    except ValueError:
        print("Lütfen geçerli bir değer giriniz.")
        
op = input("Lütfen yapmak istediğiniz işlemi giriniz. (+,-,*,/): ")

if op == "+":
    print(num1, "+" , num2 , "=" , num1 + num2)
    
elif op == "-":
    print(num1 , "-" , num2 , "=" , num1 - num2)
    
elif op == "*":
    print(num1 , "*" , num2 , "=" , num1 * num2)

elif op == "/":
    try:
        print(num1 , "/" , num2 , "=" , num1 / num2)
    except ZeroDivisionError:
        print("Tanımsız.")
else:
    print("Geçersiz işlem seçimi.")
        
    
    