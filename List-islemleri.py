#-------------------------------------------------------------
isimler = ['Duman', 'Roket', 'Boncuk', 'Pamuk', 'Miyav']
renkler = ['Gri', 'Gri', 'Sari', 'Beyaz', 'Siyah']
yaslar = [2, 2, 5, 4, 3]

min_len = min(len(isimler), len(renkler), len(yaslar))

for i in range(min_len):
  print("{} {} renklidir ve {} yasindadir".format(isimler[i], renkler[i].lower(), yaslar[i]))

#-------------------------------------------------------------
def elemanlari_gez(liste_in):
  for satir_index in range(len(liste_in)):
    for sutun_index in range(len(liste_in[0])):
      print(liste_in[satir_index][sutun_index])
  return satir_index+1 

test_listesi = [[1,2,3], [4,5,6], [7,8,9]]
satir_sayisi = elemanlari_gez(test_listesi)
print(satir_sayisi)

#-------------------------------------------------------------

def kumeye_donustur(liste_in):
  yeni_liste = []
  for eleman in liste_in:
    if not eleman in yeni_liste:
      yeni_liste.append(eleman)
  return yeni_liste


input_liste = ['yaz', 2, '103', 2, 'program', 3, 5, 'd', 0, '203', 'program', 5, 5]

kume_liste = kumeye_donustur(input_liste)
print(kume_liste)

