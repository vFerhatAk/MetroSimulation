# MetroSimulation
Bu Python kodu, İstanbul’daki metro sistemini simüle etmek için yazılmış bir sınıf yapısına ve algoritmalara sahiptir. Metro hattı istasyonları arasındaki rotaları bulmaya yönelik iki temel algoritma içerir: *En Az Aktarmalı Rota* ve *En Hızlı Rota*. İşte kodun detaylı bir açıklaması:

### 1. *Sınıflar ve Yapılar*

#### *Istasyon Sınıfı*
- **Istasyon** sınıfı, her bir metro istasyonunu temsil eder. Bu sınıfın içerisinde:
  - **idx**: İstasyonun benzersiz kimliği.
  - **ad**: İstasyonun adı (örneğin, "Yenikapı", "Taksim").
  - **hatlar**: İstasyonun üzerinde bulunduğu metro hatlarını listeleyen bir liste.
  - **komsular**: Bu istasyonun doğrudan bağlı olduğu komşu istasyonları saklayan bir liste. Bağlantılı istasyonlar ve bu istasyonlar arasındaki süreler burada tutulur.

  **bagla** metodu, iki istasyon arasında bağlantı kurar.

#### *Metro Sınıfı*
- **Metro** sınıfı, metro sistemini temsil eder ve bir dizi işlem yapmamıza olanak sağlar:
  - **istasyonlar**: İstasyonların ID'ye göre tutulduğu bir sözlük. İstasyonlar bu sözlükte depolanır ve her bir istasyon bir **Istasyon** nesnesi olarak tutulur.
  - **hatlar**: Metro hatları ve her bir hattın istasyonları hakkında bilgiler barındıran bir sözlük.

  **istasyon_ekle** metodu, bir istasyon ekler.
  **hat_ekle** metodu, bir hat ekler.
  **baglantilari_ekle** metodu, iki istasyon arasına bağlantı ekler ve her bağlantının süresini belirtir.

### 2. *En Az Aktarmalı Rota (BFS)*

*En az aktarmalı rota bulma* için *BFS (Breadth-First Search)* algoritması kullanılır. BFS, bir grafiği katman katman keşfeden ve her bir düğümün en kısa mesafede keşfedilmesini sağlayan bir algoritmadır.

- *Algoritma Adımları*:
  1. *Başlangıç İstasyonu* ve *Hedef İstasyonu* tanımlanır.
  2. *BFS kuyruğu* (queue), başlangıç istasyonuyla başlatılır. Bu kuyruk, istasyonların sırasıyla ziyaret edilmesini sağlar.
  3. *Aktarma Sayısı*: Her istasyonun hangi hattı kullandığı kontrol edilerek aktarma yapılması gereken durumlar sayılır. Eğer mevcut istasyon ile bir komşu istasyon aynı hat üzerinde değilse, aktarma yapılır ve aktarma sayısı artırılır.
  4. *Hedefe Ulaşıldığında*: Hedef istasyona ulaşılınca, bu istasyonun rotası ve aktarma sayısı döndürülür.

Bu metodun amacı, aktarmaları minimum yaparak bir hedef istasyona ulaşmaktır.

### 3. *En Hızlı Rota (BFS)*

*En hızlı rota bulma* için de *BFS* algoritması kullanılır, ancak burada amaç rotayı en kısa sürede bulmaktır. Yani, her istasyon arasındaki yolculuk süresi dikkate alınır.

- *Algoritma Adımları*:
  1. *Başlangıç İstasyonu* ve *Hedef İstasyonu* tanımlanır.
  2. *BFS kuyruğu* başlatılır ve her istasyonun toplam süre bilgisi ile birlikte ziyaret edilmesi sağlanır.
  3. *Her İstasyonun Bağlantıları*: Her bir komşu istasyonun bağlantısı kontrol edilir. Bu bağlantının süresi, o anki toplam süreye eklenir.
  4. *Hedefe Ulaşıldığında*: Hedef istasyon bulunduğunda, toplam süre ve rota döndürülür.

Bu metodun amacı, en hızlı (yani toplam süreyi minimize eden) rotayı bulmaktır.

### 4. *Metro Sistemi Kurma ve Bağlantılar*

Kodda, İstanbul'daki metro hattına dair örnek bir sistem kurulur. M1, M2, M3, M4, M5, M6, M7, M8 ve M9 gibi farklı hattlar bulunur. Her bir hat için belirli istasyonlar eklenir ve aralarındaki bağlantılar baglantilari_ekle fonksiyonu ile oluşturulur. Bu bağlantılar, her bir hattın aktarma gereksinimlerini ve yolculuk sürelerini de göz önünde bulundurarak yapılır.

### 5. *Örnek Rota Aramaları*

Kodda belirtilen *başlangıç* ve *hedef* istasyonlarına göre:
- *Başlangıç İstasyonu*: "Yenikapı" (M1A1)
- *Hedef İstasyonu*: "Hacıosman" (M2A4)

Her iki algoritma da (en az aktarmalı ve en hızlı rota) bu iki istasyon arasındaki en uygun rotayı arar ve kullanıcıya sonucu döndürür.

### 6. *Sonuçlar*
- *En Az Aktarmalı Rota*: Kullanıcıya, iki istasyon arasında yapılması gereken en az aktarmalı rotayı verir. Eğer mümkünse, bu rota yazdırılır.
- *En Hızlı Rota*: Kullanıcıya, belirtilen iki istasyon arasında varılacak en hızlı rotayı ve bu rotanın toplam süresini sunar.

### 7. *Örnek Çıktılar*

Örneğin, *Yenikapı* ile *Hacıosman* arasında yapılacak en az aktarmalı rota ve en hızlı rota şu şekilde olabilir:
- *En Az Aktarmalı Rota*: "Yenikapı" -> "Vezneciler" -> "Taksim" -> "Hacıosman"
- *En Hızlı Rota*: "Yenikapı" -> "Taksim" -> "Hacıosman" - Süre: 10 dakika

### 8. *Sonuç*
Bu kod, İstanbul'daki metro sisteminin gerçek hayattaki verilerine dayalı olarak iki farklı rotayı aramak için kullanılabilir. Sistemi daha da geliştirmek için, aktarma sayısını ve süreyi daha detaylı şekilde optimize edebilir ve farklı parametreler ekleyebilirsiniz.

### 9. *Geliştirme İpuçları*
- *Gerçek Zamanlı Veriler*: Bu tür bir simülasyonu gerçek zamanlı veriyle desteklemek, örneğin hattın yoğunluk durumlarına göre yolculuk sürelerini değiştirmek mümkündür.
- *Hata Yönetimi*: Gerçek hayattaki veri hataları için hata yönetimi eklemek, sistemin dayanıklılığını artırır.
