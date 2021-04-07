# fswair/TCKimlikDogrualama

Açıklama: Türkiye Cumhuriyeti Kimlik Numarasını Doğrulama Amacıyla, TC Kimlik No Doğrulama Algoritması Baz Alınarak Oluşturulmuş Bir Kimlik Doğrulama Aracıdır.

Amaç: Verilen TC Kimlik Numarasını, Doğrulama Algoritmasının Yönergelerini Kontrol Ederek Doğrular.

Bu Yönergeler Şunlardır:

1- TCKN 11 Haneden Oluşmalıdır.

2- TCKN '0' İle Başlamamalıdır.

3- TCKN Tamamen Sayılardan Oluşmalıdır.

4- TCKN 10. Basamağı 1,3,5,7. basamakların toplamının 7 ile çarpımından, 2,4,6,8 basamakların toplamını çıkarıp, 10 sayısına bölümünden kalanı alarak bulunur. (MOD10)

5- TCKN 11. Basamağı, 1,2,3,4,5,6,7,8,9,10. basamakların toplamının 10 sayısına bölümünden kalanı alarak bulunur. (MOD10)

6- TCKN Son Basamağı Çift Sayı Olmalıdır.
