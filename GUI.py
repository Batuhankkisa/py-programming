import tkinter.filedialog as fd
import tkinter as tk
import json
 
class VisualInterface(tk.Frame):
    
    def __init__(self, parent):
        self.parent = parent
        self.harcamalar = {}
        self.frame = tk.Frame(self.parent)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.initUI()
        
    def initUI(self):
        
        self.lb = tk.Listbox(self.frame, selectmode="single")
        self.lb.pack(fill=tk.BOTH, expand=True)
 
        self.buton_ekle = tk.Button(self.frame, text="Aktar", command = self.liste_olustur)
        self.buton_secilisil = tk.Button(self.frame, text="Secili Sil", command = self.secili_sil)
        self.buton_hepsinisil = tk.Button(self.frame, text="Hepsini Sil", command = self.tumunu_sil)
        self.buton_ekle.pack(side=tk.LEFT)
        self.buton_secilisil.pack(side=tk.LEFT)
        self.buton_hepsinisil.pack(side=tk.LEFT)
 
    def liste_olustur(self):
        self.liste_eleman_ekle()
        self.lb.pack(expand=True)
 
    def liste_eleman_ekle(self):
        file_name = fd.askopenfilename()
        harcamalar = self.urunleri_oku(file_name)
        for indeks, harcama in enumerate(harcamalar):
            self.harcamalar[indeks] = harcama
            self.lb.insert(indeks, harcama)
 
    def secili_sil(self):
        selected_indeks = self.lb.curselection()[0]
        try:
            self.harcamalar.pop(selected_indeks)
            self.lb.delete(selected_indeks)
        except KeyError as e:
            print(e)
        
 
    def tumunu_sil(self):
        self.lb.delete(0, tk.END)
        self.harcamalar.clear()

    def urunleri_oku(self, dosya_ismi):
        file = open(dosya_ismi, 'r')
        urunler = json.load(file)
        urun_listesi = []
        # Burada urun sinifini ve __str__ kodlarini da kullanabilirdik.
        for satir in urunler:
            p = "Kategori: {} | {} - {}, {}TL, stok: {}".format(satir['kategori'],
                satir['isim'], satir['marka'], satir['fiyat'], satir['stok'])
            urun_listesi.append(p)
        return urun_listesi
        
            
 

    
 
 
 
 
 
 
 
 