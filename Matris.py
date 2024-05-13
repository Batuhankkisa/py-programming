# Soru 1:
# Sadece liste kullanarak
def sparsify(liste_in):
  sparse_list = []
  for satir_index in range(len(liste_in)):
    for sutun_index in range(len(liste_in[0])):
      deger = liste_in[satir_index][sutun_index]
      if deger != 0:
        sparse_list.append([satir_index, sutun_index, deger])
  return sparse_list

liste_in = [[1, 0, 3], [2, 0, 0] , [0, 0, 5] ]
spars_list = sparsify(liste_in)
print(spars_list)

# Soru 1:
# Icice iki tane dict kullanarak 
def sparsify_2(liste_in):
  sparse_list = dict()
  for satir_index in range(len(liste_in)):
    for sutun_index in range(len(liste_in[0])):
      deger = liste_in[satir_index][sutun_index]
      if deger != 0:
        sparse_list.setdefault(satir_index, dict())
        sparse_list[satir_index].setdefault(sutun_index, dict())
        sparse_list[satir_index][sutun_index] = deger        
  return sparse_list

liste_in = [[1, 0, 3], [2, 0, 0] , [0, 0, 5] ]
spars_list_2 = sparsify_2(liste_in)
print(spars_list_2)

# Soru 1:
# tuple ve dict kullanarak
def sparsify_3(liste_in):
  sparse_list = dict()
  for satir_index in range(len(liste_in)):
    for sutun_index in range(len(liste_in[0])):
      deger = liste_in[satir_index][sutun_index]
      if deger != 0:
        sparse_list[(satir_index, sutun_index)] = deger        
  return sparse_list

liste_in = [[1, 0, 3], [2, 0, 0] , [0, 0, 5] ]
spars_list_3 = sparsify_3(liste_in)
print(spars_list_3)





# Soru 2:
# Icice iki tane dict kullanarak 
# matris boyutu disaridan verildiginde (lab calismasindaki gibi)
def desparsify_2(dict_in, matrix_boyutu):
  # 0 degerli bos icice liste yaratalim
  buyuk_liste = []
  for sutun in range(matrix_boyutu):
    buyuk_liste.append([0]*matrix_boyutu) # satir sayisi kadar GERCEK kopyalama lazim

  # Get maximum index numbers first:
  for satir_index, sutun in dict_in.items():
    for sutun_index, deger in sutun.items():
      buyuk_liste[satir_index][sutun_index] = deger

  return buyuk_liste

normal_list_2 = desparsify_2(spars_list_2, 3)
print(normal_list_2)

# Soru 2:
# Tuple ve dict kullanarak 
# matris boyutu disaridan verildiginde (lab calismasindaki gibi)
def desparsify_3(dict_in, matrix_boyutu):
  
  # 0 degerli bos icice liste yaratalim
  buyuk_liste = []
  for sutun_sayisi in range(matrix_boyutu):
    buyuk_liste.append([0]*matrix_boyutu) # satir sayisi kadar GERCEK kopyalama lazim

  for satir_sutun, deger in dict_in.items():
    buyuk_liste[satir_sutun[0]][satir_sutun[1]] = deger
  return buyuk_liste
  


print(spars_list_3)
normal_list_3 = desparsify_3(spars_list_3, 3)
print(normal_list_3)

