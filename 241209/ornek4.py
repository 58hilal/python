not1=int(input("1. notu giriniz: "))        # kullanıcıdan not1'i girilmesini istendi
not3=int(input("3. notu giriniz: "))        # kullanıcıdan not2'yi girilmesini istendi
not2=int(input("2. notu giriniz: "))        # kullanıcıdan not3'ün girilmesi istendi
ortalama=(not1+not2+not3)/3                 # girilen notlar toplamı alınıp 3'e bölünür
print("3 notun ortalaması: ",ortalama)      # ortalama ekrana yazdırılır
print(type(ortalama))                       # türünü ekrana yazdırır