
# Soru 1:

def odev3_soru1(girdi):
  kelimeler = girdi.split()
  return len(kelimeler[len(kelimeler)-1])

print(odev3_soru1("Bu bir deneme cumlesidir"))
print(odev3_soru1("Bu bir deneme cumlesidir    "))
print(odev3_soru1("Bu bir deneme"))

# Soru 2:

def odev3_soru2_yontem1(girdi):
  out_text = ""
  for eleman in girdi:
    if eleman == '0':
      out_text += 'a'
    if eleman == '1':
      out_text += 'b'
    if eleman == '2':
      out_text += 'c'
    if eleman == '3':
      out_text += 'd'
    if eleman == '4':
      out_text += 'e'
    if eleman == '5':
      out_text += 'f'
    if eleman == '6':
      out_text += 'g'
    if eleman == '7':
      out_text += 'h'
    if eleman == '8':
      out_text += 'i'
    if eleman == '9':
      out_text += 'j'
  return out_text
print(odev3_soru2_yontem1('152'))
print(odev3_soru2_yontem1('15241242'))
print(odev3_soru2_yontem1('0123456789'))

def odev3_soru2_yontem2(girdi):
  print(ord('0'), ord('9'), ord('a'), ord('k'))
  #0 -> 48
  #a -> 97
  
  out_text = ""
  for eleman in girdi:
    number = ord(eleman) + 97 - 48
    out_text += chr(number)
  return out_text

print(odev3_soru2_yontem2('152'))
print(odev3_soru2_yontem2('15241242'))
print(odev3_soru2_yontem2('0123456789'))

def odev3_soru2_yontem3(girdi):
  convertor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
  
  out_text = ""
  for eleman in girdi:
    sayisal_deger = int(eleman)  # Girdi her zaman 0-9 arasi olacak
    out_text += convertor[sayisal_deger]
  return out_text

print(odev3_soru2_yontem3('152'))
print(odev3_soru2_yontem3('15241242'))
print(odev3_soru2_yontem3('123456789'))

# Soru 3:


def odev3_soru3_deneme(girdi):
  for eleman in girdi:
    print(eleman, 'Lower', eleman.islower())
    print(eleman, 'Digit', eleman.isdigit())
    print(eleman, 'Upper', eleman.isupper())
    print("----")

odev3_soru3("Bunu Dene 1")

def odev3_soru3(girdi):
  buyuk_harfler = ''
  kucuk_harfler = ''
  sayilar = ''
  for eleman in girdi:
    if eleman.islower():
      kucuk_harfler += eleman
    if eleman.isupper():
      buyuk_harfler += eleman
    if eleman.isdigit():
      sayilar += eleman
  
  return buyuk_harfler + kucuk_harfler + sayilar

print(odev3_soru3("Bunu Dene 1"))
print(odev3_soru3("Programlama Temelleri 1"))
print(odev3_soru3("bunuDeNeMeliyim"))
print(odev3_soru3("yAS21OkuL4"))
print(odev3_soru3("Bazen Farkli Cumleler Gelebilir"))

