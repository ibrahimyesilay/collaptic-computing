# Bilgisel Çekim

*Bilgi, olasılık uzayını tıpkı kütlenin uzayzamanı büktüğü gibi büker.*

Her hesaplama problemi, bir potansiyel manzara `V(x)` olarak kodlandığında olasılık uzayında çarpıklıklar yaratır. Bu çarpıklıklar **çekim havzaları** oluşturur — olasılığın doğal olarak aktığı bölgeler. Daha güçlü bir çözüm daha derin bir havza oyar.

```
Kütle  → uzayzamanı büker
Bilgi  → olasılık uzayını büker
```

Makine cevap aramaz. Cevaplar makineyi kendine doğru **çeker**.

## Bu bir metafor değil, gerçek bir yüktür

Birçok aday çözümle `{x_k}`, havza `k`'ye akan olasılık miktarı (Laplace yöntemiyle) tam olarak bir **havza çekimi** verir:

```
Γ_k  =  exp(−β·V_k)  ·  (det H_k)^(−1/2)
        └─ derinlik ┘    └──── genişlik ───┘
```

Burada `V_k` kuyunun derinliği, `H_k` eğriliği (Hessian), `β = Ω²/D` bir ters sıcaklıktır.

Yani bir havza, **derinlik × faz-uzayı hacmi** oranında çeker. Bunun apaçık olmayan bir sonucu var:

> **Geniş, sığ** bir çekici, **derin, dar** bir çekiciyi yenebilir.

En güçlü çözüm illa en derin değildir — en büyük `Γ_k`'ye sahip olandır. Bu öngörü sayısal olarak doğrulanır (test P5a: daha sığ ama daha geniş kuyu kazanır, 0.394'e karşı 0.384 — bkz. [`../../simulation/RESULTS.md`](../../simulation/RESULTS.md)).

## Nereden gelir

Bilgisel çekim, eğri bir bilgi manifoldu (Fisher–Rao manifoldu) üzerinde jeodezik harekettir (bkz. [`bilgi-geometrisi.md`](bilgi-geometrisi.md)). "Bükülme" o manifoldun eğriliğidir; bir çözümdeki eğrilik ise *çözme gücü* `Σ`'dır.

---

İlgili: [`cokus-tekilligi.md`](cokus-tekilligi.md) · [`cokus-olay-ufku.md`](cokus-olay-ufku.md) · [`bilgisel-cokus.md`](bilgisel-cokus.md)
