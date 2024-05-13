
class Product():

    def __init__(self, isim, tanim, marka, link, fiyat, kategori, stok):
        self.isim = isim
        self.tanim = tanim
        self.link = link
        self.marka = marka
        self.kategori = kategori
        
        if type(fiyat)==str or type(stok)==str:
            try:
                self.fiyat = float(fiyat) # Float yapisinda oldugundan emin olalim
                self.stok = int(stok) # int yapisinda oldugundan emin olalim
            except:
                raise Exception("Fiyat veya stok degiskenleri float/int yapisinda veya numerik string yapisinda olmalidir")

    def fiyat_arttir(self, artis_miktari):
        self.fiyat += artis_miktari
    
    def kampanya(self, yuzde):
        ''' Yapilan kampanya yuzdesi oraninda indirim yapar. Ornegin yuzde:10 indirim icin urun fiyati 0.9 ile carpilir
        '''
        self.fiyat *= (1-yuzde) 

    def __str__(self):
        return "{} : urun ismi {}, kategorisi {}, fiyati {}, kalan adet {}".format(self.model_id, self.isim, self.kategori, self.fiyat, self.stok)


class Butce():
    def __init__(self, isim, butce_limiti):
        self.isim = isim
        try:
            self.butce_limiti = float(butce_limiti)
        except:
            raise Exception("Butce limiti degeri numerik bir deger olmalidir")
        self.toplam_harcama = 0.0
        self.satin_alinanlar = []

    def urun_al(self, urun:Product, adet):
        if type(urun) != Product:
            raise Exception("Urun sinifindan bir deger ile cagirmalisiniz -> Beklenen {}, kullanilan {}".format(Product, type(urun)))
        self.satin_alinanlar.append(urun)
        self.toplam_harcama += urun.fiyat * adet
        # urun stoklarini degistirmek zorunde degilsiniz, fakat su sekilde yapilabilir
        urun.stok -= 1
        

    def kalan_yuzde_hesapla(self):
        return self.toplam_harcama / self.butce_limiti * 100

    def kalan_ekrana_bas(self):
        print("Butce ismi {}, toplam harcama miktari {}, kalan para {} ve harcama yuzdesi {}".format(
            self.isim, self.toplam_harcama, self.butce_limiti-self.toplam_harcama, self.kalan_yuzde_hesapla()))

