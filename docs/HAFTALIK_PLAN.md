# Haftalık Plan – Madde Madde

Her madde **tek bir Claude Code isteği**dir. Kutudaki metni kopyalayıp Claude Code'a yapıştırın.

**Kurallar**

- Her maddeye başlamadan önce Claude Code'da `/clear` yazın. Böylece konuşma sıfırlanır, kullanım limitiniz daha geç dolar. `CLAUDE.md` her seferinde yeniden okunur, bilgi kaybolmaz.
- Yanında **[ELLE]** yazan maddeleri Claude Code değil siz yaparsınız. Claude yalnızca nasıl yapılacağını anlatır.
- **[COLAB]** yazan maddelerde Claude notebook yazar, siz Google Colab'da çalıştırıp çıktıyı geri yapıştırırsınız.
- Bir madde bitince `/modul-bitir` yazın. Claude test eder, inceler, not alır, kutuyu işaretler ve commit önerir.
- Hata alırsanız hata metninin **tamamını** kopyalayıp yapıştırın ve şunu yazın: "Bu hatayı aldım, nedenini açıkla ve düzelt."
- Geride kalırsanız (⭐ işaretleri): ⭐⭐⭐ olmazsa olmaz, ⭐⭐ olmalı, ⭐ olsa iyi. Kesmeye ⭐'dan başlayın.

---

## HAFTA 1 · 18–23 Kasım · Kurulum ve YouTube toplayıcı

**Hafta sonu hedefi:** YouTube linkinden standart CSV üreten script + Drive'da hazır veri setleri.

- [ ] **Madde 0: Ajan ve skill klasörünü yerine koy** ⭐⭐⭐ (bir kerelik)

```
Bu klasörde "_claude" adında bir klasör var; içinde agents ve skills alt klasörleri bulunuyor. Bu klasörün adını ".claude" yap (içeriğini olduğu gibi koru; .claude zaten varsa içine birleştir). Sonra .claude/agents ve .claude/skills içindeki dosyaları listele ve _claude klasörünün kalmadığını doğrula.
```

> Bu adım bitince Claude Code'u kapatıp yeniden açın (veya `/clear` yazın). Ajanlar ve skill'ler yeniden açılışta yüklenir.

- [ ] **Madde 1: Claude Code'un projeyi tanıdığını kontrol et** ⭐⭐⭐

```
CLAUDE.md dosyasını oku ve bana bu projeyi 5 cümlede özetle. Sonra .claude/agents ve .claude/skills klasörlerindeki ajanları ve skill'leri birer cümleyle listele. Hiçbir dosyayı değiştirme.
```

> Doğru özetlediyse kurulum tamam demektir. Ayrıca `/agents` yazarak ajan listesini görebilirsiniz.

- [ ] **Madde 2: Klasörü GitHub reposuna bağla** ⭐⭐⭐

```
Bu klasör henüz bir git deposu değil, ama GitHub'da https://github.com/yekurtulus/yorum-analizi adında aynı klasör yapısında bir repo var (main dalı, içinde boş .py dosyaları ve boş.txt'ler). Şunları yap ve her adımı bana açıkla:
1) git kurulu mu kontrol et; değilse nasıl kuracağımı anlat ve dur.
2) Bu klasörde git init yap, origin olarak bu repoyu ekle, origin/main'i çek. Yerel dosyalarımın üzerine yazma; çakışma olursa bana sor.
3) Klasörlerdeki boş.txt dosyalarını .gitkeep olarak yeniden adlandır ve .gitignore'u buna göre düzelt.
4) Yeni eklenen dosyaları (CLAUDE.md, .claude/, docs/ vb.) "Proje altyapısı: CLAUDE.md, ajanlar, skill'ler, plan" mesajıyla commit et.
5) Push etmeden önce bana sor. Push sırasında GitHub girişi istenirse ne yapacağımı anlat.
```

- [ ] **Madde 3: Python ortamını kur** ⭐⭐⭐

```
Windows'ta bu proje için Python ortamını kur: Python sürümünü kontrol et (3.11+ olmalı), .venv adında sanal ortam oluştur, requirements.txt'i kur. Sanal ortamı her seferinde nasıl etkinleştireceğimi ve VS Code'da nasıl seçeceğimi kısaca anlat. Sonra .claude/skills/standart-csv/dogrula.py ile data/ornek_standart.csv'yi doğrula.
```

- [ ] **Madde 4: API anahtarlarını al** ⭐⭐⭐ **[ELLE]**

```
YouTube Data API v3 anahtarını ve Gemini API anahtarını nasıl alacağımı adım adım, Türkçe ve ekran ekran anlat (Google Cloud Console ve Google AI Studio). Sonra .env.example dosyasını .env olarak kopyala; anahtarları ben kendim yazacağım. .env'nin git'e girmediğini kontrol et.
```

> Anahtarları siz yazın, sohbete **yapıştırmayın**.

- [ ] **Madde 5: SarcasTürk veri seti için e-posta** ⭐ **[ELLE]**

```
SarcasTürk ironi veri setinin yazarlarına, veri setini akademik bir ders projesinde kullanmak için izin ve erişim isteyen kısa, kibar, Türkçe bir e-posta taslağı yaz. Proje: Türkçe müşteri yorumu analizi, Yapay Zeka dersi, veri yeniden paylaşılmayacak. Makaleden yazar e-postalarını nasıl bulacağımı da söyle. Dosya oluşturma, sadece metni ver.
```

- [ ] **Madde 6: CSV/Excel yükleme toplayıcısı** ⭐⭐⭐

```
toplayici ajanını kullan. collectors/csv_yukle.py dosyasını yaz: kullanıcının yüklediği herhangi bir CSV veya Excel dosyasını standart CSV'ye çevirsin. Yorum sütununu farklı adlarla (Yorum, yorum, comment, text, review, içerik…) otomatik bulsun, bulamazsa hata mesajında sütun adlarını göstersin. Platform "csv", alan parametre olarak verilsin. standart-csv skill'indeki doğrulamayı kullansın. Komut satırından çalışsın ve data/ornek_standart.csv ile test et.
```

- [ ] **Madde 7: YouTube toplayıcı** ⭐⭐⭐

```
toplayici ajanını kullan. collectors/youtube.py dosyasını yaz: YouTube Data API v3 ile bir video linkinden (youtube.com/watch?v=, youtu.be/, shorts/ biçimlerinin hepsi) üst düzey yorumları ve istenirse yanıtları çeksin; limit parametresi olsun (varsayılan 300); sayfalama (nextPageToken) yapsın; tarihi YYYY-MM-DD'ye çevirsin; kanal/kullanıcı adını KAYDETMESİN; platform=youtube, alan=video. API kotasını ve hata durumlarını (yorumlar kapalı, geçersiz link, kota doldu) anlaşılır Türkçe mesajla yönetsin. Önce planını göster, onaylarsam yaz. Sonra benim vereceğim bir linkle test edelim.
```

- [ ] **Madde 8: Hazır veri setlerini Drive'a indir** ⭐⭐⭐ **[COLAB]**

```
model-egitici ajanını kullan. models/egitim_notebooklari/00_veri_indirme.ipynb notebook'unu yaz: Google Drive'ı bağlasın, /content/drive/MyDrive/yorum-analizi/veri/ altına proje planındaki veri setlerini Hugging Face'ten indirsin (winvoker/turkish-sentiment-analysis-dataset, turkish_product_reviews ve plandaki SemEval-2016 Türkçe restoran veri seti). Her veri seti için satır sayısını, sütunları ve sınıf dağılımını göstersin. Bir veri seti Hugging Face'te bulunamazsa hata vermeden atlasın ve uyarı yazsın. Bittikten sonra bu notebook'u Colab'da nasıl çalıştıracağımı adım adım anlat.
```

> Colab çıktısını (özellikle hata ve tablo kısımlarını) Claude'a geri yapıştırın.

- [ ] **Madde 9: Hafta 1 kapanışı** ⭐⭐⭐

```
/modul-bitir
```

> Ardından: "Tüm commit'leri GitHub'a push et." Ekip arkadaşlarınız `git pull` ile alır.

---

## HAFTA 2 · 24–30 Kasım · Temizlik, parçalama, duygu modeli

**Hafta sonu hedefi:** Çalışan duygu modeli + ilk sonuç tablosu + Gemini ile etiketleme başladı.

- [ ] **Madde 1: Temizlik ve Türkçe filtresi** ⭐⭐⭐

```
pipeline-muhendisi ajanını kullan. pipeline/temizlik.py dosyasını turkce-metin skill'indeki sıraya göre yaz: HTML/boşluk temizliği, link sayma + [LINK] ile değiştirme, kişisel bilgi silme (e-posta, telefon, @kullanıcı), tekrar harf sınırlama, Türkçe filtresi, kısa yorum işareti. Fonksiyon DataFrame alıp yeni sütunlar eklesin (temiz_yorum, link_sayisi, turkce_mi, kisa_mi). tests/test_temizlik.py ile en az 8 Türkçe örnek üzerinde test et (İ/ı dönüşümü dahil).
```

- [ ] **Madde 2: Yorum parçalama** ⭐⭐⭐

```
pipeline-muhendisi ajanını kullan. pipeline/parcalama.py dosyasını turkce-metin skill'indeki parçalama kurallarına göre yaz. Her yorum satırını parçalara bölüp yorum_id ve parca_no sütunlarıyla yeni bir DataFrame döndürsün. tests/test_parcalama.py içinde en az 10 zor örnek olsun ("yemek güzel ama servis yavaş", "fena değil ama pahalı", "yalnız gittim, çok beğendim", tek kelimelik yorum, emojili yorum...). Sonuçları bana tablo olarak göster.
```

- [ ] **Madde 3: Konu listelerini kesinleştir** ⭐⭐⭐ **[ELLE – ekip toplantısı]**

```
CLAUDE.md'deki üç alanın (ürün, mekan, video) konu listelerini incele. Her konu için 1 cümlelik tanım ve 3'er örnek yorum parçası yaz; sınırda kalan durumları (ör. "kargo hızlı ama kutu ezik" hangi konular?) listele. Bunu docs/konu_tanimlari.md dosyasına yaz. Ekip olarak okuyup karar vereceğiz.
```

> 3 kişi 20 dakika oturup tanımlara karar verin. Sonra Claude'a "konu_tanimlari.md'yi şu kararlarla güncelle: …" deyin. **Bu tanımlar etiketlemenin temelidir; sonradan değiştirmek pahalıdır.**

- [ ] **Madde 4: Duygu modeli – TF-IDF baseline** ⭐⭐⭐ **[COLAB]**

```
model-egitici ajanını kullan. models/egitim_notebooklari/01_duygu_tfidf.ipynb notebook'unu yaz: Drive'daki winvoker ve turkish_product_reviews verilerini birleştirip olumlu/olumsuz/nötr üç sınıfa getirsin (etiket eşleştirmesini açıkla), en fazla 30 bin örnek alsın, TF-IDF + Lojistik Regresyon eğitsin, model-degerlendirme skill'indeki metrikleri versin ve modeli Drive'a kaydetsin. Bu notebook GPU gerektirmez, bunu da belirt.
```

- [ ] **Madde 5: Duygu modeli – BERTurk ince ayar** ⭐⭐⭐ **[COLAB]**

```
model-egitici ajanını kullan. models/egitim_notebooklari/02_duygu_berturk.ipynb notebook'unu colab-notebook skill'indeki hücre sırasıyla yaz: dbmdz/bert-base-turkish-cased'i 01 notebook'undaki aynı veri ve aynı bölme ile 3 sınıflı duygu için ince ayarla. Sonunda TF-IDF ile yan yana karşılaştırma tablosu çıksın. Modeli Drive'a kaydetsin. Colab'da ne kadar süreceğini tahmin et.
```

> Eğitim 30–60 dk sürebilir. Colab sekmesini kapatmayın.

- [ ] **Madde 6: Gemini ile toplu etiketleme scripti** ⭐⭐⭐

```
model-egitici ajanını kullan. models/gemini_etiketle.py scriptini gemini-kullanimi skill'ine göre yaz: bir CSV'deki yorum parçalarını 40'lık gruplar halinde Gemini'ye göndersin, docs/konu_tanimlari.md'deki konuları kullansın, duygu + konular + ironik etiketlerini JSON olarak alsın, data/etiketli/gemini_<alan>.csv'ye eklesin, kaldığı yerden devam edebilsin, istekler arasında beklesin. Önce --deneme bayrağıyla yalnızca 1 grup (40 parça) çalışsın; sonuçları birlikte kontrol edelim.
```

- [ ] **Madde 7: Etiketlenecek verileri hazırla ve etiketlemeyi başlat** ⭐⭐⭐

```
Etiketleme için üç alanın ham verisini hazırla:
- urun: Drive'dan indirdiğimiz turkish_product_reviews'ten rastgele 2.000 yorum (bunu bilgisayara nasıl alacağımı anlat),
- mekan: SemEval restoran verisi; mevcut konu etiketlerini bizim mekan konularımıza eşleştiren bir tablo öner,
- video: collectors/youtube.py ile 5-6 farklı türde videodan (inceleme, eğitim, vlog) toplam ~2.000 yorum.
Hepsini temizlik + parçalama adımlarından geçirip data/etiketli/etiketlenecek_<alan>.csv olarak kaydet. Sonra gemini_etiketle.py'yi önce urun için --deneme ile çalıştır.
```

> Gemini ücretsiz kotası günlüktür. Etiketlemeyi 2-3 güne yayın; script kaldığı yerden devam eder.

- [ ] **Madde 8: Hafta 2 kapanışı** ⭐⭐⭐

```
/modul-bitir
```

---

## HAFTA 3 · 1–7 Aralık · Altın test seti, konu modelleri, spam, web toplayıcılar

**Hafta sonu hedefi:** Konu modeli + 3 platformdan CSV.

- [ ] **Madde 1: Altın test setini hazırla** ⭐⭐⭐ **[ELLE – 3 kişi]**

```
model-degerlendirme skill'ine göre altın test seti için her alandan 150 parça seç (etiketlenecek_<alan>.csv'den, Gemini'nin etiketlediklerinden FARKLI olanlardan, rastgele ama alanı temsil edecek şekilde). data/etiketli/altin_<alan>_bos.xlsx olarak kaydet: sütunlar parca, duygu, konular, ironik; duygu ve ironik için Excel'de açılır liste olsun. Ayrıca 3 kişinin bağımsız etiketleyip sonra nasıl birleştireceğimizi (çoğunluk oyu) anlatan kısa bir talimat yaz ve birleştirme scripti hazırla: models/altin_birlestir.py.
```

> Her biriniz aynı 450 parçayı **birbirinize bakmadan** etiketleyin (~2-3 saat/kişi). `docs/konu_tanimlari.md` açık dursun. Sonra birleştirme scriptini çalıştırın.

- [ ] **Madde 2: Gemini etiketlerini kontrol et** ⭐⭐

```
data/etiketli/gemini_*.csv dosyalarını incele: her alan için etiket dağılımı, hiç kullanılmayan konular, boş/bozuk satırlar. Altın test setiyle çakışan metin varsa eğitim verisinden çıkar. Kısa bir rapor ver.
```

- [ ] **Madde 3: Konu modelleri (3 alan)** ⭐⭐⭐ **[COLAB]**

```
model-egitici ajanını kullan. models/egitim_notebooklari/03_konu_berturk.ipynb notebook'unu yaz: en üstteki ALAN ayarıyla (urun / mekan / video) çalışsın, data/etiketli/gemini_<ALAN>.csv ile BERTurk'ü çok etiketli (multi-label, sigmoid + eşik) sınıflandırma için ince ayarlasın, eşiği doğrulama setinde ayarlasın, altın test setinde konu bazında F1 versin, modeli Drive'a <ALAN> adıyla kaydetsin. Mekan için ayrıca SemEval verisini ekleme seçeneği olsun.
```

> Notebook'u üç kez çalıştırın: ALAN = urun, mekan, video.

- [ ] **Madde 4: Spam / şüpheli yorum filtresi** ⭐⭐

```
pipeline-muhendisi ajanını kullan. pipeline/spam.py dosyasını yaz. Kurallar: link içeren, "kanalıma bakın / abone ol / takip et" kalıpları, birebir tekrar eden metin, 2 kelimeden kısa, tamamı büyük harf veya tamamı emoji. Her kural ayrı bir fonksiyon olsun, her yoruma supheli (True/False) ve supheli_neden sütunu eklesin. Arayüzde "sahte" değil "şüpheli" kullanılacak. tests/test_spam.py ile test et.
```

- [ ] **Madde 5: Google Haritalar toplayıcı** ⭐⭐

```
toplayici ajanını kullan. collectors/google_maps.py dosyasını web-toplayici skill'ine harfiyen uyarak Playwright ile yaz: mekan linki → Yorumlar sekmesi → En yeni sıralaması → panel kaydırma → "Daha fazla" genişletme; "2 ay önce" tarihlerini yaklaşık tarihe çevirsin (tarih_yaklasik=True); limit varsayılan 200; headless seçeneği; captcha/engel görürse dursun. Önce Playwright kurulumunu yap. Planını göster, onaylarsam yaz; sonra küçük bir limitle (20) test edelim.
```

- [ ] **Madde 6: E-ticaret toplayıcı** ⭐⭐

```
toplayici ajanını kullan. collectors/eticaret.py dosyasını web-toplayici skill'ine uyarak yaz: Trendyol ve Hepsiburada ürün linklerini tanısın, yorum sayfasını açsın, yorum + yıldız + tarihi okusun, platform=trendyol/hepsiburada, alan=urun. Seçicileri dosyanın başında topla. Planını göster, onaylarsam yaz; sonra limit 20 ile test edelim.
```

> Site yapısı değişirse kod bozulabilir. Bozulursa: "eticaret.py artık çalışmıyor, şu hatayı veriyor: … Seçicileri güncelle." Olmazsa CSV yükleme yolu her zaman var.

- [ ] **Madde 7: Hafta 3 kapanışı** ⭐⭐⭐

```
/modul-bitir
```

---

## HAFTA 4 · 8–14 Aralık · Uçtan uca analiz (arayüzsüz)

**Hafta sonu hedefi:** `analyze(csv)` tek fonksiyonla her şeyi hesaplıyor.

- [ ] **Madde 1: İroni modeli (deneysel)** ⭐ **[COLAB]**

```
model-egitici ajanını kullan. models/egitim_notebooklari/04_ironi.ipynb notebook'unu yaz: SarcasTürk elimizdeyse onu, değilse Gemini'nin ironik=true işaretlediği parçalar + aynı sayıda ironik olmayan parçayla BERTurk ikili sınıflandırma eğitsin. Veri azsa bunu açıkça yazsın. Sonuçlar "deneysel" diye etiketlenecek.
```

> Vakit darsa bu maddeyi **atlayın**; pipeline ironi modülü olmadan da çalışacak şekilde yazılıyor.

- [ ] **Madde 2: Eğitilmiş modelleri bilgisayarda çalıştırma** ⭐⭐⭐

```
pipeline-muhendisi ajanını kullan. Drive'daki eğitilmiş modelleri (duygu, konu_urun, konu_mekan, konu_video, varsa ironi) models/kaydedilmis_modeller/ altına nasıl indireceğimi anlat. Sonra pipeline/modeller.py dosyasını yaz: modelleri bir kez yükleyip önbellekte tutsun (CPU'da), duygu_tahmin(parcalar), konu_tahmin(parcalar, alan), ironi_tahmin(parcalar) fonksiyonları toplu (batch) çalışsın. Bir model klasörü yoksa açık bir hata mesajı versin; ironi modeli yoksa sessizce atlasın. requirements.txt'e transformers ve torch'u (CPU sürümü) ekle, nasıl kurulacağını söyle.
```

- [ ] **Madde 3: analyze(csv) fonksiyonu** ⭐⭐⭐

```
pipeline-muhendisi ajanını kullan. pipeline/analiz.py içinde analyze(csv_yolu, alan) fonksiyonunu yaz: standart CSV'yi okusun → temizlik → spam → parçalama → duygu → ironi (varsa, ironik olumluyu olumsuza çevir) → konu. Sonuç sözlüğü: genel skor (0-10), olumlu/olumsuz/nötr sayıları, güven seviyesi ve cümlesi ("Bu analiz 47 yoruma dayanıyor, güven: orta"), konu tablosu (her konu için olumlu/olumsuz yüzde ve sayı), her konu için en net 2 olumlu ve 2 olumsuz örnek, ironi ve spam sayıları. CLAUDE.md'deki hesap kurallarına uy. data/ornek_standart.csv ile çalıştırıp sonucu düzgün yazdır.
```

- [ ] **Madde 4: Trend ve aylık karşılaştırma** ⭐⭐

```
pipeline-muhendisi ajanını kullan. analiz.py'ye aylık trend ekle: her ay için skor ve yorum sayısı; son ay ile önceki ayın karşılaştırması ve en çok değişen konu ("Memnuniyet 7,2'den 6,1'e düştü; en büyük düşüş kargoda (−%18)"); 20'den az yorumlu aylara uyarı; tarih_yaklasik varsa "tarihler yaklaşık" notu. Tarihi olmayan yorumlar trende girmesin ama genel skora girsin. Test et.
```

- [ ] **Madde 5: Gemini özeti + şablon yedeği** ⭐⭐⭐

```
pipeline-muhendisi ajanını kullan. pipeline/ozet.py dosyasını gemini-kullanimi skill'ine göre yaz: analyze() sonucunu (ham yorumların hepsini değil, istatistikleri ve konu başına en fazla 3 örneği) Gemini'ye göndersin, 3-5 madde "Beğenilenler" ve 3-5 madde "Beğenilmeyenler" alsın. Analiz başına tek çağrı, sonucu önbelleğe al, API anahtarı yoksa veya hata/kota olursa şablon özete düşsün ve bunu belirtsin. Hem Gemini'li hem Gemini'siz (anahtarı geçici olarak boşaltarak) test et.
```

- [ ] **Madde 6: Uçtan uca test** ⭐⭐⭐

```
Uçtan uca test yap: data/ham altındaki gerçek bir YouTube CSV'si, bir Google Haritalar CSV'si ve bir e-ticaret CSV'si (hangileri varsa) için analyze() + özet çalıştır, sonuçları özetle ve süreleri ölç. Yavaş olan adım varsa hızlandırma öner. Sonra inceleyici ajanıyla pipeline/ klasörünün tamamını incelet.
```

- [ ] **Madde 7: Hafta 4 kapanışı** ⭐⭐⭐

```
/modul-bitir
```

---

## HAFTA 5 · 15–21 Aralık · Streamlit arayüzü ve demo

**Hafta sonu hedefi:** Çalışan demo.

- [ ] **Madde 1: Arayüz iskeleti + Analiz Et sayfası** ⭐⭐⭐

```
arayuz-gelistirici ajanını kullan. app/streamlit_app.py'yi 4 sayfalı yapıyla kur (Analiz Et, Sonuç Paneli, Aylık Karşılaştırma, Model Hakkında). Önce yalnızca Analiz Et sayfasını tamamla: link girme (platformu linkten otomatik tanı) veya CSV/Excel yükleme, alan seçimi, "Demo verisi kullan" seçeneği, analiz sırasında ilerleme göstergesi. Sonuç st.session_state'e kaydedilsin. Nasıl çalıştıracağımı söyle.
```

- [ ] **Madde 2: Sonuç Paneli** ⭐⭐⭐

```
arayuz-gelistirici ajanını kullan. Sonuç Paneli sayfasını yaz: büyük skor göstergesi (0-10), güven cümlesi, Beğenilenler/Beğenilmeyenler özeti (şablon özetse küçük not), konu tablosu + yatay çubuk grafik (olumlu yeşil, olumsuz kırmızı), her konu için açılır kutuda 2 olumlu ve 2 olumsuz örnek, ironi ve spam istatistikleri. Sade ve okunaklı olsun.
```

- [ ] **Madde 3: Aylık Karşılaştırma sayfası** ⭐⭐

```
arayuz-gelistirici ajanını kullan. Aylık Karşılaştırma sayfasını yaz: aylık skor çizgi grafiği (yorum sayısı ikinci eksende çubuk), bu ay / geçen ay kartları ve farkı, en çok değişen konular, az yorumlu ay ve yaklaşık tarih uyarıları.
```

- [ ] **Madde 4: Model karşılaştırması + Model Hakkında sayfası** ⭐⭐ **[COLAB]**

```
model-egitici ajanını kullan. models/egitim_notebooklari/05_karsilastirma.ipynb'yi yaz: altın test setinde TF-IDF, bizim BERTurk ve Gemini'nin doğrudan cevabını (mekan için ayrıca Sengil/ABSA-Turkish-bert-based-small) model-degerlendirme skill'indeki tabloyla karşılaştırsın, karışıklık matrislerini ve hata örneklerini kaydetsin. Sonra arayuz-gelistirici ile Model Hakkında sayfasını bu dosyalardan okuyacak şekilde yaz (tablo, grafik, kısa açıklama, "modelin yanıldığı örnekler").
```

- [ ] **Madde 5: Demo CSV'leri ve demo modu** ⭐⭐⭐

```
Sunum için data/demo_csv/ altına 3 hazır CSV hazırla: bir YouTube videosu, bir Google Haritalar mekanı, bir e-ticaret ürünü (her biri 150-400 yorum, en az 3 aya yayılmış). Kişisel bilgi olmadığını kontrol et. Demo modunun internet olmadan da çalıştığını test et (Gemini yoksa şablon özet). Bu CSV'ler sunumda gösterileceği için git'e eklenebilir; ham veri klasörü eklenmez.
```

- [ ] **Madde 6: Hafta 5 kapanışı + ekip provası** ⭐⭐⭐

```
/modul-bitir
```

> Ekipçe uygulamayı baştan sona birlikte kullanın, her hatayı not edin.

---

## HAFTA 6 · 22–24 Aralık · Kod dondurma

**Kural: yeni özellik yok, sadece hata düzeltme.**

- [ ] **Madde 1: Tam proje incelemesi** ⭐⭐⭐

```
inceleyici ajanıyla projenin tamamını incelet. Sonra bulunan sorunları önem sırasına göre listele; yalnızca gerçek hataları düzelt, yeni özellik ekleme.
```

- [ ] **Madde 2: Temiz kurulum testi** ⭐⭐⭐ **[ELLE]**

```
README.md'yi güncelle: kurulum, modellerin Drive'dan indirilmesi, .env, çalıştırma, demo modu. Bir ekip arkadaşım repoyu sıfırdan kendi bilgisayarına kurup çalıştıracak; adımları ona göre eksiksiz yaz.
```

> Ekip arkadaşınız README'ye bakarak kendi bilgisayarında kursun. Takıldığı her yer README'de düzeltilmeli.

- [ ] **Madde 3: Bonus (sadece vakit kalırsa)** ⭐

```
Vaktimiz var. CLAUDE.md'deki bonusları (firma adıyla arama, Şikâyetvar) değerlendir: hangisi en az riskle 1 günde yapılır? Plan öner, kod yazma.
```

---

## HAFTA 7 · 25–30 Aralık · Sunum

- [ ] **Madde 1: Sunum içeriği** ⭐⭐⭐

```
docs/NOTLAR.md, models/sonuclar/ ve proje planındaki sunum akışına (10-12 slayt) göre her slayt için başlık, 3-4 madde ve konuşmacı notu yaz: Problem, canlı demo, mimari şeması, veri ve etiketleme yöntemi, modeller ve karşılaştırma tablosu, ironi ve spam örnekleri, hata analizi, sınırlamalar ve gelecek çalışmalar. docs/sunum_icerik.md'ye kaydet.
```

> Slaytları claude.ai'de sohbette "bu içerikten sunum yap" diyerek veya PowerPoint'te hazırlayabilirsiniz.

- [ ] **Madde 2: Demo videosu** ⭐⭐⭐ **[ELLE]**

> Uygulamayı demo verisiyle baştan sona kullanırken ekran kaydı alın (Windows: Win+G → Xbox Game Bar → kayıt). 2-3 dakika. Canlı demo çökerse bu oynatılır.

- [ ] **Madde 3: Soru-cevap provası** ⭐⭐⭐

```
docs/NOTLAR.md ve kodları okuyarak hocanın sorabileceği 20 soruyu (her modül için en az 2) ve kısa cevaplarını yaz; kim hangi bölümü anlatacaksa ona göre grupla. docs/soru_cevap.md'ye kaydet.
```

> En az 2 prova yapın. Herkes her modülü anlatabilmeli.
