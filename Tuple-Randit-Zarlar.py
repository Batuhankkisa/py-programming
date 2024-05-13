# soru 1
# {2: [(1,1)], 3: [(2,1), (1,2)], 4: [(1,3), (2,2), (3,1)], 5: [(1,4), (2,3), (3,2), (4,1)],

#yontem 1
MAX_ZAR_DEGERI = 6
MIN_ZAR_DEGERI = 1
zar_olasilik_sozluk = {}

for toplam_zar_degeri in range(2,13):
  zar_olasilik_sozluk[toplam_zar_degeri] = [] # Bos bir liste yaratalim

  for zar1 in range(1, min(MAX_ZAR_DEGERI+1, toplam_zar_degeri)):
    zar2 = toplam_zar_degeri - zar1
    if MIN_ZAR_DEGERI <= zar2 <= MAX_ZAR_DEGERI:
      # bu zar gecerlidir
      zar_olasilik_sozluk[toplam_zar_degeri].append((zar1, zar2))


print(zar_olasilik_sozluk)

#----------------------------------------------

#yontem 2
MAX_ZAR_DEGERI = 6
MIN_ZAR_DEGERI = 1
zar_olasilik_sozluk = {}

for zar1 in range(1,7):
  for zar2 in range(1,7):
    zar_toplami = zar1 + zar2

    if zar_toplami in zar_olasilik_sozluk.keys():
      # Daha onceden bu toplamda deger bulunmus
      zar_olasilik_sozluk[zar_toplami].append((zar1, zar2))
    else:
      zar_olasilik_sozluk[zar_toplami]=[(zar1, zar2)]


print(zar_olasilik_sozluk)

#-------------------------------------------
import random

zar1 = random.randint(1,6)
print("Ilk zar {} geldi".format(zar1))


zar2 = random.randint(1,6)
print("Ikinci zar {} geldi".format(zar2))

# Yontem 1 :
deger_listesi = list(zar_olasilik_sozluk.values())
anahtar_listesi = list(zar_olasilik_sozluk.keys())


indeks = -1
for i in range(len(deger_listesi)):
  if (zar1, zar2) in deger_listesi[i]:
    # Liste icerisinde bu ikiliyi bulduk
    indeks = i
    break

if indeks > 0:
  print("Yontem 1: {} ve {} ikilisi sozlukte arandiginda {} anahtari bulunmustur".format(zar1, zar2, anahtar_listesi[indeks]))
else:
  print("Bir hata olustu")


# Yontem 2 :

for anahtar, deger in zar_olasilik_sozluk.items():
  if (zar1, zar2) in deger:
    break
    # Bu sayede anahtar degeri guncellenmeyecektir ve son basarili deger ekrana basilabilir

print("Yontem 2: {} ve {} ikilisi sozlukte arandiginda {} anahtari bulunmustur".format(zar1, zar2, anahtar))

