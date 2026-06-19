# Kollapton

*Collaptics'nin temel bilgi birimi.*

Bit bir noktadır: ya `0`'dır ya `1`. **Kollapton** bir buluttur: tek bir değer yerine bir *eğilim* — bütün bir olasılık dağılımı — saklar.

```
bit:       x = 5
Kollapton:  x ≈ { 5 : %71,  6 : %18,  4 : %11 }
```

## Durum

Bir Kollapton altı nicelikle tanımlanır:

```
C = {
  μ : beklenen durum
  σ : belirsizlik
  ρ : güven yoğunluğu
  φ : faz
  ω : rezonans imzası
  τ : yönelimsel eğilim
}
```

Bunlardan ikisi — rezonans imzası `ω` ve güven yoğunluğu `ρ` — tüm çerçeveyi yöneten **tutarlı rezonans** `Ω = ρ·ω`'da birleşir (bkz. [`../matematik/cokus-denklemleri.md`](../matematik/cokus-denklemleri.md)).

## Neden değer değil, dağılım

Gerçeklik nadiren ikilidir. Dil, biyoloji, piyasalar ve zekâ olasılık ve eğilimlerle işler. Bugünün yapay zekâsı zaten her şeyi olasılık dağılımı olarak temsil eder — ama onları *taklit etmek* için trilyonlarca ikili işlem harcar. Kollapton, dağılımı altkatmanın fiziksel durumunda **doğrudan** temsil eder.

## Fiziksel gerçekleme

Kollapton donanım arayan bir soyutlama değildir. Birçok fiziksel durum doğası gereği çok-değerli ve analogdur; istisna olan, silisyumun iki seviyeli yük kuyusudur:

- bir **ferroelektrik kutuplanma** (sürekli, çok-bölgeli),
- bir **manyetik yönelim** (doğal rezonans frekanslı bir vektör),
- bir **optik osilatör fazı** (sürekli, tutarlı).

Bir FeFET'in kutuplanması, fiziksel bir Kollaptondur. Bkz. [`../donanim/kollaptik-altkatman.md`](../donanim/kollaptik-altkatman.md).

## Cebir

Kollaptonlar olasılıksal bir grafik model gibi birleşir: iki Kollaptonu eşleştirmek, potansiyellerini **toplar** ve alanlarını **çarpar**. Bir Collaptics programı, bir komut dizisi değil; bir eşleşme grafiği artı bir rezonans takvimidir.

---

İlgili: [`bilgisel-cokus.md`](bilgisel-cokus.md) · [`bilgisel-cekim.md`](bilgisel-cekim.md) · [`cokus-tekilligi.md`](cokus-tekilligi.md)
