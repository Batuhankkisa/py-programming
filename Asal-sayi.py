
def asal_sayi_bul(n):
  if n < 1:
    print("Sadece pozitif sayilar icin gecerlidir.")
    return False

  for i in range(2,n):
    if n % i == 0:
      # Tam olarak bolunuyorsa asal sayi degildir
      return False
  
  # Eger hic bir sayi tam olarak bolunmuyorsa asal sayidir
  # 1 i ayri kontrol etmeye gerek yok - Yukaridaki for dongusune girmeyecektir n=1
  return True

deneme_sayisi = 0
print(deneme_sayisi, asal_sayi_bul(deneme_sayisi))

deneme_sayisi = 1
print(deneme_sayisi, asal_sayi_bul(deneme_sayisi))

deneme_sayisi = 2
print(deneme_sayisi, asal_sayi_bul(deneme_sayisi))

deneme_sayisi = 4
print(deneme_sayisi, asal_sayi_bul(deneme_sayisi))

deneme_sayisi = 6
print(deneme_sayisi, asal_sayi_bul(deneme_sayisi))

deneme_sayisi = 9
print(deneme_sayisi, asal_sayi_bul(deneme_sayisi))

deneme_sayisi = 19
print(deneme_sayisi, asal_sayi_bul(deneme_sayisi))

deneme_sayisi = -10
print(deneme_sayisi, asal_sayi_bul(deneme_sayisi))

