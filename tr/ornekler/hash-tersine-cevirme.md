# Örnek: Hash Tersine Çevirme — dürüst bir olumsuz sonuç

Collaptics'nin bir kriptografik hash'i tersine çevirdiğini hayal etmek caziptir: hedef hash'i bir olasılık topolojisine çevir, aday uzayını yokuş aşağı bırak, alanın ön-görüntüye çökmesini izle. Bu **çalışmaz** — ve nedenini açıkça söylemek değerlidir, çünkü o neden, Collaptics'nin başka yerlerde çalışmasının da nedenidir.

## Kurulum

SHA-256'yı tersine çevirmek, verilen bir `h` için `SHA256(x) = h` olacak bir `x` bulmaktır. Naif fikir: "hedef hash'ten uzaklığı" bir potansiyel `V(x)` olarak kodla ve Çöküş Akışı'nı çalıştır.

## Neden başarısız olur

Kriptografik bir hash, Collaptics'nin sömürdüğü yapıyı *tam olarak* yok etmek için tasarlanır.

- **Gradyan yok.** Çığ (avalanche) özelliği, tek bir girdi bitini çevirmenin çıktı bitlerinin yaklaşık yarısını değiştirmesini garanti eder. Komşu girdiler tamamen ilgisiz çıktılar verir. Yani `V(x)` **düzdür** — cevaba işaret eden bir eğim yoktur.
- **Havza yok.** Düz manzarada her havza çekimi `Γ_k` aynıdır. İçine düşülecek bir Çöküş Tekilliği yoktur.
- **Çöküş rastgele aramaya iner.** `Ω`, düz `V` üzerinde kullanılabilir sürüklenme sağlamayınca Çöküş Akışı yönsüz difüzyona — tam olarak kaba kuvvete, hızlanma olmadan — iner.

Bu, belirli bir uygulamanın sınırı değildir. Yapısaldır: Collaptics'nin avantajı *gradyanın kendisidir* ve güvenli bir hash, o gradyanın kasıtlı yokluğudur.

## Ders

Çerçevenin dürüst sınırı (bkz. [`../temeller/bilgisel-cokus.md`](../temeller/bilgisel-cokus.md)), Collaptics'nin **düz, geçilebilir manzaralarda** bir enerji/verim avantajı olduğunu, evrensel bir çözücü olmadığını söyler. Hash tersine çevirme, o çizginin yanlış tarafındaki en temiz durumdur. Collaptics bir hash'i kırabilseydi, o hash zaten gradyan inişiyle kırılmış olurdu — ki değil.

Bu olumsuz durum, çerçevenin sınırını olumlu örnekler kadar keskin biçimde çizer.

---

Bkz. [`protein-katlanmasi.md`](protein-katlanmasi.md) · [`dil-modeli-cikarimi.md`](dil-modeli-cikarimi.md)
