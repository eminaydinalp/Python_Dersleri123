# Değişken Tanımlama  (1.Ders)

"""
Yorum Satırı

"""

sayi1 = 5
yazi1 = "İstanbul"

sayi1 = 10
sayi1 = sayi1 + 1
sayi1 += 1
sayi1 -= 1
sayi1 *= 2

yazi1 = "Ankara"


#%% Math (2.Ders)

sayi2 = 10

toplama = sayi1 + sayi2
print(toplama)
print(5)
print("Anakara")
cikartma = sayi1 - sayi2
print(cikartma)

carpma = sayi1 * sayi2
print(carpma)

bolme = sayi1 / sayi2
print(bolme)

bolme2 = sayi1 // sayi2
print(bolme2)

kalan_bulma = sayi1 % sayi2
print(kalan_bulma)

ust_bulma = 2**3
print(ust_bulma)

kare_kok = 64**0.5
print(kare_kok)

r = 4
pi = 3.14

alan = pi*r**2
print(alan)

#%% Veri Tipleri (3.Ders)

# int -> 0, 100, -20

a = 5
print(type(a))

# float -> 1.5, -9.6

b = 3.4
print(type(b))

# String 

c = "Ahmet"
d = "Ali"

print(c)
print("ömer")
print(c+d)
print(c+" "+d)
print(c*3)

# index

print(c[0])
print(c[1])
print(c[-1])
print(c[-2])

# Parçalama -> degisken_Adi[başlama_index :bitiş_index :atlama_değeri ]

e = "Abdurrahim"
print(e[1:5])
print(e[0:2])
print(e[2:7:2])
print(e[:3])
print(e[2:])
print(e[::])
print(e[::-1])

print(e[:2] + e[2:])

print(len(e))

e = "ömer"
e[0] = "a"



























