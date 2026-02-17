def get_numer(number):
    while True:
        opreand = input("Number" + str(number))
        try:
           return float(opreand)
 
        except:
            print("Invalid number, try again")
opreand = get_numer(1)
opreand2 = get_numer(2)                
sign = input("Sign: ")



result = 0
if sign == "+":
    result = opreand + opreand2

elif sign == "-":
    result =  opreand - opreand2
    
elif sign == "*":
    result = opreand * opreand2

elif sign == "/":
    if opreand2 != 0:
       result = opreand / opreand2 

    else:
        print("Divison by zero.")       

print(result)
