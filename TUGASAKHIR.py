#MesinKasir
from tkinter import N, Y


pilihan ="Y"
while pilihan=="Y":
    print(""""
    ============================)

    BobaQ Drink
    List Menu 

    ============================
    A. Chocolate : Rp 15000
    B. Cappucino : Rp 15000
    C. Matcha : Rp 18000
    ============================
    """)
    pesan= str(input("masukkan list abjad menu BobaQ="))
    jumlahpesanan=int(input("masukkanjumlah pesanan="))
    if pesan == "a":
        listnama= "Chocolate"
        harga=(15000*jumlahpesanan)
        ppn=int(harga*0.1)
        totalharga= int(harga+ppn)
    elif pesan == "b":
        listnama= "Cappucino"
        harga=(15000*jumlahpesanan)
        ppn=int(harga*0.1)
        totalharga= int(harga+ppn)
    elif pesan == "c":
        listnama= "Matcha"
        harga=(18000*jumlahpesanan)
        ppn=int(harga*0.1)
        totalharga= int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        totalharga= "-"
        pilihan= input("menu tidak tersedia, silahkan masukkan abjad yang tersedia silahkan ulangi Y/N=")

    print("--------------------------")
    print("BobaQ Drink")
    print("--------------------------")
    print("Menu:", listnama)
    print("Jumlah Pesan:", jumlahpesanan)
    print("Harga:", harga)
    print("PPN:",ppn)
    print("--------------------------")
    print("Jumlah Bayar:", totalharga)
    print("--------------------------")
    pilihan= input("apakah anda inginorder kembali Y/N=")