---
name: model-degerlendirme
description: Modelleri altın test setinde ölçme ve karşılaştırma kuralları - accuracy, macro-F1, sınıf bazında rapor, karışıklık matrisi, TF-IDF vs BERTurk vs Gemini tablosu, hata analizi. Bir modelin başarısını ölçerken veya Model Hakkında sayfası için tablo üretirken kullan.
---
# Model değerlendirme

## Altın test seti

- Her alan (ürün, mekan, video) için ~150 yorum parçası, **3 ekip üyesi tarafından elle** etiketlenir.
- Dosya: `data/etiketli/altin_<alan>.csv` – sütunlar: `parca`, `duygu`, `konular` (noktalı virgülle ayrılmış), `ironik`.
- **Eğitimde asla kullanılmaz.** Eğitim verisinde aynı metin varsa eğitimden çıkar.
- Etiket anlaşmazlığında çoğunluk oyu.

## Metrikler

- **Duygu** (3 sınıf): accuracy + **macro-F1** (sınıflar dengesiz olabilir; asıl metrik macro-F1) + `classification_report`.
- **Konu** (çok etiketli): micro-F1, macro-F1, konu bazında F1.
- **İroni** (ikili): accuracy, F1, karışıklık matrisi.
- Karışıklık matrisini görsel olarak kaydet (`seaborn`/`matplotlib`), sunumda kullanılır.

## Karşılaştırma tablosu

Aynı altın test setinde, aynı formatta:

| Yöntem | Duygu Acc | Duygu Macro-F1 | Konu Micro-F1 | Hız (parça/sn) | Maliyet |
|---|---|---|---|---|---|
| TF-IDF + Lojistik Regresyon | | | | | ücretsiz, çok hızlı |
| BERTurk (bizim) | | | | | ücretsiz, GPU ile eğitim |
| Gemini (doğrudan) | | | | | kotalı API |
| Sengil/ABSA-Turkish (hazır, sadece mekan) | | | | | ücretsiz |

Tabloyu `models/sonuclar/karsilastirma.csv` olarak kaydet; Streamlit "Model Hakkında" sayfası buradan okur.

## Hata analizi

Her modelden **yanlış tahmin edilen 10 örneği** `models/sonuclar/hatalar_<model>.csv` olarak kaydet (metin, gerçek, tahmin). Sunumda "modelin yanıldığı ilginç örnekler" slaytı buradan çıkar: ironi, olumsuzlama ("fena değil"), karma yorumlar.

## Dürüstlük

Rakamları yalnızca gerçekten çalıştırılmış koddan al. Sonuç kötüyse kötü yaz; sunumda nedenini açıklamak puan getirir.
