def k_kucuk(k, liste):
    try:
        if k <= 0:
            return "0'dan büyük bir k değeri giriniz!"
        elif k > len(liste):
            return "Liste boyutundan küçük bir k değeri giriniz!"

        liste.sort()
        return liste[k - 1]
    except ValueError:
        return "Geçersiz bir değer girdiniz.Lütfen sayıları doğru bir şekilde giriniz."


def en_yakin_cift(sayi, liste):
    try:
        if len(liste) < 2:
            return "Listede en az iki eleman olmalıdır."

        liste.sort()

        en_yakin_cift = (liste[0], liste[1])
        en_yakin_fark = abs(en_yakin_cift[0] + en_yakin_cift[1] - sayi)

        for i in range(len(liste) - 1):
            for j in range(i + 1, len(liste)):
                toplam = liste[i] + liste[j]
                fark = abs(toplam - sayi)
                if fark < en_yakin_fark:
                    en_yakin_cift = (liste[i], liste[j])
                    en_yakin_fark = fark

        return en_yakin_cift
    except ValueError:
        return "Geçersiz giriş.Lütfen doğru formatta liste ve sayı giriniz."


def tekrar_eden_elemanlar(listeler):
    try:
        liste = [int(x) for x in listeler]
        tekrarlar = [x for x in liste if liste.count(x) > 1]
        sonuc = list(set(tekrarlar))

        if sonuc:
            print("Listede tekrar eden elemanlar:", sonuc)
        else:
            print("Listede tekrar eden eleman yok.")
    except ValueError:
        print("Geçersiz giriş.Lütfen doğru formatta liste ve sayı giriniz.")


def matris_olustur(satir, sutun):
    matris = []
    for i in range(satir):
        satir = [int(x) for x in input(f"{i + 1}. satırı giriniz (virgülle ayırınız): ").split(",")]
        if len(satir) != sutun:
            raise ValueError("Satır, sütun sayısıyla uyumsuz!")
        matris.append(satir)
    return matris

def matris_carpimi(list1, list2):
    if len(list1[0]) != len(list2):
        return "Matrisler çarpılabilir olmalıdır!"

    sonuc = [[sum(a * b for a, b in zip(list1_satir, list2_sutun)) for list2_sutun in zip(*list2)] for list1_satir in list1]
    return sonuc


def kelime_frekans(dosya_yolu):
    try:
        with open(dosya_yolu, 'r') as dosya:
            metin = dosya.read()

        kelimeler = metin.lower().split()
        kelime_frekanslari = dict(map(lambda kelime: (kelime, kelimeler.count(kelime)), kelimeler))
        return kelime_frekanslari
    except FileNotFoundError:
        return "Dosya bulunamadı."


def en_kucuk_deger(liste):
    if not liste:
        return "Geçersiz liste"

    en_kucuk = liste[0]

    for eleman in liste:
        if eleman < en_kucuk:
            en_kucuk = eleman
    return en_kucuk


def karekok(N, x0, tol=1e-10, maxiter=10):
    x = x0
    for i in range(maxiter):
        x_n = 0.5 * (x + N / x)
        hata = abs(x_n**2 - N)

        if hata < tol:
            return x_n

        x = x_n

    raise ValueError(f"{maxiter} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin.")


def eb_ortak_bolen(int1, int2):
    if int2 == 0:
        return int1
    else:
        return eb_ortak_bolen(int2, int1 % int2)


def asal_veya_degil(n):
    def asal_kontrol(i):
        if i <= 1:
            return True
        if n % i == 0:
            return False
        return asal_kontrol(i - 1)

    if n <= 1:
        return False
    return asal_kontrol(n - 1)


def hizlandirici(n, k, fib_k, fib_k1):
    if k == n:
        return fib_k
    else:
        fib_k2 = fib_k + fib_k1
        return hizlandirici(n, k + 1, fib_k2, fib_k)

print("-----Menüye Hoş Geldiniz-----")

def main():
    while True:
        print("1. İstenen En Küçük Elemanı Bul")
        print("2. En Yakın Çifti Bul")
        print("3. Listede Tekrar Eden Elemanları Bul")
        print("4. Matris Çarpımı Hesapla")
        print("5. Bir Text Dosyasındaki Kelime Frekansını Bul")
        print("6. Listedeki En Küçük Değeri Bul")
        print("7. Karekök Hesapla")
        print("8. Ebob Hesapla")
        print("9. Asallık Testi")
        print("10. Fibonacci Sayısını Hesapla")
        print("11. Çıkış")

        choice = int(input("Yukarıdaki menüden yapmak istediğiniz işlemi seçiniz: "))

        if choice == 1:
            try:
                liste = [int(x) for x in input("Virgülle ayrılmış şekilde listeyi giriniz: ").split(',')]
                k = int(input("Listede kaçıncı sıradaki sayıyı bulmak istiyorsunuz?: "))
                sonuc = k_kucuk(k, liste)
                print(f"{k}. sıradaki sayı: {sonuc}")
            except ValueError:
                print("Geçersiz giriş.Lütfen doğru formatta sayı giriniz.")
        elif choice == 2:
            try:
                liste = [int(x) for x in input("Virgülle ayrılmış şekilde listeyi giriniz: ").split(',')]
                sayi = int(input("Bir sayı giriniz: "))
                sonuc = en_yakin_cift(sayi, liste)
                print(f"Seçilen sayıya en yakın sayı çifti: {sonuc[0]} ve {sonuc[1]}")
            except ValueError:
                print("Geçersiz giriş.Lütfen doğru formatta liste ve sayı giriniz.")
        elif choice == 3:
            liste = input("Virgülle ayrılmış şekilde listeyi giriniz: ").split(",")
            tekrar_eden_elemanlar(liste)
        elif choice == 4:
            try:
                satir1 = int(input("Birinci matrisin satır sayısını giriniz: "))
                sutun1 = int(input("Birinci matrisin sütun sayısını giriniz: "))
                list1 = matris_olustur(satir1, sutun1)

                satir2 = int(input("İkinci matrisin satır sayısını giriniz: "))
                sutun2 = int(input("İkinci matrisin sütun sayısını giriniz: "))
                list2 = matris_olustur(satir2, sutun2)

                sonuc = matris_carpimi(list1, list2)
                print("Birinci Matris: ", list1)
                print("İkinci Matris: ", list2)
                print("Sonuç: ", sonuc)
            except ValueError:
                print("Geçersiz giriş.Lütfen matris boyutlarını doğru bir şekilde giriniz.")
        elif choice == 5:
            dosya_yolu = input("Bulunduğunuz klasördeki txt dosyasının adını giriniz.(Örneğin: giris_metni.txt): ")
            frekanslar = kelime_frekans(dosya_yolu)

            if type(frekanslar) is dict:
                for kelime, frekans in frekanslar.items():
                    print(f"{kelime}: {frekans} kez geçiyor.")
            else:
                print("Dosya bulunamadı.")
        elif choice == 6:
            try:
                liste = [int(x) for x in input("Virgülle ayrılmış şekilde listeyi giriniz: ").split(",")]
                en_kucuk = en_kucuk_deger(liste)
                print(f"Listedeki en küçük sayı: {en_kucuk}")
            except ValueError:
                print("Geçersiz giriş.Sayıları virgülle ayırarak giriniz.")
        elif choice == 7:
            N = float(input("N değerini giriniz: "))
            x0 = float(input("Başlangıç değerini giriniz: "))
            tol = 1e-10
            maxiter = 10
            karekok_deger = karekok(N, x0, tol, maxiter)
            print(f"Karekök: {karekok_deger}")
        elif choice == 8:
            sayi1 = int(input("Ebob hesaplanması için birinci sayıyı giriniz: "))
            sayi2 = int(input("Ebob hesaplanması için ikinci sayıyı giriniz: "))
            ebob = eb_ortak_bolen(sayi1, sayi2)
            print(f"{sayi1} ve {sayi2} ebob değeri: {ebob}")
        elif choice == 9:
            sayi = int(input("Asallığını kontrol etmek istediğiniz sayıyı giriniz: "))
            sonuc = asal_veya_degil(sayi)
            print(f"Asal sayı mı: {sonuc}")
        elif choice == 10:
            n = int(input("Kaçıncı Fibonacci sayısını hesaplamak istiyorsunuz? "))
            result = hizlandirici(n, 1, 1, 0)
            print(f"{n}. Fibonacci sayısı: {result}")
        elif choice == 11:
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek.Lütfen tekrar deneyin.")

        yeni_islem = input("Yeni işlem yapmak istiyor musunuz? (Evet/Hayır): ").lower()
        if yeni_islem != "evet":
            print("Programdan çıkılıyor.")
            break
        print("")

if __name__ == "__main__":
    main()