---
name: standart-csv
description: Projenin standart yorum CSV formatı (platform, kaynak_url, yorum, tarih, puan, alan) ve doğrulama kuralları. Bir toplayıcı CSV ürettiğinde, kullanıcı CSV/Excel yüklediğinde veya pipeline bir CSV okuduğunda kullan.
---
# Standart CSV

Projede her yorum bu formata dönüşür. Analiz kodu başka format tanımaz.

## Sütunlar (bu sırayla)

| sütun | zorunlu | kural |
|---|---|---|
| platform | evet | `youtube`, `google_maps`, `trendyol`, `hepsiburada`, `sikayetvar`, `csv` |
| kaynak_url | evet | link; CSV yüklemede dosya adı olabilir |
| yorum | evet | boş olamaz; ham metin (temizlik pipeline'da yapılır) |
| tarih | hayır | `YYYY-MM-DD` ya da boş |
| puan | hayır | 1–5 arası tam sayı ya da boş |
| alan | evet | `urun`, `mekan`, `video` |

İsteğe bağlı ek sütunlar: `tarih_yaklasik` (True/False, Google Haritalar'ın "2 ay önce" tarihleri için), `yorum_id`.

## Kurallar

- UTF-8 kodlama, virgül ayırıcı. Excel'de Türkçe karakter bozulmasın diye kaydederken `encoding="utf-8-sig"` kullan.
- Kullanıcı adı, profil linki, e-posta, telefon **yer almaz**.
- Birebir aynı (platform, yorum) satırları tekrar etmez.
- Dosya adı: `data/ham/<platform>_<YYYYMMDD_HHMM>.csv`.

## Doğrulama

Bu klasördeki `dogrula.py` dosyasını kullan:

```powershell
python .claude/skills/standart-csv/dogrula.py data/ornek_standart.csv
```

Kodun içinden:

```python
import sys; sys.path.append(".claude/skills/standart-csv")
from dogrula import dogrula
hatalar = dogrula(df)   # boş liste = geçerli
```

## Kullanıcının yüklediği CSV/Excel

Sütun adları farklıysa (ör. `Yorum`, `comment`, `text`) eşleştirme sözlüğüyle `yorum` sütununa çevir; eşleşme bulunamazsa kullanıcıya hangi sütunun yorum olduğunu sor (arayüzde açılır menü).
