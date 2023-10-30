def k_kucuk(k, listemiz):
    if k < 1 or k > len(listemiz):  # sınırlamalar getiriyoruz, geçersiz değer girilmemesi adına
        return "Geçersiz k değeri"

    listemiz.sort()  # listeyi küçükten büyüğe sıralayan kısım
    k_kucuk_sonuc = listemiz[k - 1]  # k. en küçük elemanı al. Listedeki ilk eleman 0 olduğu için k-1
    return k_kucuk_sonuc

listemiz = [7, 10, 4, 20, 15, 3]

##########################################################################################################3
def en_yakin_cift(hedef, liste2):
    liste2.sort()
    en_kucuk_fark = float('inf')
    en_yakin_cift = None

    for i in range(len(liste2) - 1):
        for j in range(i + 1, len(liste2)):
            toplam = liste2[i] + liste2[j]
            fark = abs(toplam - hedef)
            if fark < en_kucuk_fark:
                en_kucuk_fark = fark
                en_yakin_cift = (liste2[i], liste2[j])

    return en_yakin_cift

liste2 = [5, 25, 27, 29, 33, 53]

########################################################################################################
def tekrar_eden_elemanlar(liste3):
    görülmüş_olanlar = set()
    tekrarlilar = set()

    for eleman in liste3:
        if eleman in görülmüş_olanlar:
            tekrarlilar.add(eleman)
        görülmüş_olanlar.add(eleman)

    return list(tekrarlilar)

liste3 = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]


def matris_carpimi(matris1, matris2):
    satir_matris1 = len(matris1)
    sutun_matris1 = len(matris1[0])
    satir_matris2 = len(matris2)
    sutun_matris2 = len(matris2[0])

    # İki matrisin çarpılabilirliğini kontrol eder
    if sutun_matris1 != satir_matris2:
        return "Matrisler çarpılamaz. İlk matrisin sütun sayısı ikinci matrisin satır sayısına eşit olmalıdır", " """
    
    # Sonuc matrisini oluşturur
    sonuc = [[0 for _ in range(sutun_matris2)] for _ in range(satir_matris1)]

    # Matris çarpımını hesaplar
    for i in range(satir_matris1):
        for j in range(sutun_matris2):
            sonuc[i][j] = sum(mat1 * mat2 for mat1, mat2 in zip(matris1[i], (row[j] for row in matris2)))

    return sonuc

def matris_girisi_al():
    print("İlk matrisi girin:")
    matris1 = []
    for _ in range(int(input("Matris satır sayısı: "))):
        satir = [int(x) for x in input("Satırı girin (virgülle ayırın): ").split(",")]
        matris1.append(satir)

    print("İkinci matrisi girin:")
    matris2 = []
    for _ in range(int(input("Matris satır sayısı: "))):
        satir = [int(x) for x in input("Satırı girin (virgülle ayırın): ").split(",")]
        matris2.append(satir)

    return matris1, matris2



def kelime_frekansi():
    # Kullanıcıdan dosya adını girmesini iste
    text_dosya_yolu = input("Lütfen dosya adını uzantısı ile girin: ")

    try:
        # Dosyayı açıp içeriğini okur
        with open(text_dosya_yolu, 'r') as dosya:
            metin = dosya.read()

        # Metni kelimelere ayırır ve her kelimeyi küçük harfe çevirir
        kelimeler = metin.lower().split()

        # Kelimeleri birer çift (kelime, sayı) olarak eşler
        kelime_sayilari = [(kelime, kelimeler.count(kelime)) for kelime in set(kelimeler)]

        # Sonuçları yazdırır
        for kelime, sayi in kelime_sayilari:
            print(f"{kelime}={sayi} adet")
    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen doğru dosya adını girin.")


def en_kucuk_deger(liste):
    if not liste:
        return None
    if len(liste) == 1:
        return liste[0]
    ilk_eleman = liste[0]
    geri_kalan = liste[1:]
    en_kucuk_geri_kalan = en_kucuk_deger(geri_kalan)
    if ilk_eleman < en_kucuk_geri_kalan:
        return ilk_eleman
    else:
        return en_kucuk_geri_kalan


def eb_ortak_bolen(x, y):
    if y == 0:
        return x
    else:
        return eb_ortak_bolen(y, x % y)


def asal_veya_degil(sayi):
    if sayi <= 1:
        return False
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True


def hizlandirici(n, k, fib_k, fib_k1):
    if k == n:
        return fib_k
    else:
        return hizlandirici(n, k + 1, fib_k + fib_k1, fib_k)

while True:
    print("\nConsole Menü")
    print("1. K'den Küçük Elemanı Bul")
    print("2. En Yakın Çifti Bul")
    print("3. Tekrar Eden Elemanları Bul")
    print("4. Matris Çarpımı")
    print("5. Kelime Frekansı")
    print("6. En küçük değer")
    print("7. Kök")
    print("8. En büyük ortak bölen")
    print("9. Asal Sayı Kontrolü")
    print("10. Fibonacci Hesaplama")
    print("11. Çıkış")
    secim = input("Lütfen bir seçenek girin: ")

    if secim == '1':
        k = int(input("1-6 arası değer giriniz: "))  # örneğin 3. en küçük eleman
        sonuc = k_kucuk(k, listemiz)
        print(k, ". en küçük eleman:", sonuc)
    
    elif secim == '2':
        hedef_sayi = int(input("Hedef sayıyı girin: "))
        en_yakin_cifti = en_yakin_cift(hedef_sayi, liste2)
        print("En yakın çift:", en_yakin_cifti)
    
    elif secim == '3':
        tekrarli_degerler = tekrar_eden_elemanlar(liste3)
        print("Tekrar eden elemanlar:", tekrarli_degerler)
    
    elif secim == '4':
        # Matris çarpımı işlemi
        matris1, matris2 = matris_girisi_al()
        sonuc_matrisi = matris_carpimi(matris1, matris2)
        print("Matris Çarpım Sonucu:")
        for satir in sonuc_matrisi:
            print(satir)
        
    elif secim == '5':
        kelime_frekansi()
    
    elif secim == '6':
        liste = [int(x) for x in input("Listeyi virgülle ayırarak girin: ").split(",")]
        en_kucuk = en_kucuk_deger(liste)
        print(f"Listedeki en küçük değer: {en_kucuk}")

    elif secim == '7':
        print()

    elif secim == '8':
        sayi1 = int(input("Birinci sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))
        ebob = eb_ortak_bolen(sayi1, sayi2)
        print(f"{sayi1} ve {sayi2} sayılarının en büyük ortak böleni: {ebob}")

    elif secim == "9":
        sayi = int(input("Bir sayı girin: "))
        if asal_veya_degil(sayi):
            print(sayi, "asal bir sayıdır.")
        else:
            print(sayi, "asal bir sayı değildir.")


    elif secim == "10":
        n = int(input("Bir pozitif tamsayı (n) girin: "))
        if n <= 0:
            print("Geçerli bir pozitif tamsayı girin.")
        else:
            sonuc = hizlandirici(n, 1, 1, 0)
            print(f"Fibonacci({n}) = {sonuc}")
    
    elif secim == "11":
        print("Programdan çıkılıyor.")
        break

    else:
        print("Geçersiz seçenek! Lütfen geçerli bir seçenek girin.")

