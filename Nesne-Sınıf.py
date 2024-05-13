
# Her iki yontem icin de tam puan alacaksiniz.

import math

# Yontem I (sinif tanimlarindaki printler sadece bilgilendirme icin)

class Point():
  print("Bos bir point nesnesi yaratiliyor")

class Ucgen():
  print("Bir ucgen nesnesi yaratiliyor")

class Dikdortgen():
  print("Bir dikdortgen nesnesi yaratiliyor")

class Daire():
  print("Bir daire nesnesi yaratiliyor")

# Simdi tanimlamalarimizin icini dolduralim:

nokta1, nokta2, nokta3 = Point(), Point(), Point()
nokta1.x = 0
nokta1.y = 0
nokta2.x = 0
nokta2.y = 10
nokta3.x = 5
nokta3.y = 5

ucgen_nesnesi = Ucgen()
ucgen_nesnesi.kose1 = nokta1 # Burada dikkatli olmak lazim, nokta 1 degistigi zaman ucgen.kose1 de degisecek
ucgen_nesnesi.kose2 = nokta2 # Burada dikkatli olmak lazim, nokta 2 degistigi zaman ucgen.kose2 de degisecek
ucgen_nesnesi.kose3 = nokta3 # Burada dikkatli olmak lazim, nokta 3 degistigi zaman ucgen.kose3 de degisecek

#Alternatif olarak:
ucgen_nesnesi2 = Ucgen()
ucgen_nesnesi2.kose1 = Point()
ucgen_nesnesi2.kose2 = Point()
ucgen_nesnesi2.kose3 = Point()

ucgen_nesnesi2.kose1.x, ucgen_nesnesi2.kose1.y = 0, 0
ucgen_nesnesi2.kose2.x, ucgen_nesnesi2.kose2.y = 0, 10
ucgen_nesnesi2.kose3.x, ucgen_nesnesi2.kose3.y = 5, 5

daire_nesnesi = Daire()
daire_nesnesi.merkez = nokta1 # Burada dikkatli olmak lazim, nokta 1 degistigi zaman daire_nesnesi.merkez de degisecek
daire_nesnesi.cember_noktasi = nokta2 # Burada dikkatli olmak lazim, nokta 1 degistigi zaman daire_nesnesi.merkez de degisecek


dikdortgen_nesnesi = Dikdortgen()
dikdortgen_nesnesi.nokta1, dikdortgen_nesnesi.nokta2 = Point(), Point()
dikdortgen_nesnesi.nokta3, dikdortgen_nesnesi.nokta4 = Point(), Point()
dikdortgen_nesnesi.nokta1.x, dikdortgen_nesnesi.nokta1.y = 0, 0
dikdortgen_nesnesi.nokta2.x, dikdortgen_nesnesi.nokta2.y = 0, 20
dikdortgen_nesnesi.nokta3.x, dikdortgen_nesnesi.nokta3.y = 10, 0
dikdortgen_nesnesi.nokta4.x, dikdortgen_nesnesi.nokta4.y = 10, 20
dikdortgen_nesnesi.width = 10
dikdortgen_nesnesi.height = 20


dikdortgen_nesnesi2 = Dikdortgen()
dikdortgen_nesnesi2.nokta1, dikdortgen_nesnesi2.nokta2 = Point(), Point()
dikdortgen_nesnesi2.nokta3, dikdortgen_nesnesi2.nokta4 = Point(), Point()
dikdortgen_nesnesi2.nokta1.x, dikdortgen_nesnesi2.nokta1.y = 0, 0
dikdortgen_nesnesi2.nokta2.x, dikdortgen_nesnesi2.nokta2.y = 0, 20
dikdortgen_nesnesi2.nokta3.x, dikdortgen_nesnesi2.nokta3.y = 10, 0
dikdortgen_nesnesi2.nokta4.x, dikdortgen_nesnesi2.nokta4.y = 10, 20


def distance(p1, p2):
  dist = math.sqrt(((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2))
  return dist


def findArea(nesne_girdisi):
  if isinstance(nesne_girdisi, Ucgen):
    area = 1/2 * abs((((nesne_girdisi.kose1.x * nesne_girdisi.kose2.y) 
    + (nesne_girdisi.kose2.x * nesne_girdisi.kose3.y)
    + (nesne_girdisi.kose3.x * nesne_girdisi.kose1.y)) 
    - ((nesne_girdisi.kose2.x * nesne_girdisi.kose1.y) + (nesne_girdisi.kose3.x
    * nesne_girdisi.kose2.y) + (nesne_girdisi.kose1.x * nesne_girdisi.kose3.y))))
    return area

  if isinstance(nesne_girdisi, Daire):
    dist =  distance(nesne_girdisi.merkez, nesne_girdisi.cember_noktasi)
    area = math.pi * (dist ** 2)
    return area

  
  if isinstance(nesne_girdisi, Dikdortgen):
    if hasattr(nesne_girdisi, 'width'):
      # Yontem1:
      area = nesne_girdisi.width * nesne_girdisi.height
      return area
    else:
    # Yontem2 (Eger width ve height tanimlanmadiysa:)
      x_uzunluklari = [ abs(nesne_girdisi.nokta1.x - nesne_girdisi.nokta2.x),
                      abs(nesne_girdisi.nokta2.x - nesne_girdisi.nokta3.x),
                      abs(nesne_girdisi.nokta3.x - nesne_girdisi.nokta4.x),
                      abs(nesne_girdisi.nokta4.x - nesne_girdisi.nokta1.x)]
      y_uzunluklari = [ abs(nesne_girdisi.nokta1.y - nesne_girdisi.nokta2.y),
                      abs(nesne_girdisi.nokta2.y - nesne_girdisi.nokta3.y),
                      abs(nesne_girdisi.nokta3.y - nesne_girdisi.nokta4.y),
                      abs(nesne_girdisi.nokta4.y - nesne_girdisi.nokta1.y)]

      width = max(x_uzunluklari)
      height = max(y_uzunluklari)
      area = width * height
      return area



print("Ucgen alani", findArea(ucgen_nesnesi))

print("Daire alani", findArea(daire_nesnesi))

print("Dikdortgen alani", findArea(dikdortgen_nesnesi))
print("Dikdortgen alani", findArea(dikdortgen_nesnesi2))

# Sinif Tanimlama Yontem 2 (init ve str fonksiyonlari kullanarak):

class Point_2():
  print("Bos bir point nesnesi yaratiliyor")

  def __init__(self, x = 0, y = 0):
    print('x ve y degerleri dolduruluyor, [{}, {}]'.format(x, y))
    self.x = x
    self.y = y

  def __str__(self):
    return "({},{})".format(self.x, self.y)

class Ucgen_2():
  print("Bir ucgen nesnesi yaratiliyor")

  def __init__(self, point1, point2, point3):
    print('Ucgen dolduruluyor, [{}, {}, {}]'.format(point1,point2,point3))
    self.kose1 = point1
    self.kose2 = point2
    self.kose3 = point3

  def __str__(self):
    return "Ucgen Noktalari : (Point1 {} , (Point2 {} , (Roof {}".format(self.kose1, self.kose2, self.kose3)

class Dikdortgen_2():
  print("Bir dikdortgen nesnesi yaratiliyor")

  def __init__(self, point1, point2, point3, point4):
    print('Dikdortgen dolduruluyor, [{}, {}, {}, {}]'.format(point1,point2,point3, point4))
    self.nokta1 = point1
    self.nokta2 = point2
    self.nokta3 = point3
    self.nokta4 = point4

  def __str__(self):
    return "Dikdortgen, Kose Noktalari: {}, {}, {}, {}".format(self.nokta1, self.nokta2, self.nokta3, self.nokta4)


class Daire_2():
  print("Bir daire nesnesi yaratiliyor")
  def __init__(self, point1, point2):
    print('Daire dolduruluyor, [{}, {}]'.format(point1,point2))
    self.merkez = point1
    self.cember_noktasi = point2

  def __str__(self):
    return "Daire, Merkez {}, Cember Noktasi {} ".format(self.merkez, self.cember_noktasi)


nokta_dene=Point_2(10,0)
print(nokta_dene)

ucgen_nesnesi = Ucgen_2 (Point_2(0,0), Point_2(0,10), Point_2(5,5))

dikdortgen_nesnesi = Dikdortgen_2 (Point_2(0,0), Point_2(0,20), Point_2(10,20) , Point_2(10,0))

daire_nesnesi = Daire_2 (Point_2(0,0), Point_2(0,10))

print(ucgen_nesnesi)

print(dikdortgen_nesnesi)

print(daire_nesnesi)



def findArea(nesne_girdisi):
  if isinstance(nesne_girdisi, Ucgen_2):
    area = 1/2 * abs((((nesne_girdisi.kose1.x * nesne_girdisi.kose2.y) 
    + (nesne_girdisi.kose2.x * nesne_girdisi.kose3.y)
    + (nesne_girdisi.kose3.x * nesne_girdisi.kose1.y)) 
    - ((nesne_girdisi.kose2.x * nesne_girdisi.kose1.y) + (nesne_girdisi.kose3.x
    * nesne_girdisi.kose2.y) + (nesne_girdisi.kose1.x * nesne_girdisi.kose3.y))))
    return area

  if isinstance(nesne_girdisi, Daire_2):
    dist =  distance(nesne_girdisi.merkez, nesne_girdisi.cember_noktasi)
    area = math.pi * (dist ** 2)
    return area

  
  if isinstance(nesne_girdisi, Dikdortgen_2):
    if hasattr(nesne_girdisi, 'width'):
      # Yontem1:
      area = nesne_girdisi.width * nesne_girdisi.height
      return area
    else:
    # Yontem2 (Eger width ve height tanimlanmadiysa:)
      x_uzunluklari = [ abs(nesne_girdisi.nokta1.x - nesne_girdisi.nokta2.x),
                      abs(nesne_girdisi.nokta2.x - nesne_girdisi.nokta3.x),
                      abs(nesne_girdisi.nokta3.x - nesne_girdisi.nokta4.x),
                      abs(nesne_girdisi.nokta4.x - nesne_girdisi.nokta1.x)]
      y_uzunluklari = [ abs(nesne_girdisi.nokta1.y - nesne_girdisi.nokta2.y),
                      abs(nesne_girdisi.nokta2.y - nesne_girdisi.nokta3.y),
                      abs(nesne_girdisi.nokta3.y - nesne_girdisi.nokta4.y),
                      abs(nesne_girdisi.nokta4.y - nesne_girdisi.nokta1.y)]

      width = max(x_uzunluklari)
      height = max(y_uzunluklari)
      area = width * height
      return area



print("Ucgen alani", findArea(ucgen_nesnesi))

print("Daire alani", findArea(daire_nesnesi))

print("Dikdortgen alani", findArea(dikdortgen_nesnesi))