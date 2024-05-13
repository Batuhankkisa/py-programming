import math

def oklit_mesafesi(px,py,qx,qy):
  x_farki = (px-qx)**2
  y_farki = (py-qy)**2

  return math.sqrt(x_farki + y_farki)


px = 7
py = 5
qx = 4
qy = 1
# Qy Qx'den kucuk testi
print("Oklit Mesafesi px:{}, py:{}, qx:{}, qy:{} Sonucu {} ".format(px, py, qx, qy, oklit_mesafesi(px, py, qx, qy)) )

px = 7
py = 5
qx = 6
qy = 10
# Qy Qx'den buyuk testi
print("Oklit Mesafesi px:{}, py:{}, qx:{}, qy:{} Sonucu {} ".format(px, py, qx, qy, oklit_mesafesi(px, py, qx, qy)) )

px = 7
py = 15
qx = 6
qy = 10
# Py Px'den buyuk testi
print("Oklit Mesafesi px:{}, py:{}, qx:{}, qy:{} Sonucu {} ".format(px, py, qx, qy, oklit_mesafesi(px, py, qx, qy)) )

px = 7
py = 0
qx = 6
qy = 0
# 0 testleri
print("Oklit Mesafesi px:{}, py:{}, qx:{}, qy:{} Sonucu {} ".format(px, py, qx, qy, oklit_mesafesi(px, py, qx, qy)) )

px = 0
py = 0
qx = 6
qy = 10
# 0 testleri
print("Oklit Mesafesi px:{}, py:{}, qx:{}, qy:{} Sonucu {} ".format(px, py, qx, qy, oklit_mesafesi(px, py, qx, qy)) )

px = 0
py = 0
qx = 0
qy = 0
# 0 testleri
print("Oklit Mesafesi px:{}, py:{}, qx:{}, qy:{} Sonucu {} ".format(px, py, qx, qy, oklit_mesafesi(px, py, qx, qy)) )

## Alternatif olarak:
print("Oklit Mesafesi Sonucu ", oklit_mesafesi(2, 2, 5, 6))
print("Oklit Mesafesi Sonucu ", oklit_mesafesi(10, 20, 0, 20))
print("Oklit Mesafesi Sonucu ", oklit_mesafesi(0, 0, 30, 20)) 
print("Oklit Mesafesi Sonucu ", oklit_mesafesi(10, 40, 60, 70))

