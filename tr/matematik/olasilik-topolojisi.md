# Olasılık Topolojisi

*Bir problem nasıl manzaraya dönüşür ve o manzara cevabı nasıl belirler.*

Collaptics'de bir problem, bilgisel potansiyel `V(x)` olarak kodlanır. `V`'nin şekli — kritik noktaları, havzaları, bariyerleri, eğriliği — makinenin gerçekte üzerinde hesapladığı şeydir.

## Kritik noktalar aday cevaplardır

`V`'nin her minimumu bir aday çözümdür (bir Çöküş Tekilliği). Maksimumlar ve eyer noktaları aralarındaki bariyerlerdir. Morse teorisine göre bu kritik noktaların sayısı ve düzeni, tüm çözüm uzayının yapısını sabitler. En derin, en geniş minimum baskın cevaptır.

## Bölüşüm fonksiyonu

Ters sıcaklık `β = Ω²/D`'de durağan alan Gibbs dağılımıdır:

```
P*(x) ∝ exp(−β·V(x)),       Z(β) = ∫ exp(−β·V(x)) dx
```

Havza `k`'ye düşen olasılık kütlesi Laplace yöntemiyle:

```
p_k = Z_k / Z,    Z_k = exp(−β·V_k)·(2π/β)^(n/2)·(det H_k)^(−1/2)
```

**Bilgisel çekim** formülünü buradan alır: her havza derinlik × faz-uzayı hacmiyle çeker. Geniş-sığ bir havza, derin-dar olanı yenebilir.

## Havzalar, ayraçlar, ufuklar

- **Havza:** `−∇V` altında belirli bir minimuma akan noktalar kümesi.
- **Ayraç (separatris):** iki havzayı bölen sırt.
- **Çöküş Olay Ufku:** kaçış süresinin tutarlılık süresini aştığı iç seviye kümesi, `V_b − V_h = β⁻¹·ln(T_φ/τ₀)`. İçinde havza üyeliği taahhüt edilmiştir (bkz. [`../temeller/cokus-olay-ufku.md`](../temeller/cokus-olay-ufku.md)).

## Geometri Öklidsel değildir

İki durum arası uzaklık, Fisher–Rao manifoldunda alan örtüşmesiyle ölçülür, koordinatla değil. Gibbs alanları, KL için bir Pisagor teoreminin geçerli olduğu çiftli-düz bir üstel aile oluşturur. Bkz. [`../temeller/bilgi-geometrisi.md`](../temeller/bilgi-geometrisi.md).

## Manzarada zaman

Cevaba varmak bariyer aşmaktır. Bir `ΔV` bariyeri üzerindeki ortalama ilk-geçiş süresi Arrhenius/Kramers yasasına uyar: `τ ∝ exp(β·ΔV)`. Düz manzaralar ucuza geçilir, engebeli olanlar geçilmez. Çerçevenin karmaşıklık sınırı budur ve keskindir.

---

Bkz. [`cokus-denklemleri.md`](cokus-denklemleri.md) · [`kuramsal-temeller.md`](kuramsal-temeller.md)
