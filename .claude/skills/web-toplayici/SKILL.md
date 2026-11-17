---
name: web-toplayici
description: Playwright ile Google Haritalar, Trendyol, Hepsiburada ve Şikâyetvar sayfalarından yorum okuyan toplayıcılar için nezaket ve dayanıklılık kuralları. Web sayfasından yorum toplayan kod yazarken veya düzeltirken kullan. YouTube için değil (o resmi API kullanır).
---
# Web toplayıcı kuralları

Otomatik sayfa okuma, sitelerin kullanım şartları açısından gri alandır. Bu proje akademik, küçük ölçekli ve veriyi yayınlamıyor. Kod bu çerçevede kalmalı.

## Nezaket

- Tek seferde **en fazla 500 yorum**; varsayılan `limit=200`.
- Kaydırma/tıklama arasında rastgele **1,5–4 saniye** bekle.
- Aynı anda tek sayfa; paralel çalıştırma yok.
- Captcha, "olağandışı trafik" veya giriş sayfası görürsen **dur**, o ana kadar toplananı kaydet ve kullanıcıya "CSV yükleme yolunu kullanın" de. Engeli aşmaya çalışma (proxy, captcha çözücü vb. yok).
- Kişisel bilgi (isim, profil fotoğrafı, profil linki) okuma ve kaydetme; yalnızca yorum metni, puan, tarih.

## Dayanıklılık

- Seçicileri (CSS selector) dosyanın en üstünde `SECICILER = {...}` sözlüğünde topla. Site değişince tek yerden düzeltilir.
- Mümkünse görünür metne/role dayalı seçici kullan (`get_by_role`, `get_by_text`); otomatik üretilmiş sınıf adları (`.a8f3k`) çabuk bozulur.
- "Devamını oku" / "Daha fazla" butonlarını genişlet, yoksa yorum kesik gelir.
- Her 50 yorumda ara kayıt yap; yarıda kesilirse veri kaybolmasın.
- `headless=False` seçeneği olsun; hata ayıklarken tarayıcıyı görmek çok yardımcı olur.

## Kurulum (Windows)

```powershell
pip install playwright
python -m playwright install chromium
```

## Platform notları

- **Google Haritalar**: resmi Places API en fazla 5 yorum verir, bu yüzden kullanılmaz. Mekan sayfası → "Yorumlar" sekmesi → "En yeni" sıralaması → yorum panelini kaydır. Tarihler "2 ay önce" biçimindedir → `turkce-metin` skill'iyle yaklaşık tarihe çevir, `tarih_yaklasik=True`.
- **Trendyol / Hepsiburada**: ürün sayfasındaki "Tüm değerlendirmeler" sayfası. Puan yıldız sayısından okunur.
- **Şikâyetvar**: bonus; puan yok, alan `urun`.

## Sunum günü

Canlı toplama sunumda çökebilir. Her platform için önceden toplanmış bir CSV `data/demo_csv/` içinde hazır olmalı.
