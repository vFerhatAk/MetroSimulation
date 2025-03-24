from collections import deque

class Istasyon:
    def __init__(self, idx, ad, hatlar):
        self.idx = idx
        self.ad = ad
        self.hatlar = hatlar  # Bu istasyonun bulunduğu hatlar
        self.komsular = []  # Bağlantılı olduğu komşu istasyonlar

    def bagla(self, komsu_istasyon, sure):
        """Komşu istasyonla bağlantı kur"""
        self.komsular.append((komsu_istasyon, sure))

class Metro:
    def __init__(self):
        self.istasyonlar = {}
        self.hatlar = {}

    def istasyon_ekle(self, idx, ad, hatlar):
        self.istasyonlar[idx] = Istasyon(idx, ad, hatlar)

    def hat_ekle(self, hat_ad, istasyonlar):
        self.hatlar[hat_ad] = istasyonlar
        for istasyon in istasyonlar:
            istasyon.hatlar.append(hat_ad)

    def baglantilari_ekle(self, istasyon1, istasyon2, sure):
        """İki istasyon arasına bağlantı ekler"""
        istasyon1.bagla(istasyon2, sure)
        istasyon2.bagla(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id, hedef_id):
        """En az aktarmalı rotayı bulmak için BFS algoritması"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # BFS başlatıyoruz
        queue = deque([(baslangic, [], 0)])  # (istasyon, rota, aktarma sayısı)
        visited = set()  # Ziyaret edilen istasyonlar
        
        while queue:
            current_istasyon, rota, aktarma_sayisi = queue.popleft()
            
            # Eğer hedefe ulaşıldıysa, rotayı döndür
            if current_istasyon.idx == hedef_id:
                return rota + [current_istasyon.ad]

            if current_istasyon.idx not in visited:
                visited.add(current_istasyon.idx)

                for komsu, sure in current_istasyon.komsular:
                    # Eğer komşu istasyon daha önce ziyaret edilmemişse
                    if komsu.idx not in visited:
                        yeni_aktarma_sayisi = aktarma_sayisi
                        
                        # Aktarma yapılıp yapılmadığını kontrol et
                        if not any(hat in komsu.hatlar for hat in current_istasyon.hatlar):
                            yeni_aktarma_sayisi += 1
                        
                        queue.append((komsu, rota + [current_istasyon.ad], yeni_aktarma_sayisi))
                        
        return None  # Eğer rota bulunamadıysa

    def en_hizli_rota_bul(self, baslangic_id, hedef_id):
        """En hızlı rotayı bulmak için basit BFS"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # BFS başlatıyoruz
        queue = deque([(baslangic, 0, [baslangic.ad])])  # (istasyon, toplam süre, rota)
        visited = set()  # Ziyaret edilen istasyonlar
        
        while queue:
            current_istasyon, sure, rota = queue.popleft()

            if current_istasyon.idx == hedef_id:
                # Rotayı bulduk, geri döndürüyoruz
                return rota, sure

            visited.add(current_istasyon.idx)

            for komsu, komsu_sure in current_istasyon.komsular:
                if komsu.idx not in visited:
                    queue.append((komsu, sure + komsu_sure, rota + [komsu.ad]))

        return None

# Metro sistemini kurma
metro = Metro()

# İstasyonlar
# M1 hattı (Aksaray - Yenikapı)
metro.istasyon_ekle("M1A1", "Yenikapı", ["M1"])
metro.istasyon_ekle("M1A2", "Vezneciler", ["M1"])
metro.istasyon_ekle("M1A3", "Aksaray", ["M1"])
metro.istasyon_ekle("M1A4", "İstanbul Üniversitesi", ["M1"])

# M2 hattı (Şişhane - Hacıosman)
metro.istasyon_ekle("M2A1", "Taksim", ["M2"])
metro.istasyon_ekle("M2A2", "Şişhane", ["M2"])
metro.istasyon_ekle("M2A3", "Osmanbey", ["M2"])
metro.istasyon_ekle("M2A4", "Hacıosman", ["M2"])

# M3 hattı (Beylikdüzü - Mahmutbey)
metro.istasyon_ekle("M3A1", "Beylikdüzü", ["M3"])
metro.istasyon_ekle("M3A2", "Marmara Park", ["M3"])
metro.istasyon_ekle("M3A3", "Mahmutbey", ["M3"])

# M4 hattı (Kadıköy - Tavşancık)
metro.istasyon_ekle("M4A1", "Kadıköy", ["M4"])
metro.istasyon_ekle("M4A2", "Ayrılık Çeşmesi", ["M4"])
metro.istasyon_ekle("M4A3", "Tavşancık", ["M4"])

# M5 hattı (Üsküdar - Çekmeköy)
metro.istasyon_ekle("M5A1", "Üsküdar", ["M5"])
metro.istasyon_ekle("M5A2", "Bağlarbaşı", ["M5"])
metro.istasyon_ekle("M5A3", "Çekmeköy", ["M5"])

# M6 hattı (Levent - Boğaziçi Üniversitesi)
metro.istasyon_ekle("M6A1", "Levent", ["M6"])
metro.istasyon_ekle("M6A2", "Boğaziçi Üniversitesi", ["M6"])

# M7 hattı (Mahmutbey - Kabataş)
metro.istasyon_ekle("M7A1", "Mahmutbey", ["M7"])
metro.istasyon_ekle("M7A2", "Kabataş", ["M7"])

# M8 hattı (Bostancı - Dudullu)
metro.istasyon_ekle("M8A1", "Bostancı", ["M8"])
metro.istasyon_ekle("M8A2", "Dudullu", ["M8"])

# M9 hattı (İstanbul Havalimanı - Kayabaşı)
metro.istasyon_ekle("M9A1", "İstanbul Havalimanı", ["M9"])
metro.istasyon_ekle("M9A2", "Kayabaşı", ["M9"])

# Bağlantılar
metro.baglantilari_ekle(metro.istasyonlar["M1A1"], metro.istasyonlar["M2A1"], 5)
metro.baglantilari_ekle(metro.istasyonlar["M2A1"], metro.istasyonlar["M2A2"], 3)
metro.baglantilari_ekle(metro.istasyonlar["M2A2"], metro.istasyonlar["M2A3"], 4)
metro.baglantilari_ekle(metro.istasyonlar["M2A3"], metro.istasyonlar["M2A4"], 5)

# Başlangıç ve hedef
baslangic_id = "M1A1"  # Yenikapı
hedef_id = "M2A4"      # Hacıosman

# En az aktarmalı rotayı bulma
rota_aktarma = metro.en_az_aktarma_bul(baslangic_id, hedef_id)
if rota_aktarma:
    print(f"En az aktarmalı rota: {rota_aktarma}")
else:
    print("En az aktarmalı rota bulunamadı.")

# En hızlı rotayı bulma
result = metro.en_hizli_rota_bul(baslangic_id, hedef_id)
if result:
    rota, sure = result
    print(f"En hızlı rota: {rota} - Süre: {sure} dakika")
else:
    print("En hızlı rota bulunamadı.")
