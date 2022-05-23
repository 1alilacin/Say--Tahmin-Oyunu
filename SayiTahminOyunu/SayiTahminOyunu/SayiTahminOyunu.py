import random
sayi=random.randint(0,20)
x=3
while x>0:
    x=x-1
    tahmin=int(input("Lütfen tahmininizi giriniz:"))
    if tahmin==sayi:
     print("Tebrikler tahmininiz başarılı!!!")
    elif tahmin>sayi:
        print("Lütfen daha küçük bir tahminde bulununuz:")
    elif tahmin<sayi:
     print("Lütfen daha büyük bir tahminde bulununuz:")
