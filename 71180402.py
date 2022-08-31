
# fungsi penjumlahan
def add(x, y):
   return x + y

# fungsi pengurangan
def subtract(x, y):
   return x - y

# fungsi perkalian
def multiply(x, y):
   return x * y

# fungsi pembagian
def divide(x, y):
   return x / y

# menu operasi
# print("Pilih Operasi.")
# print("1.Jumlah")
# print("2.Kurang")
# print("3.Kali")
# print("4.Bagi")

# Meminta input dari user
input_menu = input("Masukkan pilihan(1/2/3/4): ")

num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

#while input_menu !="q" and input_menu !="Q":
while True:
    print("Pilih Operasi.")
    print("1.Jumlah")
    print("2.Kurang")
    print("3.Kali")
    print("4.Bagi")
    if input_menu == '1':
        print(num1,"+",num2,"=", add(num1,num2))
        num1 = int(input("Masukkan bilangan pertama: "))
        num2 = int(input("Masukkan bilangan kedua: "))
        input_menu = input("Masukkan pilihan(1/2/3/4): ")
    elif input_menu == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))
        num1 = int(input("Masukkan bilangan pertama: "))
        num2 = int(input("Masukkan bilangan kedua: "))
        input_menu = input("Masukkan pilihan(1/2/3/4): ")
    elif input_menu == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))
        num1 = int(input("Masukkan bilangan pertama: "))
        num2 = int(input("Masukkan bilangan kedua: "))
        input_menu = input("Masukkan pilihan(1/2/3/4): ")
    elif input_menu == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
        num1 = int(input("Masukkan bilangan pertama: "))
        num2 = int(input("Masukkan bilangan kedua: "))
        input_menu = input("Masukkan pilihan(1/2/3/4): ")

    elif input_menu=="Q":
        break
    else:
        print("Input salah")
    



