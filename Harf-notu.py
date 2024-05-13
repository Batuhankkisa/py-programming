#Soru 2:

def harf_notu_hesaplama(lab, odev , arasinav, final):
  if not( 0 <= lab <= 100  and 0 <= odev <= 100 and 0 <= arasinav <= 100 and 0 <= final <= 100):
    # Bunu farkli bir suru sekilde de yazabilirdik, sadece 0'dan buyuk olmayi kontrol ettiyseniz de olur!
    print("Yanlis bir deger girdiniz, sinav sonuclari 0'dan kucuk veya 100'den buyuk olamaz: lab: {}, odev: {}, arasinav: {}, final: {}".format(lab, odev, arasinav, final))
    return

  agirlikli_ortalama = 0.15 * odev + 0.2*lab + 0.25*arasinav + 0.4*final

  if agirlikli_ortalama > 90:
    harf_notu = 'A'
  elif agirlikli_ortalama > 75:
    harf_notu = 'B'
  elif agirlikli_ortalama > 60:
    harf_notu = 'C'
  elif agirlikli_ortalama > 45:
    harf_notu = 'D'
  else:
    harf_notu = 'F'

  print('Programlama Temelleri I Dersi, Ogrenci No: 0000000000, Ağırlıklı Ortalama: {}, Harf Notu: {}'.format(agirlikli_ortalama, harf_notu))
  return harf_notu

harf_notu_hesaplama(90, 90 , 100, 100)

harf_notu_hesaplama(90, 90 , 40, 100)

harf_notu_hesaplama(90, 90 , 40, 60)

harf_notu_hesaplama(90, 90 , 40, 20)

harf_notu_hesaplama(90, 90 , 20, 20)

harf_notu_hesaplama(90, 90 , -1, 100)

harf_notu_hesaplama(90, 90 , 0, 120)
