---
name: modul-bitir
description: Bir modül veya plan maddesi bittiğinde uygulanacak kapanış adımları - test çalıştırma, inceleyici ajanı, NOTLAR.md'ye öğretici özet, plan maddesini işaretleme, commit. Kullanıcı "/modul-bitir" yazdığında veya bir madde tamamlandığında kullan.
---
# Modül bitirme kontrol listesi

Sırayla yap, her adımın sonucunu kısaca kullanıcıya yaz:

1. **Test**: Modülün testini veya örnek çalıştırmasını çalıştır. Başarısızsa dur, düzelt, tekrar çalıştır.
2. **İnceleme**: `inceleyici` ajanını bu modülün dosyalarıyla çağır. Ciddi sorun varsa kullanıcıya göster ve düzeltmeyi öner.
3. **Notlar**: `docs/NOTLAR.md` dosyasına şu biçimde ekle (dosya yoksa oluştur):

   ```markdown
   ## <Tarih> – <Modül adı> (Hafta X, Madde Y)
   **Ne yapar:** 2-3 cümle.
   **Nasıl çalıştırılır:** komut.
   **Önemli kararlar:** neden bu yöntem seçildi.
   **Hocanın sorabileceği soru:** soru – kısa cevap.
   ```

4. **Plan**: `docs/HAFTALIK_PLAN.md` içinde ilgili maddenin kutusunu `- [ ]` → `- [x]` yap.
5. **Commit**: değişen dosyaları göster, Türkçe commit mesajı öner (ör. `YouTube toplayıcı eklendi`). Kullanıcı onaylarsa `git add` + `git commit`; **push için ayrıca sor**.
6. **Sıradaki madde**: planda bir sonraki maddeyi adıyla söyle, ama kendiliğinden başlama.
