def stok_listesi(input_listdict):
  ''' Icerisinde birden fazla satin alma kalemlerini liste icerisinde bulunduran 
  girdi degerinden, gerekli satinalma bilgisi ile toplam satinalmayi hesaplar.

  Disariya return ile olusturulan sozlugu verir

      @param input_listdict: Bir liste icerisinde girilen satinalma verilerini saklar. 
      Listenin icinde her bir eleman sozluk yapisindadir. 
      Sozlugun anahtarlari: cins ve miktar 
      Sozlugun degerleri ise bu anahtarlarin karsiligidir.

  '''
  toplam_sozluk = {}
  for siparis in input_listdict:
    # Once her bir elemani tek tek alalim
    # Burada siparis icerisinde iki anahtar var. Biri cins, digeri de miktar

      malzeme_cinsi = siparis['cins'] # Buraya kontrol eklememiz gerekir aslinda
      malzeme_miktari = siparis['miktar'] # Buraya kontrol eklememiz gerekir aslinda
      
      # Daha onceden toplam_sozluk icerisinde bu cins malzeme var miydi?
      if malzeme_cinsi not in toplam_sozluk:
        # Yoksa su anki malzeme miktari ile olusturalim:
        toplam_sozluk[malzeme_cinsi] = malzeme_miktari
      else:
        # Varsa ekleme yapalim
        toplam_sozluk[malzeme_cinsi] = toplam_sozluk[malzeme_cinsi] + malzeme_miktari

  return toplam_sozluk

test_stok =[
{'cins':'kalem', 'miktar':10},
{'cins':'defter', 'miktar':10},
{'cins':'kalem', 'miktar':10},
{'cins':'defter', 'miktar':10},
{'cins':'kalem', 'miktar':10} 
]

print(stok_listesi(test_stok))

