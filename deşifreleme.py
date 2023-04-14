def atbash_desifrele(metin):
    return atbash_sifrele(metin)

def affine_desifrele(metin, a, b):
    mod_inv_a = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            mod_inv_a = i
            break
    sifrelenmis_metin = ""
    for harf in metin:
        if harf.isalpha():
            karakter_kodu = ord(harf)
            if harf.islower():
                karakter_kodu = (mod_inv_a * ((karakter_kodu - 97) - b + 26)) % 26 + 97
            else:
                karakter_kodu = (mod_inv_a * ((karakter_kodu - 65) - b + 26)) % 26 + 65
            sifrelenmis_metin += chr(karakter_kodu)
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin

sifreli_metin = input("lütfen şifrelenmiş metni giriniz : ")
atbash_desifretilmis_metin = atbash_desifrele(sifreli_metin)
a = 5
b = 7
affine_desifretilmis_metin = affine_desifrele(atbash_desifretilmis_metin, a, b)

print("Şifrelenmiş Metin: ", sifreli_metin)
print("Orijinal Metin: ", affine_desifretilmis_metin)