# -*- coding: utf-8 -*-
import math

def kup(kenar_uzunluk):
  ''' Verilen kenar_uzunluk degeri icin kup cisminin hacmini ve yuzey alanini hesaplar, yuzey alanini geri dondurur.
  '''
  if kenar_uzunluk < 0:
    print("Uzunluk degeri sifirdan kucuk olamaz")
    return -1

  hacim = kenar_uzunluk**3
  yuzey_alani = 6 * (kenar_uzunluk * kenar_uzunluk)

 
  print("Kupun Hacmi: {}".format(hacim))
  # -- Fonksiyonu cagirirken: print("Kupun Yuzey alani: {}".format(kup(6)))


  # print("Kupun Hacmi: {}".format(hacim))
  # print("Kupun Yuzey alani: {}".format(yuzey_alani))

  # - Ya da:
  # - print("Kupun hacmi: {} \nKupun Yuzey alani:{}".format(hacim,yuzey_alani))

  return yuzey_alani

def dikdortgenler_primasi(kenar1,kenar2,kenar3):
  ''' Verilen kenar1, kenar2 ve kenar3 degerleri icin dikdortgenler prizmasi cisminin hacmini ve yuzey alanini hesaplar, yuzey alanini geri dondurur.
  '''
  if kenar1 < 0 or kenar2 < 0 or kenar3 < 0:
    print("Uzunluk degeri sifirdan kucuk olamaz")
    return -1

  hacim = kenar1 * kenar2 * kenar3
  yuzey_alani = 2 * (kenar1*kenar2 + kenar1*kenar3 + kenar3*kenar2)

  print("Dikdortgen Prizmasinin Hacmi: {}".format(hacim))
  return yuzey_alani


def piramit(l, w, h):
  ''' Verilen kenar1, kenar2 ve yukseklik degerleri icin dikdortgenler prizmasi cisminin hacmini ve yuzey alanini hesaplar, yuzey alanini geri dondurur.

      @params l: Piramit baz ucgen uzunlugu
      @params w: Piramit baz ucgen genisligi
      @params h: Piramit yuksekligi
  '''
  if l < 0 or w < 0 or h < 0:
    print("Uzunluk degeri sifirdan kucuk olamaz")
    return -1

  hacim = l * w * h / 3
  yuzey_alani= l * math.sqrt((w/2)**2 + h**2) + w * math.sqrt((l/2)**2 + h**2) + l*w
  

  print("Piramit Prizmasinin Hacmi: {}".format(hacim))
  return yuzey_alani


def silindir(r, h):
  ''' Verilen yaricap ve yukseklik degerleri icin silindir cisminin hacmini ve yuzey alanini hesaplar, yuzey alanini geri dondurur.

    @params r: Silindir yaricapi
    @params h: Silindir yuksekligi
  '''
  if r < 0 or h < 0:
    print("Uzunluk degeri sifirdan kucuk olamaz")
    return -1
  hacim = math.pi * r**2 * h
  yuzey_alani = 2*math.pi * r**2 + 2*math.pi*r*h
  print("Silindir Hacmi: {}".format(hacim))
  return yuzey_alani

def kure(yaricap):
  ''' Verilen yaricap degeri icin kure cisminin hacmini ve yuzey alanini hesaplar, yuzey alanini geri dondurur.
  '''
  if yaricap < 0:
    print("Uzunluk degeri sifirdan kucuk olamaz")
    return -1

  hacim = 4 * math.pi * yaricap**3 / 3
  yuzey_alani = 4 * math.pi * yaricap**2

  print("Kurenin Hacmi: {}".format(hacim))
  return yuzey_alani

k = kup(10)
if k >= 0:
  print ("Kupun Yuzey Alani : {}".format(k))

k = kup(-10)
if k >= 0:
  print ("Kupun Yuzey Alani : {}".format(k))

k = kup(0)
if k >= 0:
  print ("Kupun Yuzey Alani : {}".format(k))

print('-' * 50)

d = dikdortgenler_primasi(3,4, 5)
if d >= 0:
  print ("Dikdortgen Prizmasinin Yuzey Alani : {}".format(d))

d = dikdortgenler_primasi(1,20, -5)
if d >= 0:
  print ("Dikdortgen Prizmasinin Yuzey Alani : {}".format(d))

d = dikdortgenler_primasi(10,0, 5)
if d >= 0:
  print ("Dikdortgen Prizmasinin Yuzey Alani : {}".format(d))
print('-' * 50)


p = piramit(3,4,8)
if p >= 0:
  print ("Piramit Yuzey Alani : {}".format(p))

p = piramit(4,0,6)
if p >= 0:
  print ("Piramit Yuzey Alani : {}".format(p))

p = piramit(4,-6,8)
if p >= 0:
  print ("Piramit Yuzey Alani : {}".format(p))

print('-' * 50)

s = silindir(400,8)
if s >= 0:
  print ("Silindir Yuzey Alani : {}".format(s))

s = silindir(0,8)
if s >= 0:
  print ("Silindir Yuzey Alani : {}".format(s))

s = silindir(4,-8)
if s >= 0:
  print ("Silindir Yuzey Alani : {}".format(s))



print('-' * 50)

c = kure(1000000000)
if c >= 0:
  print ("Kure Yuzey Alani : {}".format(c))

c = kure(0)
if c >= 0:
  print ("Kure Yuzey Alani : {}".format(c))

c = kure(-5)
if c >= 0:
  print ("Kure Yuzey Alani : {}".format(c))
