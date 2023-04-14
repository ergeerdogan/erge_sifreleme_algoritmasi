def atbash_sifrele(metin):
    alfabe = 'abcdefghijklmnopqrstuvwxyz'
    ters_alfabe = alfabe[::-1]
    sifrelenmis_metin = ""
    for harf in metin:
        if harf.isalpha():
            indeks = alfabe.index(harf.lower())
            sifrelenmis_harf = ters_alfabe[indeks]
            if harf.isupper():
                sifrelenmis_harf = sifrelenmis_harf.upper()
            sifrelenmis_metin += sifrelenmis_harf
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin

def affine_sifrele(metin, a, b):
    sifrelenmis_metin = ""
    for harf in metin:
        if harf.isalpha():
            karakter_kodu = ord(harf)
            if harf.islower():
                karakter_kodu = (a * (karakter_kodu - 97) + b) % 26 + 97
            else:
                karakter_kodu = (a * (karakter_kodu - 65) + b) % 26 + 65
            sifrelenmis_metin += chr(karakter_kodu)
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin

metin = input("lütfen metin giriniz : ")
atbash_sifreli_metin = atbash_sifrele(metin)
a = 5
b = 7
affine_sifreli_metin = affine_sifrele(atbash_sifreli_metin, a, b)

print("Orijinal Metin: ", metin)
print("erge algoritması : ", affine_sifreli_metin)