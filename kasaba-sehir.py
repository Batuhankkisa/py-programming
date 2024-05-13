def land_population(population, area):
  if population <= 0 or area <= 0:
    print("Populasayon ya da alan 0'dan kucuk olamaz. Population: {}, Area: {}".format(population, area))
    return

  if population < 20000:
    print("Populasyon: {}, ---- Kasaba".format(population))
    #print("Populasyon:", population, ", ----Kasaba")
  else:
    print("Populasyon: {}, ---- Sehir".format(population))

  arazi_yogunlugu = population / area # Burada area 0 degeri alabiliyor olsaydi hata alirdik
  if arazi_yogunlugu < 100:
    print("Arazi Yogunlugu: {}, ---- Nadiren Nufuslu".format(arazi_yogunlugu))
  else:
    print("Arazi Yogunlugu: {}, ---- Yogun Nufuslu".format(arazi_yogunlugu))

# Sehir, Nadir Testi
land_population(25000, 1000)

# 0'dan kucuk populasyon testi
land_population(-1, 1000)

# 0 area testi
land_population(25000, 0)

# Kasaba Nadir Testi
land_population(15000, 1000)

# Sehir Yogun Testi
land_population(25000, 100)