# Çok Platformlu Müşteri Yorumu Analiz Sistemi

Bu dosya Claude Code'un her oturumda okuduğu proje hafızasıdır. Değiştirirken kısa ve net tut.

## Proje

- Yapay Zeka dersi projesi. 3 kişilik öğrenci ekibi, makine öğrenmesi deneyimi az.
- **Sunum + canlı demo: 31 Aralık 2026. Hedef bitiş: 24 Aralık 2026.** 22 Aralık'tan sonra yeni özellik yok, sadece hata düzeltme.
- Bütçe: yalnızca ücretsiz araçlar (Colab, Hugging Face, YouTube Data API, Gemini ücretsiz katman, Streamlit).
- Dil: Türkçe yorumlar, Türkçe arayüz, Türkçe kod yorumları.
- Ayrıntılı proje planı: `docs/Proje_Plani_Yorum_Analizi.pdf`. Adım adım iş listesi: `docs/HAFTALIK_PLAN.md`.

## Ana mimari kural (asla bozma)

Hangi platformdan gelirse gelsin her yorum önce **standart CSV**'ye dönüşür. Analiz kodu yalnızca bu CSV'yi tanır.

| sütun | tip | açıklama |
|---|---|---|
| platform | metin | `youtube`, `google_maps`, `trendyol`, `hepsiburada`, `sikayetvar`, `csv` |
| kaynak_url | metin | yorumun alındığı sayfa/video linki |
| yorum | metin | yorumun ham metni |
| tarih | metin | `YYYY-MM-DD`. Bilinmiyorsa boş. Yaklaşık tarihse `tarih_yaklasik=True` (isteğe bağlı ek sütun) |
| puan | sayı / boş | 1–5 yıldız varsa, yoksa boş |
| alan | metin | `urun`, `mekan`, `video` |

- Dosya kodlaması **UTF-8**, ayırıcı virgül. Örnek: `data/ornek_standart.csv`.
- Doğrulama: `standart-csv` skill'indeki kurallara uy. Her toplayıcı çıktısını doğrula.
- Kullanıcı adı, profil linki gibi kişisel bilgiler CSV'ye **yazılmaz**.

## Akış (pipeline)

```
[Link veya CSV] → collectors/ → standart CSV
  → pipeline/temizlik.py   (temizlik + Türkçe filtresi)
  → pipeline/spam.py       (şüpheli yorum işareti)
  → pipeline/parcalama.py  ("yemek güzel AMA servis yavaş" → 2 parça)
  → duygu modeli (BERTurk) → ironi kontrolü → konu modeli (alana göre)
  → pipeline/analiz.py     (skor, konu tablosu, güven, aylık trend; analyze(csv) burada)
  → pipeline/ozet.py       (Gemini ile "Beğenilenler / Beğenilmeyenler", yedek: şablon)
  → app/streamlit_app.py
```

## Klasörler

- `collectors/` – youtube.py, google_maps.py, eticaret.py (her biri standart CSV üretir)
- `pipeline/` – temizlik, spam, parcalama, analiz, ozet
- `models/egitim_notebooklari/` – **Colab'da çalıştırılacak** `.ipynb` dosyaları
- `models/kaydedilmis_modeller/` – eğitilmiş modeller (büyük dosyalar git'e girmez, Google Drive'da tutulur)
- `data/ham/` toplanan ham veri (git'e girmez) · `data/etiketli/` etiketli veri · `data/demo_csv/` sunum için hazır CSV'ler
- `app/` – Streamlit arayüzü (4 sayfa: Analiz Et · Sonuç Paneli · Aylık Karşılaştırma · Model Hakkında)
- `tests/` – küçük testler · `docs/` – plan, rehber, `NOTLAR.md`

## Modeller

- Duygu: `dbmdz/bert-base-turkish-cased` ince ayar → olumlu / olumsuz / nötr
- Konu: BERTurk, çok etiketli (multi-label), her alan için ayrı model
  - Ürün: kalite, fiyat_performans, kargo_teslimat, paketleme, satici_iletisim, iade_degisim
  - Mekan: lezzet_urun, hizmet_personel, fiyat, ortam_temizlik, konum_ulasim, bekleme_suresi
  - Video: icerik_bilgi, anlatim, ses_goruntu, sure_tempo
- İroni: BERTurk ikili sınıflandırma (deneysel). İronikse görünen olumlu duygu olumsuza çevrilir.
- Spam: kurallar + basit model. Arayüzde "sahte" değil **"şüpheli"** yazılır.
- Karşılaştırma: aynı altın test setinde TF-IDF + Lojistik Regresyon vs BERTurk vs Gemini.
- Hesaplar: skor = 10 × olumlu / (olumlu + olumsuz); nötr ve şüpheli hariç. Güven: <30 düşük, 30–100 orta, >100 yüksek. Bir ayda <20 yorum varsa uyarı.

## Ortam

- Kullanıcıların bilgisayarı **Windows**. Python 3.11+, sanal ortam `.venv`. Komutları Windows'ta çalışacak şekilde ver (PowerShell).
- Model eğitimi ve GPU gerektiren işler **bilgisayarda çalıştırılmaz**; `colab-notebook` skill'ine göre notebook yazılır, kullanıcı Colab'da çalıştırır ve sonucu geri yapıştırır.
- API anahtarları `.env` dosyasında (`YOUTUBE_API_KEY`, `GEMINI_API_KEY`). Koda asla yazılmaz, `.env` git'e girmez.
- Bağımlılıklar `requirements.txt`'te. Yeni kütüphane eklemeden önce kullanıcıya sor ve nedenini söyle.

## Çalışma kuralları

1. **Bir seferde tek modül.** Kullanıcı hangi maddeyi istediyse yalnızca onu yap; sonraki maddeye kendiliğinden geçme.
2. Büyük bir işe başlamadan önce kısa bir plan göster (hangi dosyalar, ne yapacak), onay al.
3. Her modülde: çalıştırılabilir küçük bir test ya da `if __name__ == "__main__":` örneği ekle, kullanıcıya **hangi komutla deneyeceğini** yaz.
4. Kod yorumları Türkçe ve öğretici olsun; kullanıcılar ML'e yeni. Fonksiyonlara kısa docstring yaz.
5. Basit tut: sınıf hiyerarşisi, gereksiz soyutlama, gereksiz kütüphane yok.
6. Hata çıktısı yapıştırılırsa önce nedenini açıkla, sonra düzelt.
7. Modül bitince `modul-bitir` skill'ini uygula (test, açıklama, `docs/NOTLAR.md`, commit önerisi).
8. Git: anlamlı Türkçe commit mesajı; `git push` yapmadan önce kullanıcıya sor.

## Kırmızı çizgiler

- Gemini'ye (veya herhangi bir dış API'ye) kullanıcı adı, e-posta, telefon, profil linki **gönderme**; önce `temizlik.py` ile sil.
- Toplanan ham veriyi ve büyük model dosyalarını git'e ekleme (`.gitignore` hazır).
- Web toplayıcılarda yavaş ve az istek (`web-toplayici` skill'i). Engel/captcha aşmaya çalışma; CSV yedeğine yönlendir.
- Altın test setini (elle etiketlenen ~150 parça/alan) eğitimde **kullanma**; yalnızca ölçüm için.
- Sonuçları uydurma: metrikler gerçekten çalıştırılmış koddan gelir.

## Öncelikler (geride kalınırsa alttan kes)

1. Olmazsa olmaz: CSV yükleme, YouTube toplayıcı, duygu modeli, konu modeli, skor, özet, Streamlit
2. Olmalı: Google Haritalar ve e-ticaret toplayıcıları, spam, trend ve aylık karşılaştırma, model karşılaştırması
3. Olsa iyi: ironi modülü (deneysel)
4. Bonus: firma adıyla arama, Şikâyetvar

## Ajanlar ve skill'ler

- Ajanlar (`.claude/agents/`): `toplayici`, `model-egitici`, `pipeline-muhendisi`, `arayuz-gelistirici`, `inceleyici`.
- Skill'ler (`.claude/skills/`): `standart-csv`, `turkce-metin`, `web-toplayici`, `colab-notebook`, `gemini-kullanimi`, `model-degerlendirme`, `modul-bitir`.
- İş ilgili ajanın uzmanlık alanındaysa ona devret. Her modülden sonra `inceleyici` ile gözden geçir.
