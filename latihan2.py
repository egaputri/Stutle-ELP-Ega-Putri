#No1
y= 7
x= 10
print(x-y)

#No2
a = 10
b= 3
print(a**b)

#No3
tahun= input("Masukkan angka:")
if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print("bilangan tersebut adalah tahun kabisat")
        else:
            print ("bukan tahun kabisat")
print(tahun)       
