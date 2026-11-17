---
name: colab-notebook
description: Google Colab'da çalışacak model eğitim notebook'u (.ipynb) yazma kuralları - GPU kontrolü, Drive bağlama, veri yükleme, BERTurk ince ayarı, kaydetme, sonuç tablosu. Model eğitimi veya GPU gerektiren bir iş için notebook yazarken kullan.
---
# Colab notebook kuralları

Kullanıcıların bilgisayarında GPU yok. Eğitim **Google Colab**'da yapılır: Claude notebook'u yazar, kullanıcı Colab'a yükleyip çalıştırır, çıktıyı geri yapıştırır.

## Dosya

- Yer: `models/egitim_notebooklari/NN_konu.ipynb` (ör. `01_duygu_tfidf.ipynb`, `02_duygu_berturk.ipynb`).
- Geçerli Jupyter JSON'u yaz (nbformat 4). Çıktı hücreleri boş olsun.
- **Her kod hücresinden önce** ne yaptığını 1-3 cümleyle anlatan Türkçe markdown hücresi.

## Standart hücre sırası

1. **Başlık**: amaç, girdi, çıktı, tahmini süre.
2. **GPU kontrolü**: `!nvidia-smi` ve `torch.cuda.is_available()`; GPU yoksa "Çalışma zamanı → Çalışma zamanı türünü değiştir → T4 GPU" uyarısı yazdır.
3. **Kurulum**: `!pip install -q transformers datasets evaluate scikit-learn` (Colab'da zaten olanları tekrar kurma).
4. **Drive bağlama**: `from google.colab import drive; drive.mount('/content/drive')`. Proje klasörü: `/content/drive/MyDrive/yorum-analizi/`.
5. **Ayarlar** hücresi: tüm sabitler tek yerde (`MODEL_ADI`, `MAKS_UZUNLUK=128`, `EPOCH=3`, `BATCH=16`, `ORNEK_SAYISI=20000`, `TOHUM=42`).
6. **Veri yükleme ve inceleme**: ilk 5 satır, sınıf dağılımı.
7. **Bölme**: eğitim/doğrulama (stratify). Altın test seti ayrı dosyadan gelir, eğitime karışmaz.
8. **Eğitim**: Hugging Face `Trainer`; `fp16=True` (GPU varsa), her epoch'ta değerlendirme, en iyi modeli tut.
9. **Değerlendirme**: `model-degerlendirme` skill'indeki tablo.
10. **Kaydetme**: model + tokenizer → `/content/drive/MyDrive/yorum-analizi/modeller/<ad>/`; ayrıca metrikleri `sonuclar.json` olarak kaydet.
11. **Deneme**: 5 elle yazılmış Türkçe cümleyle tahmin göster.

## Limitler

- Colab ücretsiz GPU süresi sınırlıdır ve oturum ~90 dk hareketsizlikte kapanabilir. Veri 20–30 bin örneği geçmesin, epoch 2–4.
- Kopma ihtimaline karşı `save_strategy="epoch"` ile Drive'a ara kayıt.
- `MAKS_UZUNLUK=128` yorum parçaları için yeterli; artırmak süreyi uzatır.

## Kullanıcıya anlatım

Notebook'u yazdıktan sonra şu adımları ver: colab.research.google.com → Dosya → Not defteri yükle → GPU seç → hücreleri sırayla çalıştır (Shift+Enter) → son hücrelerin çıktısını buraya yapıştır.
