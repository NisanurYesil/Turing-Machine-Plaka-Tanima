class TuringMakinesi:
    def __init__(self, girdi):
        self.bant = list(girdi) + ['_']
        self.kafa = 0
        self.durum = 'q0'
        self.gecisler = self._gecis_tablosunu_olustur()

    def _gecis_tablosunu_olustur(self):
        tablo = {}
        rakamlar = "0123456789"
        harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for r in rakamlar: tablo[('q0', r)] = ('q1', r, 'R')
        for r in rakamlar: tablo[('q1', r)] = ('q2', r, 'R')
        for h in harfler: tablo[('q2', h)] = ('q3', h, 'R')
        for h in harfler: tablo[('q3', h)] = ('q4', h, 'R')
        for r in rakamlar: tablo[('q4', r)] = ('q5', r, 'R')
        for r in rakamlar: tablo[('q5', r)] = ('q6', r, 'R')
        for r in rakamlar: tablo[('q6', r)] = ('q7', r, 'R')
        tablo[('q7', '_')] = ('KABUL', '_', 'S') 
        
        return tablo

    def calistir(self):
        print("\n--- Turing Makinesi Simülasyonu Başlıyor ---\n")
        
        while self.durum not in ['KABUL', 'RED']:
            if self.kafa < len(self.bant):
                okunan_sembol = self.bant[self.kafa]
            else:
                okunan_sembol = '_'

            gosterilen_sembol = "boşluk" if okunan_sembol == '_' else okunan_sembol

            if (self.durum, okunan_sembol) in self.gecisler:
                yeni_durum, yazilan_sembol, yon = self.gecisler[(self.durum, okunan_sembol)]
            else:
                yeni_durum, yazilan_sembol, yon = 'RED', okunan_sembol, 'S'

            # Bant içeriğini kafanın olduğu yeri [ ] içine alarak hazırla
            bant_gosterimi = ""
            for i, char in enumerate(self.bant):
                if i == self.kafa:
                    bant_gosterimi += f"[{char}]"
                else:
                    bant_gosterimi += char
            
            yon_metni = 'Sağ (R)' if yon == 'R' else 'Dur (S)'

            print(f"Mevcut Durum: {self.durum:<5} | Okunan Sembol: {gosterilen_sembol:<6} | Kafa Hareketi: {yon_metni:<7} | Bant İçeriği: {bant_gosterimi}")

            self.bant[self.kafa] = yazilan_sembol
            self.durum = yeni_durum

            if yon == 'R':
                self.kafa += 1
            elif yon == 'L':
                self.kafa -= 1

        print(f"\nSonuç: {self.durum}")
        if self.durum == 'KABUL':
            print("Plaka formatı GEÇERLİ.")
        else:
            print("Plaka formatı GEÇERSİZ!")

if __name__ == "__main__":
    plaka_girdisi = input("Lütfen kontrol edilecek plakayı giriniz: ")
    plaka_girdisi = plaka_girdisi.strip() 
    
    makine = TuringMakinesi(plaka_girdisi)
    makine.calistir()