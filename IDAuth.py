'''
*******************************************
* Powered by TheBadCode
* Author: @FLUSWAIR
* ID Auth Project | Kimlik Doğrulama Projesi
* https://www.github.com/fswair
*******************************************
'''

idn = False
rule = """
1- TCKN 11 Haneden Oluşmalıdır.

2- TCKN '0' İle Başlamamalıdır.

3- TCKN Tamamen Sayılardan Oluşmalıdır.

4- TCKN 10. Basamağı 1,3,5,7,9 basamakların toplamının 7 ile çarpımından, 2,4,6,8 basamakların toplamını çıkarıp, 10 sayısına bölümünden kalanı alarak bulunur. (MOD10)

5- TCKN 11. Basamağı, 1,2,3,4,5,6,7,8,9,10. basamakların toplamının 10 sayısına bölümünden kalanı alarak bulunur. (MOD10)

6- TCKN Son Basamağı Çift Sayı Olmalıdır.
"""

try:
    name = input("İsminiz: ")
    idn = int(input("TC Kimlik Numaranızı Giriniz: "))
    str_idn = str(idn)
    cx = sum([int(letter) for letter in str_idn][0:9:2]) * 7 # (1 + 3 + 5 + 7 + 9) * 7
    cy = (cx - (sum([int(letter) for letter in str_idn][1:8:2]))) % 10 # CX - (IDN[2,4,6,8]) % 10
except:
    pass




if idn:
    if len(str_idn) == 11 and not str_idn.startswith("0") and str_idn.isdigit():
        if int(str_idn[9]) == cy:
            cz = sum([int(s) for s in str_idn][0:10:1]) % 10
            if int(str_idn[10]) == cz and int(str_idn[10]) % 2 == 0:
                # Doğrulandığında bir bildirim veriyoruz.
                print(f'Merhaba, {name}! Girmiş olduğunuz {str_idn} kimlik numarası için TC Kimlik Doğrulama Başarılı!')
    else:
        print(rule)
else:
    # 11 haneli mi diye kontrol edelim!
    raise Exception("\n11 haneden oluşan bir sayı girdiğinizden emin olup tekrar deneyin.")
