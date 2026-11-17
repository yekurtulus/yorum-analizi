---
name: gemini-kullanimi
description: Gemini API'yi (ücretsiz katman) bu projede kullanma kuralları - toplu ön etiketleme, özet üretimi, model karşılaştırması için doğrudan tahmin; kota koruma, önbellek, kişisel bilgi silme, JSON çıktı, şablon yedeği. Gemini çağıran kod yazarken kullan.
---
# Gemini kullanımı

Gemini bu projede **3 iş** için kullanılır, analiz için değil:

1. **Ön etiketleme** (eğitim verisi üretmek): yorum parçalarına konu ve duygu etiketi.
2. **Özet**: hazır istatistikleri "Beğenilenler / Beğenilmeyenler" maddelerine çevirmek.
3. **Karşılaştırma**: altın test setinde "Gemini doğrudan cevap verirse ne kadar başarılı?" ölçümü.

Asıl analizi projenin kendi modelleri yapar.

## Kurulum

```powershell
pip install google-genai
```

Anahtar `.env` içinde `GEMINI_API_KEY`. Model adını koda gömme; `GEMINI_MODEL` ayarı olsun (varsayılan: ücretsiz katmandaki güncel Flash modeli). Ücretsiz katman limitleri değişebilir; limit hatası (429) gelirse bekle ve tekrar dene.

## Kurallar

- **Kişisel bilgi gönderme**: ücretsiz katmandaki istekler Google tarafından ürün geliştirmede kullanılabilir. Göndermeden önce `temizlik.py` ile isim/e-posta/telefon/kullanıcı adı silinmiş olmalı.
- **Toplu gönder**: etiketlemede tek istekte 30–50 parça. Her parçaya numara ver, cevabı numarayla eşleştir.
- **JSON iste**: `response_mime_type="application/json"` ve açık şema. Cevabı `json.loads` ile oku; bozuksa o grubu bir kez tekrar dene, yine bozuksa atla ve logla.
- **Sıcaklık 0**: etiketlemede tutarlılık için `temperature=0`.
- **Önbellek**: aynı girdi için tekrar istek atma. Etiketlemede sonuçları `data/etiketli/gemini_<alan>.csv`'ye ekle ve kaldığı yerden devam et; özette girdi hash'ini anahtar yapıp `ozet_onbellek/` klasörüne kaydet.
- **Bekleme**: istekler arasında 4–6 saniye (dakikalık limit).
- **Özet: analiz başına tek çağrı.** API hata verirse veya kota dolarsa şablon özete düş:
  "En çok beğenilen: {en_olumlu_konu} (%{oran}). En çok şikâyet edilen: {en_olumsuz_konu} (%{oran})."

## Etiketleme istemi (prompt) iskeleti

```
Aşağıda {alan} alanından numaralı Türkçe yorum parçaları var.
Her parça için:
- duygu: "olumlu" | "olumsuz" | "notr"
- konular: şu listeden uygun olanlar (birden fazla olabilir, hiçbiri değilse boş): {konu_listesi}
- ironik: true | false
Yalnızca JSON dizi döndür: [{"no": 1, "duygu": "...", "konular": [...], "ironik": false}, ...]

1. ...
2. ...
```

## Özet istemi kuralı

Gemini'ye ham yorumların hepsini değil, **hazır istatistikleri** ve konu başına en fazla 3 örnek parçayı gönder. İstem: "Sadece verilen sayılara dayan, sayı uydurma, 3-5 madde Beğenilenler, 3-5 madde Beğenilmeyenler yaz."

## Raporda nasıl anlatılır

Ön etiketleme yöntemi: "LLM destekli zayıf denetimle (weak supervision) veri oluşturma". Gemini etiketleri gürültülüdür; bu yüzden başarı, elle etiketlenmiş altın test setinde ölçülür.
