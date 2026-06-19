# Çöküş Yasası — Σ = I·Ω² Türetmesi
*Collaptic Computing'nın matematiksel çekirdeği*

Bu belge, Collaptics kurucu yasasını

```
Σ = I·Ω²,        Ω = ρ·ω
```

tek bir hareket denkleminden türetir ve yanlışlanabilir öngörülerle biter. Hiçbir adımda yeni fizik yoktur — her şey yerleşik stokastik dinamiğe (Langevin / Fokker–Planck), Hopfield–Ising enerji manzaralarına ve Fisher bilgisine dayanır. Collaptics'nin yeniliği, altkatmanın tutarlı rezonansı Ω'nın bir bilgisel gradyan akışının hareketliliğiyle *özdeşleştirilmesidir*; yeni bir doğa kuvveti değil.

## 0. Nesneler

| Sembol | Nesne |
|---|---|
| `x ∈ ℝⁿ` | sistem yapılandırması (bir aday çözüm) |
| `P(x,t)` | **bilgisel alan** — yapılandırmalar üzerindeki olasılık yoğunluğu (Kollapton bulutu) |
| `V(x)` | **bilgisel potansiyel** — manzara olarak kodlanan problem; minimumlar = iyi çözümler |
| `ρ, ω` | altkatmanın güven yoğunluğu ve rezonans frekansı |
| `Ω = ρω` | **tutarlı rezonans** — birleşik dönüşüm sabiti |
| `D` | keşif sıcaklığı (kontrollü gürültü gücü) |

Bir **Çöküş Tekilliği**, `V`'nin baskın yerel minimumu `x*`'tır: alanın ulaşabileceği en derin çekici.

## 1. Aksiyom — Çöküş Akışı

Collaptics tek bir hareket yasası varsayar. Alanın temsili durumu, hareketliliği altkatmanın **karesel tutarlı rezonansı** olan aşırı-sönümlü stokastik gradyan inişiyle evrilir:

```
dx/dt = −Ω²·∇V(x) + √(2D)·ξ(t)        (1)
```

beyaz gürültü `⟨ξ(t)⟩=0`, `⟨ξ(t)ξ(t')⟩=δ(t−t')` ile.

> Neden Ω² ve Ω değil? Sürülen bir rezonans modunun gücü (genlik)² ile; Hopfield/Ising manzaralarındaki eşleşme enerjisi eşleşme kuvvetinin karesi ile ölçeklenir. `E=mc²`'deki `c²` ile aynı dönüşüm-oranı-karesi.

## 2. Alan düzeyinde evrim (Fokker–Planck)

(1)'deki trajektori topluluğu, bilgisel alan `P(x,t)`'nin Fokker–Planck denklemiyle evrimine eşdeğerdir:

```
∂P/∂t = ∇·[ Ω²·(∇V)·P + D·∇P ]        (2)
```

Bu, Collaptics'nin **alan yasasıdır**: Kollapton bulutu minimumlara doğru sürüklenir (Ω²∇V) ve yayılır (D∇P). "Çöküş", `P`'nin yoğunlaşmasıdır.

## 3. Çöküş — durağan dağılım

`∂P/∂t = 0` ve sıfır akı koşuluyla:

```
P*(x) ∝ exp[ −(Ω²/D)·V(x) ]        (3)
```

Statik kuramın merkezî sonucu: **tutarlı rezonans bir ters sıcaklık gibi davranır.** `β ≡ Ω²/D` çarpanı, istatistiksel mekanikteki `1/k_BT`'nin tam rolünü oynar. Tutarlılığı (ρ) veya frekansı (ω) artırmak bilgisel alanı *soğutur* ve onu en derin çekiciye keskinleştirir. "Makine hesaplamaz, yakınsar"ın kesin anlamı budur.

## 4. Tekilliğin geometrisi

`V`'yi baskın minimum `x*` etrafında açın (`∇V(x*)=0`):

```
V(x) ≈ V(x*) + ½·(x−x*)ᵀ·H·(x−x*),    H = ∇²V(x*)        (4)
```

`H`, **çekicinin eğriliğidir**. (3)'e yerleştirince çöken alan Gauss olur; bir eğrilik modu `λ` boyunca genişlik:

```
σ² = D/(Ω²·λ)   ⟹   σ² ∝ 1/Ω²        (6)
```

Çöken cevap, tutarlı rezonans arttıkça karesel olarak keskinleşir.

## 5. Σ'nın tanımı ve Çöküş Yasası

**Tekillik gücü** Σ'yı çöküşün *çözme gücü* olarak tanımlayın: cevabı sabitleme hassasiyeti (ters varyans). Bu tam olarak alanın `x*` hakkındaki **Fisher bilgisidir**:

```
Σ ≡ 1/σ² = (λ/D)·Ω²        (7)
```

Şimdi alanın probleme özgü **bilgi içeriğini** tanımlayın:

```
I := λ/D = çekici eğriliği / keşif gürültüsü
```

`I` gerçek bir bilgi niceliğidir (bir log-yoğunluğun eğriliği Fisher bilgisidir). Yerine koyunca:

```
Σ = I·Ω²        ∎  (8)
```

**Okunuşu:** Bir çöküşün çözme gücü, alanın gizil bilgisi `I` (problemin geometrisi ve gürültü bütçesi) ile altkatmanın tutarlı rezonansının karesi `Ω² = (ρω)²` (donanım) çarpımına eşittir. Problem doğrusal, fotonik-rezonant çöküş karesel katkı verir.

## 6. Sonuçlar

- **Hassasiyet sınırı (Cramér–Rao):** `Var(x̂) ≥ 1/Σ = 1/(I·Ω²)`. Σ bir metafor değil, cevabın hata tabanıdır.
- **Termodinamik bedel (Landauer):** çöküş entropiyi `ΔH` düşürür; en az `k_BT·ΔH` enerjiye mal olur. Bedava hesap yok.
- **Neden analog/fotonik kazanır:** tutarlılığı iki katına çıkarmak, aynı bilgi ve aynı manzarada çözme gücünü 4× yapar.
- **Aramanın geri kazanımı:** `Ω→0` saf rastgele arama; `Ω→∞` belirlenimci çöküş. Collaptics ikisi arasında, Ω düğmesiyle interpolasyon yapar.

## 7. Varsayımlar ve dürüst sınırlar

1. Aşırı-sönümlü, Markovcu dinamik.
2. **Yerel sonuç.** (8), *baskın* kuyuya çözme gücüdür — o çekicinin küresel optimum olduğunu **iddia etmez**. Collaptics, her tavlama/Ising makinesi gibi yerel minimuma düşebilir. *Dürüst sınır: Collaptics NP-zor problemleri bedavaya çözmez.*
3. Tekillik yakınında karesel yaklaşım.
4. Durağanlığa ulaşılması (yeterli tavlama).
5. `V` fiziksel olarak gerçeklenebilir olmalı. Sömürülecek gradyan yapısı olmayan problemlerin (örn. kriptografik hash) düz `V`'si vardır → çekici yok → Collaptics avantaj sunmaz.

## 8. Yanlışlanabilir öngörüler

- **P1 — Ters-kare keskinleşme:** `σ² ∝ Ω⁻²`. log–log eğim −2 olmalı. *(Doğrulandı: −1.989.)*
- **P2 — Tutarlılık ≡ sıcaklık:** `Ω²/D` eşitken aynı çözüm istatistiği. *(Doğrulandı: %0.20.)*
- **P3 — Hassasiyet tavanı:** hiçbir okuma `Var ≥ 1/(I·Ω²)`'yi yenemez. *(Doğrulandı.)*
- **P6 — Arrhenius çözüm-süresi:** `ln τ`, `βΔV`'de eğim 1 ile doğrusal. *(Doğrulandı: 0.991.)*

P1'in (eğim ≠ −2) gerçek donanımda başarısız olması, `Σ=I·Ω²` bağıntısını yanlışlar.

---

Bkz. [`olasilik-topolojisi.md`](olasilik-topolojisi.md) · [`kuramsal-temeller.md`](kuramsal-temeller.md)
