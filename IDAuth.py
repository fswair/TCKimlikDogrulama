'''
*******************************************
* Powered by TheBadCode
* Author: @FLUSWAIR
* ID Auth Project | Kimlik Doğrulama Projesi
* https://www.github.com/fswair
*******************************************
'''

idn = int(input("TC Kimlik Numaranızı Giriniz: "))
nIDN = []
idn = str(idn)
numbers = "1234567890"
nNUMS = []
for i in numbers:
  nNUMS.append(i)

for i in idn:
  nIDN.append(int(i))

result1 = (nIDN[0] + nIDN[2] + nIDN[4] + nIDN[6] + nIDN[8]) * 7
result2 = result1 - (nIDN[1] + nIDN[3] + nIDN[5] + nIDN[7])
b10 = (result2 % 10)
reality = 0

if b10 == nIDN[9]:
  reality = (reality + 1)

b11 = (nIDN[0] + nIDN[1] + nIDN[2] + nIDN[3] + nIDN[4] + nIDN[5] + nIDN[6] + nIDN[7] + nIDN[8] + nIDN[9]) % 10

if b11 == nIDN[10]:
  reality = (reality + 1)

if nIDN[0] != 0:
  reality = (reality + 1)

if len(nIDN) == 11:
  reality = (reality + 1)

nIDN_Truth = 0
for j in nIDN:
  if str(j) in nNUMS:
    nIDN_Truth+=1

if nIDN_Truth == 11:
  reality = (reality + 1)
if nIDN[10] % 2 == 0:
  reality = (reality + 1)

if reality == 6:
  print("TC Kimlik Doğrulama Başarılı.")
elif nIDN[10] % 2 != 0:
  print("TC Kimlik Numarası Tek Sayı İle Bitemez.")
elif(len(nIDN) != 11):
  print("TC Kimlik Numarası 11 Rakamdan Oluşmalıdır.")
elif(nIDN_Truth != 11):
  print("TC Kimlik numarasının Tüm Karakterleri Pozitif Tam Sayı Olmalıdır.")
else:
  print("TC Kimlik Doğrulama Başarısız.")

# the end
