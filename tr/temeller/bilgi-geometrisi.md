# Bilgi Geometrisi

*Cevaplar arası uzaklık koordinatla değil, örtüşmeyle ölçülür.*

Collaptics'de durum uzayı sıradan koordinat uzayı **değildir**. Olasılık alanlarının **istatistiksel manifoldudur** ve üzerindeki uzaklık Öklidsel değildir.

İki cevap düşünün:

```
Berlin        Münih
```

Aralarındaki uzaklık **600 kilometre değildir**. Onları temsil eden iki olasılık alanının *ne kadar az örtüştüğüdür*. Havzaları ayrık olan iki cevap, koordinatları neredeyse çakışsa bile azami uzaktır; alanları birbirine karışan iki cevap, koordinatları uzak olsa bile yakındır.

## Metrik

Doğal metrik **Fisher–Rao metriğidir** — çözme gücü `Σ`'yı tanımlayan aynı Fisher bilgisi:

```
g_ij(θ) = E[ ∂_i ln P · ∂_j ln P ]
```

İki aday cevap `A` ve `B` arasındaki uzaklık, alanlarının **örtüşmesidir**, örn. Bhattacharyya / sadakat ölçüsü:

```
d(A, B) = arccos ∫ √( P_A(x) · P_B(x) ) dx
```

## Olasılık eğriliği

Manifold eğridir (Amari'nin α-geometrisi). Kritik olarak, çöküş alanları `P* ∝ exp(−βV)` bir *üstel aile* oluşturur; bu da durağan çöküşlerin manifoldunu **çiftli-düz** kılar — KL ıraksaması için genelleştirilmiş bir Pisagor teoreminin geçerli olduğu bir uzay.

"Olasılığın geometrisi" tam olarak şu demektir: düz bir çöküş-altmanifolduna sahip eğri bir bilgi manifoldu; üzerinde:

- **Bilgisel çekim** jeodezik harekettir,
- **Çöküş** doğal-gradyan inişidir (`dθ/dt = −Ω²·g⁻¹·∇V`),
- **Çözme gücü `Σ`** tekillikteki metriktir.

## Öngörü

İki çekici, koordinat uzaklıklarıyla değil, alan **örtüşmeleriyle** orantılı olarak karıştırılır. Eşit koordinat aralığına ama örtüşen / ayrık havzalara sahip iki kuyu kurun; çöküş hatası örtüşmeyi izlemelidir. Öklidsel uzaklık kullanan her model yanlışlanır.

---

İlgili: [`bilgisel-cekim.md`](bilgisel-cekim.md) · [`../matematik/olasilik-topolojisi.md`](../matematik/olasilik-topolojisi.md)
