# Soru 1:
def kitap_histogram(string_inputu, sozluk_in):

    # burada histogram hesap edilecek
    for kelime in string_inputu:
        if kelime not in sozluk_in.keys():
            sozluk_in[kelime] = 1
        else:
            sozluk_in[kelime] +=1

    # Gercekten return etmemiz gerekir mi? 
    # Sozluk degiskenini fonksiyon icersinde degistirebiliyor muyuz?
    return sozluk_in


def dosya_okuma(dosya_ismi):
    sozluk = {}
    # Once dosya okuma islemleri gelecek
    fin = open(dosya_ismi, encoding='utf-8')
    for satir in fin:
        kelimeler_listesi = satir.strip().split()
        # burada histogram hesap edilecek
        # Burada ozellikle biraz gereksiz bir islem yapiyoruz!
        # alternatif olarak (kitap_histogram(kelimeler_listesi, sozluk)) de yazabilirdik. Neden?
        sozluk = kitap_histogram(kelimeler_listesi, sozluk)

    return sozluk




print('-' * 40)
word_hist = dosya_okuma('words.txt')
kitap_hist = dosya_okuma('pg67101.txt')


# Soru 2:
def subtract(sozluk1, sozluk2):
    res = dict()
    for key in sozluk1:
        if key not in sozluk2:
            res[key] = sozluk1[key]
    return res

sonuc = subtract(word_hist, kitap_hist)
for i in range(30):
    print(list(sonuc.items())[i])