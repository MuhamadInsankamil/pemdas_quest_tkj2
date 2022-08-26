print("program bangun datar")

print("1.balok")

panjang = int(input("masuhakan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
tinggi = int(input("masukan nilai tinggi: "))

volume_balok = panjang * lebar * tinggi
print("nilai volume balok", volume_balok)

print("2.\nTabung")
import math
r =float(input("masukan jari jari : "))
t =float(input("masukan tinggi :"))
pi =math. pi 
v =round(pi*(r*r)*t,2)
print("volume tabung adalah : ",v)

print("3.\nLimas")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))
volume_1= alas * tinggi
print("volume limas adalah: ", volume_1)
 
kursDolar = 1400
rupiah = float(input("masukan uang rupiah= "))
rupToDol = rupiah/ kursDolar
dolDecimal = round(rupToDol, 2)
print("Rp.", rupiah, "==> US$", dolDecimal )
