# Rehber – Bu projede ne nedir, nasıl çalışır?

Bu dosya projeye ve araçlara hiç aşina olmayan biri için yazıldı. Sırayla okuyun.

---

## 1. Büyük resim

```
SİZ  ──(docs/HAFTALIK_PLAN.md'den bir madde kopyalarsınız)──►  CLAUDE CODE (ana Claude)
                                                                   │
                                     her oturumda okur: CLAUDE.md  │  (projenin kuralları)
                                                                   ▼
                                       işi uygun uzmana devreder (AJAN)
         ┌──────────────┬────────────────┬────────────────────┬────────────────────┬──────────────┐
      toplayici    model-egitici    pipeline-muhendisi   arayuz-gelistirici     inceleyici
         │                │                 │                     │                   │
         └── her ajan işe başlarken kendi el kitaplarını (SKILL) okur ──────────────────┘
                 standart-csv · turkce-metin · web-toplayici · colab-notebook
                 gemini-kullanimi · model-degerlendirme · modul-bitir
```

Siz proje yöneticisisiniz: ne yapılacağını siz söylersiniz, kodu çalıştırıp kontrol edersiniz. Claude Code kodu yazar.

---

## 2. Claude Code nedir, nasıl açılır?

Claude Code, Claude'un **bilgisayarınızdaki bir klasörde** çalışan hâlidir. Normal sohbetten farkı:

- Klasördeki dosyaları okuyabilir, yeni dosya yazabilir, var olanları düzenleyebilir.
- Komut çalıştırabilir (`python ...`, `pip install ...`, `git commit ...`).
- Önemli bir şey yapmadan önce (dosya yazmak, komut çalıştırmak) **izin ister**. Ne yaptığını okuyup "Evet" veya "Hayır" dersiniz.

**Açmanın iki yolu** (Claude Pro planınız Claude Code'u kapsar):

1. **Masaüstü uygulaması:** Claude uygulamasında Code bölümünü açın ve çalışma klasörü olarak `C:\Users\user\Desktop\yorum-analiz` klasörünü seçin.
2. **Terminal:** Claude Code'u kurduktan sonra (kurulum talimatı: https://docs.claude.com/en/docs/claude-code/overview) PowerShell'de:
   ```powershell
   cd C:\Users\user\Desktop\yorum-analiz
   claude
   ```

İkisi de aynı klasörde aynı dosyaları (`CLAUDE.md`, `.claude/`) kullanır.

**Bilmeniz gereken birkaç komut** (sohbet kutusuna yazılır):

| komut | ne yapar |
|---|---|
| `/clear` | konuşmayı sıfırlar. **Her yeni maddeden önce kullanın.** |
| `/agents` | ajanları listeler |
| `/modul-bitir` | bizim skill'imiz: bir maddeyi kapatır (test, inceleme, not, commit) |
| `/` | kullanılabilecek tüm komutları listeler |
| `Esc` | Claude'u o anki işinde durdurur (yanlış yöne gidiyorsa) |

---

## 3. Plan modu nedir?

Claude Code'un birkaç **çalışma modu** vardır:

- **Normal mod:** Claude dosya yazmadan veya komut çalıştırmadan önce izin ister.
- **Düzenlemeleri otomatik kabul:** dosya değişikliklerinde izin sormaz. Yeni başlayanlar için önermiyorum.
- **Plan modu:** Claude **hiçbir dosyayı değiştiremez**, sadece okur, düşünür ve ne yapacağının planını sunar. Planı beğenirseniz onaylarsınız, sonra yazmaya geçer.

**Nasıl açılır?**

- Terminalde **Shift + Tab** tuşlarına basınca modlar sırayla değişir. Alt satırda hangi modda olduğunuz yazar ("plan mode" gibi).
- Masaüstü uygulamasında mesaj kutusunun yakınındaki mod seçicisinden "Plan" seçilir.

**Ne zaman kullanılır?** Büyük ve emin olmadığınız işlerde (ör. Google Haritalar toplayıcı). Plandaki istemlerin çoğunda zaten "önce planını göster, onaylarsam yaz" yazıyor. Bu, plan modunun yaptığı işin aynısını yazıyla istemek demektir. Yani plan modunu kullanmasanız da olur.

---

## 4. CLAUDE.md nedir?

Repo kökündeki `CLAUDE.md`, Claude Code'un **her oturum başında otomatik okuduğu** proje hafızasıdır. İçinde projenin amacı, standart CSV formatı, klasörler, kurallar, kırmızı çizgiler ve öncelikler var. Böylece her seferinde projeyi baştan anlatmanız gerekmez.

**Değiştirebilirsiniz.** Bir karar değişirse (ör. konu listesi) Claude'a "CLAUDE.md'yi şu kararla güncelle" deyin. Kısa tutun: her satır her oturumda okunur.

---

## 5. Ajan (subagent) nedir?

Bir şirket düşünün: siz ana Claude'la (proje müdürü) konuşursunuz. Müdürün yanında **uzman çalışanlar** vardır. Her birinin kendi görev tanımı, kendi yetkileri ve kendi "çalışma masası" vardır.

- **Kendi görev tanımı:** ör. `toplayici` yalnızca veri toplama kodu yazmayı bilir ve kurallarını ezbere bilir.
- **Kendi yetkileri:** ör. `inceleyici` dosya okuyabilir ama **değiştiremez**; tarafsız denetçi olsun diye.
- **Kendi çalışma masası (bağlam):** Ajan işini ayrı bir konuşmada yapar ve sonuçta size sadece özeti döner. Ana konuşmanız şişmez; bu, kullanım limitini korur.

**Ajanlar nerede?** `.claude/agents/` klasöründe, her biri bir `.md` dosyası:

| ajan | görevi | dosya değiştirir mi? |
|---|---|---|
| `toplayici` | YouTube, Google Haritalar, e-ticaret, CSV yükleme kodları | evet |
| `model-egitici` | Colab notebook'ları, Gemini etiketleme, metrikler | evet |
| `pipeline-muhendisi` | temizlik, spam, parçalama, `analyze()`, özet | evet |
| `arayuz-gelistirici` | Streamlit arayüzü | evet |
| `inceleyici` | kodu inceler, Türkçe açıklar, hocanın sorabileceği soruları çıkarır | **hayır** |

**Nasıl kullanılır?** İki yol var:

1. **Açıkça:** "toplayici ajanını kullan. …". Plandaki istemler hep böyle başlıyor.
2. **Otomatik:** Ana Claude, ajan dosyasındaki `description` satırına bakarak uygun işi kendisi devredebilir.

Ajan dosyasının yapısı:

```markdown
---
name: inceleyici                 ← ajanın adı
description: ... kullan.         ← ne zaman çağrılacağı (Claude buna bakar)
tools: Read, Grep, Glob          ← yetkileri (burada sadece okuma)
skills:
  - standart-csv                 ← işe başlarken okuyacağı el kitapları
---
Sen deneyimli bir kod inceleyicisisin...   ← görev tanımı
```

---

## 6. Skill nedir? Bu projede hangileri var?

Skill, Claude'un belirli bir işi **doğru yapması için okuduğu el kitabıdır**. Tarif kartı gibi düşünün: "Colab notebook'u yazarken şu sırayla hücre koy, şuraya kaydet". Ajan, bilgi; skill ise yöntemdir.

Skill'ler `.claude/skills/<ad>/SKILL.md` dosyalarında. Ajan dosyasının `skills:` satırında yazanlar, ajan başlarken otomatik okunur. Her skill ayrıca `/ad` komutuyla da çağrılabilir.

| skill | neden gerekli? | kim kullanır |
|---|---|---|
| `standart-csv` | Projenin omurgası. Sütunlar, kurallar ve **çalışan doğrulama scripti** (`dogrula.py`) | toplayici, pipeline, arayüz, inceleyici |
| `turkce-metin` | Türkçe'ye özgü tuzaklar: `"İ".lower()` hatası, BERTurk'ün büyük/küçük harf duyarlılığı, "ama/fakat" ile parçalama, "2 ay önce" tarihleri | toplayici, model-egitici, pipeline |
| `web-toplayici` | Playwright ile sayfa okurken nezaket (bekleme, limit, engelde durma) ve dayanıklılık kuralları | toplayici |
| `colab-notebook` | GPU kontrolü, Drive'a kaydetme, hücre sırası, süre limitleri | model-egitici |
| `gemini-kullanimi` | Ücretsiz kotayı koruma, kişisel bilgi silme, JSON çıktı, şablon yedeği, hazır istemler | model-egitici, pipeline |
| `model-degerlendirme` | Altın test seti kuralları, metrikler, TF-IDF / BERTurk / Gemini karşılaştırma tablosu, hata analizi | model-egitici |
| `modul-bitir` | Her maddenin kapanış rutini: test → inceleme → `NOTLAR.md` → commit | siz (`/modul-bitir`) |

Hazır internet skill'lerine (başkalarının yazdıkları) gerek yok; bu projeye özel olanlar daha iyi çalışır. İleride ihtiyaç doğarsa (ör. "sunum hazırlama") yenisini Claude'a yazdırırsınız.

---

## 7. Colab nedir?

**Google Colab** (colab.research.google.com), Google'ın tarayıcıda çalışan **ücretsiz Python ortamıdır**. Önemli tarafı, ücretsiz **GPU** (ekran kartı) vermesi.

**Neden lazım?** BERTurk gibi büyük dil modellerini eğitmek, normal bir bilgisayarın işlemcisinde (CPU) saatler, hatta günler sürer. GPU ile 20–60 dakikada biter. Sizin bilgisayarınızda uygun GPU olmadığını varsayıyoruz.

**Nasıl çalışır?**

1. Colab, **notebook** (`.ipynb`) denen dosyalarla çalışır: kod ve açıklamaların hücre hücre dizildiği bir defter.
2. Claude Code notebook'u yazar → `models/egitim_notebooklari/` klasörüne koyar.
3. Siz colab.research.google.com → **Dosya → Not defteri yükle** ile açarsınız.
4. **Çalışma zamanı → Çalışma zamanı türünü değiştir → T4 GPU** seçersiniz.
5. Hücreleri sırayla çalıştırırsınız (**Shift + Enter**). İlk hücrelerden biri Google Drive'ınıza erişim izni ister; verin.
6. Eğitilen model **Google Drive**'ınıza kaydedilir (`MyDrive/yorum-analizi/`).
7. Çıktıyı (sonuç tablosu ya da hata) kopyalayıp Claude Code'a yapıştırırsınız; o yorumlar.

**Dikkat:**

- Ücretsiz GPU süresi sınırlı. Uzun süre işlem yapmazsanız oturum kapanabilir. Eğitim sırasında sekmeyi açık tutun.
- Colab'daki dosyalar oturum kapanınca **silinir**. Bu yüzden her şey Drive'a kaydediliyor.
- Drive'daki `yorum-analizi` klasörünü 3 kişi arasında **paylaşın**. Herkes aynı veri ve modelleri görsün.
- Eğitilen modelleri, sonradan bilgisayarınızda (CPU'da) tahmin yapmak için Drive'dan indirirsiniz. Tahmin yapmak eğitmekten çok daha hafif bir iştir.

---

## 8. Gemini ile ne yapacağız?

Gemini, Google'ın büyük dil modeli (Claude'un benzeri). Ücretsiz katmanı var. **Analizi Gemini yapmıyor**, sizin eğittiğiniz modeller yapıyor; Gemini'nin 3 yardımcı işi var:

### İş 1: Eğitim verisi etiketlemek (en önemlisi)

Konu modelini eğitmek için binlerce yorum parçasının "bu parça hangi konudan bahsediyor (kargo? fiyat?) ve olumlu mu olumsuz mu?" diye **etiketlenmiş** olması gerekir. YouTube ve e-ticaret için böyle hazır Türkçe veri yok. 2.000 parçayı elle etiketlemek günler sürer.

Çözüm: `models/gemini_etiketle.py` scripti parçaları 40'arlı gruplar halinde Gemini'ye gönderir, "her birinin konusunu ve duygusunu söyle" der, cevapları CSV'ye yazar. Bu etiketler kusursuz değildir ama model eğitmeye yeter. Raporda buna **"LLM destekli zayıf denetim (weak supervision)"** denir.

Kusurları dengelemek için **altın test seti** var: her alandan 150 parçayı siz 3 kişi **elle** etiketlersiniz. Modelin başarısı yalnızca bununla ölçülür. Gemini'nin hatalı etiketleri sonucu şişiremez.

### İş 2: Özet yazmak

Analiz bitince elinizde sayılar olur: "kargo %72 olumsuz, lezzet %85 olumlu…". `pipeline/ozet.py` bu **hazır sayıları** Gemini'ye verir, o da okunabilir maddeler yazar:

> **Beğenilenler:** Yemeklerin lezzeti çok övülüyor… · **Beğenilmeyenler:** Servis yavaşlığı en sık şikâyet…

Gemini çalışmazsa (internet yok, kota doldu) **şablon özet** devreye girer: "En çok beğenilen: lezzet (%85)…". Demo hiçbir zaman Gemini yüzünden çökmez.

### İş 3: Karşılaştırma

Sunumda güçlü bir slayt: "Aynı test setinde Gemini'ye doğrudan sorsak ne kadar başarılı olurdu?" Sizin BERTurk modelinizi, basit TF-IDF modelini ve Gemini'yi yan yana koyarsınız.

### Gemini anahtarı

Google AI Studio'dan ücretsiz alınır (Hafta 1, Madde 4), `.env` dosyasına yazılır. **Ücretsiz katmana gönderilen veriler Google tarafından ürün geliştirmede kullanılabilir.** Bu yüzden kullanıcı adları ve kişisel bilgiler göndermeden önce silinir. Kod bunu zaten yapıyor.

---

## 9. Git ve GitHub (3 kişi birlikte çalışma)

- **Git:** dosyalarınızın "kaydet noktalarını" (commit) tutar. Bir şey bozulursa geri dönersiniz.
- **GitHub:** bu kaydet noktalarının internetteki kopyası. Ekip buradan paylaşır.

Masaüstündeki klasörünüz şu an GitHub'a **bağlı değil**: dosyaları web sitesinden yüklediniz. Hafta 1 Madde 2'de Claude Code bunu bağlayacak. Repoyu ayrıca klonlamanıza gerek yok.

**Günlük döngü:**

| ne zaman | komut | Claude'a nasıl dersiniz |
|---|---|---|
| çalışmaya başlarken | `git pull` | "GitHub'daki son değişiklikleri çek" |
| madde bitince | `git add` + `git commit` | `/modul-bitir` zaten yapar |
| günün sonunda | `git push` | "GitHub'a push et" |

**Ekip arkadaşları:** Claude Pro sizde olduğu için Claude Code'u sizin bilgisayarınızda kullanacaksınız. Arkadaşlarınız repoyu kendi bilgisayarlarına klonlar (`git clone https://github.com/yekurtulus/yorum-analizi`). Colab çalıştırma, elle etiketleme, test etme ve sunum hazırlığı işlerini yaparlar. **Aynı dosyayı aynı anda iki kişi değiştirmesin**, yoksa çakışma (conflict) olur. Olursa Claude'a "git conflict çıktı, birlikte çözelim" deyin.

**Repo herkese açık (public).** İçine API anahtarı, ham kullanıcı yorumu veya kişisel bilgi **asla** girmemeli. `.gitignore` bunları engelliyor; yine de commit'ten önce Claude'un gösterdiği dosya listesine göz atın.

---

## 10. Claude Pro kullanım limiti

Pro planında belirli bir süre içinde kullanabileceğiniz miktar sınırlıdır. Limit dolarsa bir süre beklemeniz gerekir. Limiti korumak için:

- Her maddeden önce **`/clear`**. Uzun konuşmalar her mesajda tekrar okunur ve limiti hızlı yer.
- Hata yapıştırırken binlerce satırlık çıktının tamamını değil, **son 30–50 satırı** yapıştırın. Hata mesajı genelde en alttadır.
- Ajanları kullanın: işlerini ayrı bağlamda yapıp yalnızca özet döndürürler.
- Kritik haftalarda (Hafta 4–5) limitin dolabileceğini hesaba katın. İşleri haftanın başına yayın, son güne bırakmayın.

---

## 11. Dikkat edilecekler (detaylı)

### 11.1 Yapay zekayla kod yazarken

1. **Tek seferde tek madde.** "Bütün projeyi yaz" derseniz Claude çok büyük, test edilmemiş, anlamadığınız bir kod yığını üretir. Hata çıktığında nereden geldiğini bulamazsınız.
2. **Her kodu hemen çalıştırın.** Claude "çalışıyor" dese bile siz bir kez kendiniz çalıştırın. Asıl test sizin elinizdeki gerçek veridir.
3. **Anlamadığınız satırı sorun:** "parcalama.py'deki 23. satır ne yapıyor, neden böyle yazdın?" Hoca demo sırasında herhangi birinize "bu model nasıl eğitildi?" diye sorabilir. `inceleyici` ajanı her modül için "hocanın sorabileceği 3 soru" çıkarıyor; okuyun.
4. **Claude'a körü körüne "evet" demeyin.** İzin istediğinde ne yapacağını okuyun. Özellikle dosya silme (`rm`, `del`), `git push --force` ve `git reset --hard` gibi komutlarda dikkatli olun.
5. **Claude yanlış yöne gidiyorsa `Esc` ile durdurun** ve yönlendirin: "Dur. Daha basit yap, sınıf kullanma."
6. **Rakam uydurmasına izin vermeyin.** Model başarı rakamları yalnızca Colab'da gerçekten çalışan hücrelerden gelir. Rapordaki her sayının kaynağını bilin.
7. **Her gün GitHub'a yükleyin.** Bilgisayar bozulursa iş kaybolmasın.

### 11.2 Veri toplama ve hukuk

1. **Otomatik sayfa okuma gri alandır.** Google Haritalar ve e-ticaret sitelerinin kullanım şartları genelde otomatik veri toplamayı yasaklar. Bu proje akademik, küçük ölçekli ve veriyi yayınlamıyor. Bu çerçevenin dışına çıkmayın.
2. **Yavaş ve az:** tek seferde en fazla 200–500 yorum, istekler arası birkaç saniye bekleme, kendi bilgisayarınızdan.
3. **Engel gelirse (captcha, "olağandışı trafik") durun.** Engeli aşmaya çalışmayın. CSV yükleme yolunu kullanın.
4. **Toplanan ham veriyi paylaşmayın, GitHub'a koymayın.** `data/ham/` git dışında.
5. **Sunumda bu sınırlamayı açıkça söyleyin.** Proje planınıza göre bu artı puan getirir.
6. **YouTube resmi API kullanıyor:** en güvenilir kaynak. Günlük kotası var; aynı videoyu tekrar tekrar çekmeyin, bir kez çekip CSV'yi saklayın.
7. **Google Haritalar resmi API'si (Places) en fazla 5 yorum verir** ve yorumların saklanmasını şartlarıyla yasaklar. Bu yüzden kullanılmıyor.

### 11.3 Kişisel veri ve gizlilik

1. CSV'lere **kullanıcı adı, profil linki, fotoğraf** yazılmaz.
2. Yorum metninin içindeki e-posta, telefon ve `@kullanıcı` adları temizlikte silinir.
3. Gemini'ye yalnızca temizlenmiş metin gider.
4. API anahtarları yalnızca `.env` içinde. Sohbete yapıştırmayın, koda yazmayın, ekran paylaşırken `.env` dosyasını açmayın.
5. Repo herkese açık: commit öncesi dosya listesine bakın.

### 11.4 Model ve veri

1. **Altın test seti kutsaldır.** Eğitimde asla kullanılmaz. Kullanılırsa başarı sahte yüksek çıkar; buna "veri sızıntısı" denir ve hoca bunu sorabilir.
2. **Önce basit model (TF-IDF), sonra BERTurk.** Basit model sizin "alt çizginiz": BERTurk onu geçmiyorsa bir sorun vardır.
3. **Konu tanımlarını ekipçe erken kesinleştirin** (Hafta 2 Madde 3). Etiketleme başladıktan sonra konu eklemek/çıkarmak her şeyi baştan yaptırır.
4. **Elle etiketlerken birbirinize bakmayın.** Sonra çoğunluk oyuyla birleştirin. Anlaşamadığınız örnekler, sunumdaki "zor örnekler" slaytı için altın değerindedir.
5. **Colab veri sınırı:** 20–30 bin örneği geçmeyin, epoch 2–4. Daha fazlası süreyi uzatır ama genelde fazla bir şey kazandırmaz.
6. **Modelleri Drive'a kaydedin, git'e koymayın.** Bir BERTurk modeli ~400–450 MB; GitHub buna izin vermez.
7. **Sınıf dengesizliği:** veri setlerinde olumlu yorumlar genelde çok daha fazladır. Bu yüzden asıl metrik **macro-F1**. Sadece "accuracy %90" demek yanıltıcı olabilir.
8. **İroni deneyseldir.** Az veriyle iyi çalışmayabilir; sunumda "deneysel" diye sunulur ve vakit yoksa atlanır.
9. **Google Haritalar tarihleri yaklaşıktır** ("2 ay önce"). Bu kaynaktaki trend grafikleri yaklaşıktır; arayüzde bu yazmalı.

### 11.5 Gemini

1. **Ücretsiz kota sınırlı ve değişkendir.** Etiketlemeyi birkaç güne yayın; script kaldığı yerden devam eder.
2. **Analiz başına tek özet çağrısı** ve önbellek: aynı CSV'yi tekrar analiz edince Gemini'ye tekrar gitmez.
3. **Gemini etiketleri gürültülüdür.** İlk 40 parçayı (`--deneme`) mutlaka gözle kontrol edin. Saçma etiketler varsa istemi düzeltin, sonra devam edin.
4. Özet istemi "sadece verilen sayılara dayan, sayı uydurma" der. Yine de demo öncesi özetleri bir kez okuyun.

### 11.6 Zaman ve ekip

1. **Öncelik sırasına sadık kalın.** Geride kalırsanız ⭐'dan (bonus, ironi) başlayarak kesin. Olmazsa olmazlar (⭐⭐⭐) çalışan bir projedir.
2. **22 Aralık'tan sonra yeni özellik yok.** Son günlerde eklenen özellik, sunumda çöken özelliktir.
3. **Haftada 2 ortak oturum** (2–3 saat, ekran paylaşımlı). Klavyede kim oturursa Claude Code'u o kullanır; roller her oturumda değişsin. Herkes her modülü anlatabilmeli.
4. **`docs/NOTLAR.md`'yi okuyun.** `/modul-bitir` her modül için oraya "ne yapar, nasıl çalışır, hocanın sorabileceği soru" yazıyor. Sunuma hazırlanırken ana kaynağınız bu.

### 11.7 Sunum ve demo

1. **Canlı veri çekme sunumda çökebilir.** `data/demo_csv/` içindeki hazır CSV'lerle demo modu her zaman hazır olsun.
2. **Demo videosu kaydedin.** Hiçbir şey çalışmazsa video oynatılır.
3. **İnternetsiz deneyin.** Okul ağı sorunluysa Gemini yerine şablon özet çıkar; demo yine çalışmalı.
4. **Modellerin sunum bilgisayarında hazır olduğundan emin olun** (Drive'dan önceden indirilmiş).
5. Demoyu sunumun başına koyun; en etkili kısım o.
6. Sınırlamaları (Google Haritalar, yaklaşık tarihler, gürültülü etiketler, gri alan) kendiniz söyleyin. Hocanın bulmasını beklemeyin.

---

## 12. Bir şey ters giderse

| durum | ne yapmalı |
|---|---|
| Kod hata verdi | Hatanın son 30–50 satırını yapıştırın: "Bu hatayı aldım, nedenini açıkla ve düzelt." |
| Claude ne yaptığını anlamadım | "Az önce yaptığın değişikliği adım adım, basitçe açıkla." |
| Claude kafayı karıştırdı, aynı hatada dönüyor | `Esc` → `/clear` → maddeyi baştan, hata çıktısıyla birlikte verin. |
| Bir şey bozuldu, eski hâline dönmek istiyorum | "Son commit'ten beri yaptığın değişiklikleri göster, şu dosyayı son commit'teki hâline döndür." |
| Colab'da GPU yok uyarısı | Çalışma zamanı → Çalışma zamanı türünü değiştir → T4 GPU. GPU kotanız dolduysa birkaç saat sonra ya da başka bir ekip arkadaşının hesabıyla deneyin. |
| Site toplayıcısı bozuldu | "eticaret.py şu hatayı veriyor: …, seçicileri güncelle." Olmazsa CSV yükleme yolu. |
| Gemini 429 hatası | Kota doldu. Biraz bekleyin; özet zaten şablona düşer. |
| Kullanım limiti doldu | Bekleyin. Bu sürede elle yapılacak işleri (etiketleme, Colab, test) yapın. |

---

## 13. Önerilen iş bölümü (3 kişi)

Herkes her şeyi bilmeli, ama sorumlu kişi olması işi hızlandırır:

| kişi | sorumluluk | elle işleri |
|---|---|---|
| **1. kişi** (Claude Pro sahibi) | Claude Code oturumları, toplayıcılar, pipeline, GitHub | demo CSV'leri |
| **2. kişi** | Colab notebook'larını çalıştırma, Drive düzeni, model sonuçları | altın test seti, karşılaştırma tablosu |
| **3. kişi** | Konu tanımları, Gemini etiket kontrolü, arayüz testi | altın test seti, sunum ve demo videosu |

Altın test setini **3 kişi birlikte** (bağımsız) etiketler.
