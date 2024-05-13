
def faktorial(n):
  if n < 0:
    print("Sadece pozitif sayilar gecerlidir")
    return -1 
  
  fakt = 1
  if n<2:
    return fakt
  else:
    for i in range(1,n+1):
      fakt = fakt*i
  return fakt

test_sayisi = 0
print(test_sayisi, "sayisinin faktoriyeli: {}".format(faktorial(test_sayisi)))

test_sayisi = 1
print(test_sayisi, "sayisinin faktoriyeli: {}".format(faktorial(test_sayisi)))

test_sayisi = 2
print(test_sayisi, "sayisinin faktoriyeli: {}".format(faktorial(test_sayisi)))

test_sayisi = 3
print(test_sayisi, "sayisinin faktoriyeli: {}".format(faktorial(test_sayisi)))

test_sayisi = 5
print(test_sayisi, "sayisinin faktoriyeli: {}".format(faktorial(test_sayisi)))

test_sayisi = -1
print(test_sayisi, "sayisinin faktoriyeli: {}".format(faktorial(test_sayisi)))

