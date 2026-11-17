---
name: turkce-metin
description: Türkçe metin işleme tuzakları ve kuralları - İ/ı küçük harf dönüşümü, BERTurk cased model, emoji, tekrar harf, dil filtresi, kişisel bilgi silme, karma yorumu "ama/fakat" ile parçalama. Türkçe yorum temizleyen, parçalayan veya modele hazırlayan kod yazarken kullan.
---
# Türkçe metin işleme

## 1. Büyük/küçük harf

Python'un `str.lower()` fonksiyonu Türkçe için **yanlıştır**: `"İSTANBUL".lower()` → `"i̇stanbul"` (noktalı i + birleşik nokta), `"I".lower()` → `"i"` (doğrusu `ı`).

```python
def tr_kucuk(metin: str) -> str:
    return metin.replace("I", "ı").replace("İ", "i").lower()
```

- **BERTurk `dbmdz/bert-base-turkish-cased` büyük/küçük harf duyarlıdır.** Model girdisinde metni küçültme; yalnızca kural tabanlı kontrollerde (spam kalıpları, kelime listeleri) `tr_kucuk` kullan.

## 2. Temizlik (pipeline/temizlik.py)

Sırayla:
1. HTML etiketlerini ve fazla boşlukları sil.
2. Linkleri `[LINK]` ile değiştir (spam kuralı link sayar, o yüzden önce say sonra değiştir).
3. Kişisel bilgiyi sil: e-posta → `[EPOSTA]`, telefon → `[TELEFON]`, `@kullanici` → `[KULLANICI]`.
4. Tekrarlanan harfleri sınırla: `çoooook` → `çook` (3+ tekrarı 2'ye indir). Tamamen silme; vurgu duygu bilgisi taşır.
5. Emojileri **silme**: 😡 ve 😍 duygu taşır. BERTurk bilmediği emojiyi `[UNK]` yapar; istersen `:kızgın_yüz:` gibi metne çevir (`emoji` kütüphanesi, eklemeden önce kullanıcıya sor).
6. 2 kelimeden kısa yorumları işaretle (sil değil; spam adımı karar verir).

## 3. Türkçe filtresi

- Basit yöntem: Türkçe'ye özgü harf (ç, ğ, ı, ö, ş, ü) veya sık Türkçe kelime (ve, bir, bu, çok, ama, için, değil) oranı.
- Daha sağlam: `langdetect` veya fastText `lid.176` (eklemeden önce sor). Kısa yorumlarda dil tespiti yanılabilir; 3 kelimeden kısa yorumları dil filtresinden muaf tut.

## 4. Parçalama (pipeline/parcalama.py)

Karma duygulu yorum zıtlık bağlaçlarından bölünür:

`ama, fakat, ancak, lakin, yalnız, ne var ki, buna rağmen, oysa, gerçi`

- "Yemek güzel AMA servis yavaş" → ["Yemek güzel", "servis yavaş"].
- Nokta, ünlem ve soru işaretinden de cümlelere böl.
- 2 kelimeden kısa parçaları bir öncekiyle birleştir.
- `yalnız` bazen "sadece" anlamındadır ("yalnız gittim"); yalnızca cümle başında veya virgülden sonra geliyorsa böl.
- Her parça `yorum_id` ve `parca_no` taşır, sonuçlar yoruma geri bağlanabilsin.

## 5. Tarih

Google Haritalar: "2 hafta önce", "bir ay önce", "3 yıl önce" → bugünden çıkarılarak yaklaşık tarih; `tarih_yaklasik=True`. "bir" = 1.
