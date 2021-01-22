
giris = ("""
********************************************
HESAP MAKİNESİ

TOPLAMA İŞLEMİ YAPMAK İÇİN 1 'e BASIN.
ÇIKARMA İŞLEMİ YAPMAK İÇİN 2 'e BASIN.
ÇARPMA İŞLEMİ  YAPMAK İÇİN 3 'e BASIN.
BÖLME İŞLEMİ   YAPMAK İÇİN 4 'e BASIN.
KARESİNİ ALMAK İÇİN 5 'e BASIN.
KAREKÖK HESAPLAMAK İÇİN 6 'YA BASIN.
********************************************
""")


while True:
    
    print(giris)

    operation = str(input("İşlem seçiniz(Çıkmak için q'yu tuşlayın): "))

    if operation == "q":
        print("Çıkılıyor...")
        break
    elif operation == "1":
        num1 = int(input("Birinci sayıyı giriniz: "))
        num2 = int(input("İkinci sayıyı giriniz: "))
        print("Sonuç:", num1 + num2)
        print("--------------------------------")
    elif operation == "2":
        num1 = int(input("Birinci sayıyı giriniz: "))
        num2 = int(input("İkinci sayıyı giriniz: "))
        print("Sonuç:", num1 - num2)
        print("--------------------------------")
    elif operation == "3":
        num1 = int(input("Birinci sayıyı giriniz: "))
        num2 = int(input("İkinci sayıyı giriniz: "))
        print("Sonuç:", num1 * num2)
        print("--------------------------------")
    elif operation == "4":
        num1 = int(input("Birinci sayıyı giriniz: "))
        num2 = int(input("İkinci sayıyı giriniz: "))
        print("Sonuç:", num1 / num2)
        print("--------------------------------")
    elif operation == "5":
        num1 = int(input("Bir sayi giriniz: "))
        print("Sonuç = ", num1 ** 2)
        print("--------------------------------")
    elif operation == "6":
        num1 = int(input("Bir sayi giriniz: "))
        print("Sonuç = ", num1 ** 0.5)
        print("--------------------------------")
    else:
        print("Geçersiz işlem girdiniz...")
        print("Aşagidaki seçeneklerden birini girin: ", giris)
        

