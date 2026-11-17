# Çok Platformlu Müşteri Yorumu Analiz Sistemi

YouTube, Google Haritalar, e-ticaret siteleri ve CSV/Excel'den gelen Türkçe yorumları ortak bir formata çeviren; neyin beğenilip neyin beğenilmediğini çıkaran ve bunu skor, konu tablosu, trend ve özetle sunan sistem. Yapay Zeka dersi projesi.

## Nasıl çalışır?

```
Link veya CSV → Toplayıcı → standart CSV → temizlik → spam filtresi → parçalama
→ duygu (BERTurk) → ironi → konu → skor / trend → Gemini özeti → Streamlit
```

## Kurulum (Windows)

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # sonra .env içine API anahtarlarını yazın
```

## Çalıştırma

```powershell
streamlit run app/streamlit_app.py
```

## Klasörler

| klasör | içerik |
|---|---|
| `collectors/` | platformlardan yorum toplayıp standart CSV üreten scriptler |
| `pipeline/` | temizlik, spam, parçalama, analiz, özet |
| `models/` | Colab eğitim notebook'ları ve kaydedilmiş modeller |
| `data/` | ham, etiketli ve demo CSV'leri |
| `app/` | Streamlit arayüzü |
| `docs/` | proje planı, haftalık plan, rehber, notlar |

## Ekip için

- Yeni başlıyorsanız önce `docs/REHBER.md`, sonra `docs/HAFTALIK_PLAN.md`.
- Claude Code bu repodaki `CLAUDE.md`, `.claude/agents/` ve `.claude/skills/` dosyalarını otomatik kullanır.

## Sınırlamalar

Web sayfalarından otomatik yorum okumak sitelerin kullanım şartları açısından gri alandadır. Bu proje akademik amaçlı ve küçük ölçeklidir; toplanan ham veri paylaşılmaz.
