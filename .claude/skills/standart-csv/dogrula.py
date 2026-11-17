"""Standart yorum CSV'sini doğrular.

Kullanım:
    python .claude/skills/standart-csv/dogrula.py dosya.csv
"""
import re
import sys

import pandas as pd

SUTUNLAR = ["platform", "kaynak_url", "yorum", "tarih", "puan", "alan"]
PLATFORMLAR = {"youtube", "google_maps", "trendyol", "hepsiburada", "sikayetvar", "csv"}
ALANLAR = {"urun", "mekan", "video"}
TARIH_DESENI = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def dogrula(df: pd.DataFrame) -> list[str]:
    """DataFrame'i kontrol eder, bulduğu sorunları liste olarak döndürür (boş liste = geçerli)."""
    hatalar = []

    # 1) Zorunlu sütunlar var mı?
    eksik = [s for s in SUTUNLAR if s not in df.columns]
    if eksik:
        return [f"Eksik sütun(lar): {eksik}"]

    if df.empty:
        return ["CSV boş: hiç yorum yok."]

    # 2) Yorum boş olmamalı
    bos = df["yorum"].isna() | (df["yorum"].astype(str).str.strip() == "")
    if bos.any():
        hatalar.append(f"{int(bos.sum())} satırda yorum boş.")

    # 3) Platform ve alan izin verilen değerlerden olmalı
    yanlis_platform = set(df["platform"].dropna().astype(str)) - PLATFORMLAR
    if yanlis_platform:
        hatalar.append(f"Bilinmeyen platform değerleri: {sorted(yanlis_platform)}")
    yanlis_alan = set(df["alan"].dropna().astype(str)) - ALANLAR
    if yanlis_alan or df["alan"].isna().any():
        hatalar.append(f"Alan yalnızca {sorted(ALANLAR)} olabilir. Hatalı: {sorted(yanlis_alan) or 'boş değer'}")

    # 4) Tarih YYYY-MM-DD ya da boş
    tarihler = df["tarih"].dropna().astype(str)
    tarihler = tarihler[tarihler.str.strip() != ""]
    hatali_tarih = tarihler[~tarihler.str.match(TARIH_DESENI)]
    if len(hatali_tarih):
        hatalar.append(f"{len(hatali_tarih)} tarih YYYY-MM-DD biçiminde değil (ör. {hatali_tarih.iloc[0]!r}).")

    # 5) Puan 1-5 ya da boş
    puan = pd.to_numeric(df["puan"], errors="coerce")
    dolu = df["puan"].notna() & (df["puan"].astype(str).str.strip() != "")
    hatali_puan = dolu & ~puan.between(1, 5)
    if hatali_puan.any():
        hatalar.append(f"{int(hatali_puan.sum())} satırda puan 1-5 arasında değil.")

    # 6) Tekrar eden yorumlar
    tekrar = df.duplicated(subset=["platform", "yorum"]).sum()
    if tekrar:
        hatalar.append(f"{int(tekrar)} tekrar eden yorum var (drop_duplicates ile silin).")

    return hatalar


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    veri = pd.read_csv(sys.argv[1], encoding="utf-8-sig", dtype=str)
    sorunlar = dogrula(veri)
    if sorunlar:
        print("SORUNLAR:")
        for s in sorunlar:
            print(" -", s)
        sys.exit(1)
    print(f"Geçerli standart CSV: {len(veri)} yorum.")
