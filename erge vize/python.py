def erge_sifrele(metin, kaydirma_miktari):
    sifreli_metin = ""
    for karakter in metin:
        if karakter.isalpha():
            ascii_kod = ord(karakter)
            if karakter.islower():
                sifreli_ascii = (ascii_kod - ord('a') + kaydirma_miktari) % 26 + ord('a')
            else:
                sifreli_ascii = (ascii_kod - ord('A') + kaydirma_miktari) % 26 + ord('A')
            sifreli_karakter = chr(sifreli_ascii)
            sifreli_metin += sifreli_karakter
        else:
            sifreli_metin += karakter
    return sifreli_metin

metin = input("Şifrelenecek metni girin: ")
kaydirma_miktari = int(input("Kaydırma miktarını girin: "))
sifreli_metin = erge_sifrele(metin, kaydirma_miktari)
print("Şifreli metin: " , sifreli_metin)