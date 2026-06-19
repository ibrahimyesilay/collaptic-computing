# Çöküş Tekilliği

*Bir bilgisel topolojideki en derin çekici — cevabın kendisi.*

Her problemin merkezinde özel bir yapı vardır: bilgisel potansiyel `V(x)`'in baskın minimumu olan **Çöküş Tekilliği**. Rolü bir kara deliğinkine benzer.

Kara delik, maddenin nereye gitmesi gerektiğini hesaplamaz. Uzayzamanı büker, böylece madde doğal olarak içeri düşer. Benzer biçimde en güçlü çözüm en derin bilgisel kuyu olur; olasılık ona doğru akar; çözüm belirir.

## Hiyerarşi

Bir tekillik tek başına durmaz. Çöküş iç içe dört yapıdan geçer:

```
Bilgi Alanı  →  Çekim Havzası  →  Çöküş Olay Ufku  →  Çöküş Tekilliği
  (bulut)        (içeri akar)       (geçiş-yok noktası)        (cevap)
```

- **Alan**, aday çözümlerin geniş, yüksek-entropili bulutudur.
- **Havza**, tek bir cevaba akan bölgedir (bkz. [`bilgisel-cekim.md`](bilgisel-cekim.md)).
- **Olay ufku**, çöküşün geri döndürülemez hâle geldiği yerdir (bkz. [`cokus-olay-ufku.md`](cokus-olay-ufku.md)).
- **Tekillik**, kuyunun dibidir — beliren çözüm.

## Onu "cevap" yapan ne

Bir tekillik yalnızca derin değildir; en büyük **havza çekimi** `Γ_k`'ye (derinlik × genişlik) sahip çekicidir. Bir altkatmanda birçok tekillik bir arada bulunabilir. Birim hacimdeki kararlı tekillik sayısı — **Tekillik Yoğunluğu** — Collaptics'nin FLOPS yerine önerdiği iki metrikten biridir.

## Dürüst sınır

Çerçeve, *erişilebilir baskın* tekilliği çözer; illa *küresel* optimumu değil. Havzalar arası bariyerler yüksekse alan, optimum-altı bir kuyuda tuzaklanabilir (doğrulandı: test P5b). Collaptics, zor optimizasyon problemlerinin bedava çözücüsü değildir — bkz. [`../ornekler/hash-tersine-cevirme.md`](../ornekler/hash-tersine-cevirme.md).

---

İlgili: [`bilgisel-cokus.md`](bilgisel-cokus.md) · [`cokus-olay-ufku.md`](cokus-olay-ufku.md)
