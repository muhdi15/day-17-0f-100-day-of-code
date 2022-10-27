a= float(input("berat :"))
b= float(input("Tinggi :"))

bmi = a / (b * b)

if(bmi < 17.0):
    print("anda sangat kurus")

if(bmi > 17.0 and bmi < 20.0):
    print("anda normal")

if(bmi > 20.0 and bmi < 27.0):
    print("anda gemuk")
    

