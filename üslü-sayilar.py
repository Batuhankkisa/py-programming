
# Yontem 1
def ussuMu(sayi1, sayi2):
  if sayi1 == 1:
    return True

  return sayi1 % sayi2 == 0 and ussuMu(sayi1/sayi2, sayi2)

print(ussuMu(15, 3))
print(ussuMu(16, 3))
print(ussuMu(81, 3))
print(ussuMu(16, 4))
print(ussuMu(4, 4))

# Yontem 2 
def ussuMu(sayi1, sayi2):

  # Baz Durumu: 1 e kadar basari ile bolduysek ussudur
  if sayi1 == 1:
    return True

  # Kendi sorumlulugumuz: Herhangi bir carpan 3'e tam bolunmuyorsa ussu degildir
  if sayi1 % sayi2 != 0:
    return False
  
  # Sorunun kalanini ozyinelemeli kisima delege ediyoruz 
  return ussuMu(sayi1/sayi2, sayi2)

print(ussuMu(15, 3))
print(ussuMu(16, 3))
print(ussuMu(81, 3))
print(ussuMu(16, 4))
print(ussuMu(4, 4))



def recurse(n, s):
  ''' Bu fonksiyon verilen n sayısına kadar olan sayıları toplar ve s sayısına ekler. n sayısı 0'dan buyuk olmalıdır.
  '''
  if n == 0:
    print(s)
  else:
   recurse(n-1, n+s)

recurse(5, 10)

