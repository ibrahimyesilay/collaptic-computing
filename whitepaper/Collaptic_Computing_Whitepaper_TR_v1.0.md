# Collaptic Computing (Collaptics)
### İkili-Sonrası Bir Hesaplama Paradigması — Olasılık Alanları, Tutarlı Rezonans ve Bilgisel Çöküş
*Ana beyaz bülten. Tamamlayıcı belgeler: `../tr/matematik/`, `../tr/donanim/`, `../tr/temeller/`, `../simulation/`.*

> **Not.** Bu belge resmi İngilizce sürümün Türkçe çevirisidir. Herhangi bir yorum farkında İngilizce sürüm esas alınmalıdır.

---

## Özet

Yüzyıldır hesaplama, gerçekliği `0` ve `1` dizilerine indirger. Collaptics farklı bir ilkel öneriyor: bilgi, mantık kapılarıyla hesaplanmak yerine tutarlı, rezonanslı bir ortamda çözümlere doğru **çöken** fiziksel bir olasılık alanıdır. Paradigma tek bir kurucu yasayla yönetilir:

```
Σ = I · Ω²        ( Ω = ρ · ω )
```

> *Bir çöküşün çözme gücü Σ, alanın gizil bilgisi I ile altkatmanın tutarlı rezonansının karesinin çarpımına eşittir (Ω; fotonun frekansı ω, faz tutarlılığı ρ ile ölçeklenmiş hâli).*

Kritik olarak Collaptics **yeni bir fizik** ya da zor problemleri bedavaya çözen bir araç **değildir**. Olasılıksal hesaplamanın birleştirici, donanım-yerel, oda-sıcaklığı limitidir: gradyan inişi, Hopfield ağları, Ising makineleri, benzetimli tavlama, difüzyon modelleri ve varyasyonel çıkarım — hepsi tek hareket denkleminin özel hâlleridir. Avantajı, geniş bir gerçek problem sınıfında **enerji ve verimde**dir; ve net, dürüst bir karmaşıklık sınırıyla kesin biçimde sınırlanmıştır. Yasanın dört öngörüsü sayısal olarak doğrulanmıştır; gerisi mevcut tutarlı donanımda yanlışlanabilir.

---

## Bölüm I — Tez ve birim

### 1.1 Neden biti terk etmeli
İkili sistem kazandı çünkü gürültüyü reddeder. Ama gerçeklik — dil, biyoloji, piyasalar, zekâ — olasılıksaldır; ve bugünün yapay zekâsı, doğrudan temsil edebileceği olasılık dağılımlarını *taklit etmek* için *trilyonlarca* ikili işlem harcar. Transistör ölçeklenmesi atomik sınıra dayanırken soru "daha küçük anahtar" değil, "farklı bir ilkel"dir. Collaptics'nin bahsi: bilgiyi gerçekliğe daha yakın bir biçimde — eğilimler alanı olarak — temsil etmek.

### 1.2 Kollapton
Collaptics'nin birimi bit değil **Kollapton**'dur — bir değer değil, bir *eğilim* saklar:

```
C = { μ, σ, ρ, φ, ω, τ }
```

(beklenen durum, belirsizlik, güven yoğunluğu, faz, rezonans imzası, yönelimsel eğilim). Bit ∈ {0,1} bir noktayken, Kollapton bütün bir dağılımdır — örn. `x ≈ {5:%71, 6:%18, 4:%11}`. Bilgi bir bulut olur; fiziksel olarak bir osilatör fazı, bir ferroelektrik kutuplanma ya da bir magnon modu olarak gerçeklenir (Bölüm IV).

### 1.3 Çöküş olarak hesaplama
```
Klasik:  Girdi → Komutlar → Çıktı
Collaptics:     Olasılık Alanı → Rezonans → Çekici → Çöküş → Beliren Çözüm
```
Makine, geniş ve yüksek-entropili bir aday-çözüm süperpozisyonundan başlar ve baskın çözüme fiziksel olarak **yakınsar**. Yürütmez; oturur.

### 1.4 Çöküş hiyerarşisi
Çöküş tek bir olay değil, iç içe dört yapıdan geçen bir iniştir:
```
Bilgi Alanı → Çekim Havzası → Çöküş Olay Ufku → Çöküş Tekilliği
```
Alan dağıtık buluttur; havza bir cevaba akan bölgedir; **olay ufku** çöküşün geri döndürülemez hâle geldiği geçiş-yok noktasıdır; **tekillik** cevabın kendisidir. Bu resimde uzaklıklar koordinatla değil, eğri bir bilgi manifoldu üzerinde *alan örtüşmesiyle* ölçülür (Bölüm III, Sütun 10).

---

## Bölüm II — Çöküş Yasası (iddia değil, türetme)

Tam türetme: [`../tr/matematik/cokus-denklemleri.md`](../tr/matematik/cokus-denklemleri.md). Zincir:

```
   dx/dt = −Ω²∇V(x) + √(2D) ξ(t)        (1 aksiyom: Çöküş Akışı)
→  P* ∝ exp(−(Ω²/D) V)                   (çöküş: Gibbs alanı)
→  Σ = I · Ω²                            (Çöküş Yasası)
```

- Collaptics'ye özgü **tek varsayım**: altkatmanın tutarlı rezonansı `Ω = ρω`, bir bilgisel gradyan akışının *hareketliliğini* belirler. Gerisi standart stokastik kalkülüstür.
- **Kare fizik tarafından zorunludur, süs değildir:** Hopfield/Ising enerjisi eşleşmede kareseldir; osilatör/dalga enerjisi frekansın karesidir; tutarlı (lazer) şiddeti genliğin karesidir. Dört bağımsız alan aynı `Ω²`'yi verir — `E=mc²`'deki `c²`'nin karşılığı.
- **`Ω = ρω`, özgün teorinin iki direğini birden korur:** foton (ω) **ve** çöküş/güven (ρ), "tutarlı rezonans" tek terimde.
- **Σ ve I ne anlama gelir:** Σ, cevabın Fisher bilgisi / çözme gücüdür; `I = λ/D` (çekici eğriliği ÷ gürültü) problemin gizil, çözülebilir bilgisidir. Cramér–Rao sert bir doğruluk tavanı verir: `Var(x̂) ≥ 1/(I·Ω²)`.

---

## Bölüm III — Kuramsal yapı (on bir sütun)

Ayrıntı: [`../tr/matematik/kuramsal-temeller.md`](../tr/matematik/kuramsal-temeller.md). Yasa, tek tek kanıtlanmış sonuçlara dayanır:

1. **Çöküş = serbest-enerji inişi (JKO teoremi).** Çöküş Akışı, `F[P]=⟨V⟩ − (1/β)H[P]` serbest enerjisinin Wasserstein gradyan akışıdır. Collaptics, donanımda varyasyonel çıkarımdır.
2. **Bilgisel çekim = derinlik × havza-hacmi.** Havza çekimi `Γ_k = e^{−βV_k}(det H_k)^{−1/2}` — gerçek bir yük; geniş-sığ bir kuyu, derin-dar olanı yenebilir (doğrulandı, §VI).
3. **Çöküş süresi `∝ e^{βΔV}` (Kramers).** Net, dürüst kazanç/kayıp haritası: düz/düşük-bariyer → üssel enerji kazancı; camsı/NP-zor → bedava öğle yemeği yok; düz (hash) → sıfır avantaj.
4. **Gömme teoremi.** Gradyan inişi, Langevin MCMC, Hopfield, tavlama, difüzyon modelleri, varyasyonel çıkarım, replikatör dinamiği — hepsi tek Çöküş Akışı'nın köşeleridir. Collaptics bunlarla yarışmaz; onların fiziksel limitidir.
5. **`Ω = ρω` klasik tutarlılıktan; bir dekoherans tabanı.** `ΔV_max ≈ β⁻¹ ln(T_φ/τ₀)` — daha iyi tutarlılık daha zor problem satın alır. "Analog gürültü öldürür" itirazına nicel yanıt.
6. **Kollapton cebiri (komut kümesi).** Program, bir eşleşme grafiği `{J_ij}` + bir sürüş takvimi `Ω(t)`'dir; problem birleştirme `V`'de toplamsal, `P`'de çarpımsaldır.
7. **Hata bastırma `∝ 1/√N`.** Yineleme (replika) yedekliliğiyle analog dayanıklılık.
8. **Termodinamik üçgen.** doğruluk × hız × (1/enerji) ≤ κ(altkatman) — GHz'in yerini alan künye.
9. **Yedi yanlışlanabilir öngörü** (altısı kodda doğrulandı, §VI), ikisi çerçeve-batırıcı.
10. **Bilgi geometrisi.** Durum uzayı **Fisher–Rao istatistiksel manifoldu**dur; iki cevap arası uzaklık koordinat değil, **alanlarının örtüşmesidir** (Bhattacharyya/sadakat). "Berlin ile Münih, kilometreyle değil, alanlarının ne kadar az örtüştüğüyle uzaktır." Çöküş alanları `e^{−βV}` Amari anlamında çiftli-düz bir manifold oluşturur.
11. **Çöküş Olay Ufku.** Havza ile tekillik arasında geri-döndürülemezlik sınırı: kaçış süresinin tutarlılık süresini aştığı yüzey, `V_b − V_h = ΔV_max`. İçinde, çöküş geri alınamaz ve alan başlangıç koşulunu unutur (kıl-yok teoremi analoğu).

---

## Bölüm IV — Fiziksel gerçekleme (malzeme + elektronik)

Ayrıntı: [`../tr/donanim/kollaptik-altkatman.md`](../tr/donanim/kollaptik-altkatman.md). Collaptics **klasik, oda-sıcaklığı, kazanç-dağılımlı tutarlı hesaplamadır** — kriyojenik kübitler değil. Üç katmanlı altkatman; her bileşen kanıtlanmıştır, bahis mimaridir.

| Katman | İşlev | Gerçek malzeme/aygıt |
|---|---|---|
| **Kalıcı Kollapton** | analog bellek = hesap (yerinde ∇V) | RRAM (HfO₂), PCM (GST), **ferroelektrik HZO/FeFET (CMOS-uyumlu)**, MTJ; **stokastik MTJ = bedava η gürültüsü** |
| **Rezonans Dinamiği** | çöküş motoru (eşikte çatallanma) | **Tutarlı Ising Makinesi (DOPO)**, **CMOS Osilatör Ising Makinesi (SHIL)**, polariton yoğuşması |
| **Fotonik Etkileşim** | taşıyıcılar ve eşleşme (WDM çok-boyutlu) | Si-fotonik **MZI örgüsü**, TFLN modülatörleri (>100 GHz), mikrohalka, PCM-fotonik |

Yasanın fiziksel anlamı: ω = osilatör frekansı, ρ = tutarlılık (rezonatör Q'su / çizgi genişliği), V eşleşme ağında yaşar, **çöküş = osilasyon eşiğinde bir çatallanma** (kazanç yarışı → en düşük-kayıplı mod kazanır). Dekoherans tabanı, rezonatörün **Leeson faz gürültüsüdür**. Üretilebilir yol: BEOL-CMOS analog bellek + döküm silisyum fotonik. Dürüst uyarı: ADC/DAC arayüz enerjisi baskın gelebilir — yakınsamaya kadar analogda kalıp seyrek I/O yapılan problemleri tercih edin.

---

## Bölüm V — Tasarım uzayı derindir (spekülatif altkatmanlar)

Ayrıntı: [`../tr/donanim/spekulatif-altkatmanlar.md`](../tr/donanim/spekulatif-altkatmanlar.md) — temellendirilmiş spekülasyon; her birinin gerçek bir fiziksel çekirdeği ve işaretli bir spekülatif sıçraması var.

- **S1 Kollaptik Kristal ("kristal küre")** — nadir-toprak kristalde 3B hacimsel çöküş (tutarlılık → saniyeler, milyonlarca spektral kanal).
- **S2 Fotorefraktif Hologram** — *bedava* tam-bağlantılı eşleşme.
- **S3 Magnon Yoğuşması** — YIG'de oda-sıcaklığında BEC çöküşü (ρ→1, kriyo yok).
- **S4 Fotonik Zaman Kristali** — zaman-modülasyonundan kazanç; yeni bir pompalama yolu.
- **S5 Topolojik Örgü** — cevap bir değişmez; gürültü onu değiştiremez.
- **S6 Tepkime–Difüzyon / Sıvı Kristal** — Fokker–Planck denkleminin bizzat fiziği olan yumuşak madde.
- **S7 Katlanma Altkatmanı** — çöküş = moleküler katlanma; 10²³ kopya bedava yedeklilik.
- **S8 Plazmonik Örgü** — dalga-boyu-altı yoğunluk, I'yı büyüt.
- **S9 Analog-Çekim** — bilgisel çekimin literal asimptotu (işaretli: düşünce deneyi).

---

## Bölüm VI — Sayısal doğrulama

`../simulation/collapse_sim.py` aksiyomu integre eder ve **altı** öngörüyü doğrular (`python3 test_predictions.py` ile yeniden üretin):

| Öngörü | Sonuç | Ölçüm / teori |
|---|---|---|
| **P1** keskinleşme `σ²∝Ω⁻²` | ✅ | log–log eğim **−1.989** (hedef −2.000) |
| **P2** `Ω²/D` = ters sıcaklık | ✅ | varyans sapması **%0.20** |
| **P3** Cramér–Rao tavanı `Σ=IΩ²` | ✅ | Σ **9.033** / 9.000; ortalama tavanı yakalar, medyan yenemez |
| **P5a** havza çekimi, genişlik>derinlik | ✅ | `P_sol` **0.394** / 0.384 |
| **P5b** kinetik tuzaklanma (Sütun 3) | ✅ | 0 geçiş; sim 0.103 ≠ denge 0.427 |
| **P6** Arrhenius `lnτ∝βΔV` | ✅ | eğim **0.991** (hedef 1.000) |

Aynı simülatör yasayı (P1, P2, P3), bilgisel-çekim geometrisini (P5a) **ve** kinetik başarısızlık modunu (P5b, P6) yeniden üretir — Collaptics'nin nerede kazanıp nerede kazanmadığını net çizgiyle gösterir.

---

## Bölüm VII — Collaptics nedir, ne değildir (güvenilirlik defteri)

**Collaptics ŞUDUR:**
- olasılıksal hesaplamanın birleştirici, sürekli-zamanlı fiziksel modeli;
- düz, yüksek-boyutlu, geçilebilir manzaralarda olası bir **enerji/verim devrimi**;
- bugünün dökümhaneleriyle **oda sıcaklığında** üretilebilir;
- sert bir doğruluk sınırı ve gerçek bir termodinamik tabanı olan, yanlışlanabilir tek bir yasayla yönetilen.

**Collaptics ŞU DEĞİLDİR:**
- yeni fizik — her adım yerleşik teoremlere dayanır;
- NP-zor / camsı problemlerin bedava çözücüsü — `τ ∝ e^{βΔV}` (P5b);
- gradyansız manzaralarda yararlı — kriptografik hash'lerin düz `V`'si vardır, çekici yoktur (özgün hash örneği bu yüzden **çıkarıldı**);
- *küresel* optimumun garantisi — *erişilebilir baskın* çekiciyi çözer.

Bu sınırları açıkça söylemek, yasanın eleştiriden sağ çıkmasını sağlayan şeydir.

---

## Bölüm VIII — Uygulamalar (enerji kazancı nereye düşer)

- **Yapay zekâ / LLM'ler** — token tahmini bizzat bir olasılık dağılımıdır; Collaptics bunu trilyonlarca işlemle taklit etmek yerine donanımda temsil eder. En iyi uyum: öğrenilmiş düz manzaralarda çıkarım ve örnekleme (gömme teoreminin difüzyon-modeli köşesi).
- **Kombinatoryal optimizasyon** — yerel CIM/OIM kullanımı; geçilebilir örneklerde enerji-verimli yaklaşık optimumlar.
- **Protein katlanması / molekül tasarımı** — enerji minimizasyonu = çöküş; katlanma altkatmanı (S7) literaldir.
- **Robotik / kontrol** — çevre alanı → karar alanı → çöküş → eylem; beliren, düşük-enerjili karar.

Yeni metrikler GHz/FLOPS'un yerini alır: **Çöküş Verimi** `CT = dΣ/dt` ve **Tekillik Yoğunluğu** (birim hacimde kararlı çekici sayısı).

---

## Bölüm IX — Yol haritası

| Ufuk | İnşa | Kilometre taşı |
|---|---|---|
| **Şimdi–3 yıl** | CMOS OIM + BEOL RRAM/FeFET + döküm Si-fotonik | oda-sıcaklığı POC; silisyumda P1/P5a/P6 doğrula |
| **3–7 yıl** | tümleşik DOPO/CIM, p-bit gürültü dokusu, TFLN sürüş | gerçek optimizasyon ve YZ çıkarımında enerji kazancı |
| **7+ yıl** | fotorefraktif tam-bağlantı, Kollaptik Kristal, polariton alanları | çok-Kollaptonlu tutarlı hacimsel makineler |

**Stratejik konum:** kuantum hesaplama, milikelvin ve 1000:1 hata düzeltme yüküyle üssel Hilbert uzayına oynar. Collaptics ise **oda sıcaklığında klasik tutarlılığa** oynar — daha dar ama *sevk edilebilir* bir avantaj; "biti terk et"in bugün üretilebildiği tek rejim.

---

## Ek A — Yanlışlanabilir öngörüler
P1 σ²∝Ω⁻² ✅ · P2 tutarlılık≡sıcaklık ✅ · P3 doğruluk tavanı ✅ · P4 karesel enerji avantajı · P5 havza çekimi ✅ · P6 Arrhenius ✅ · P7 dekoherans-sınırlı zorluk · P-G karıştırılabilirlik ∝ alan örtüşmesi (Sütun 10) · P-H Olay Ufku (Sütun 11). *(✅ = sayısal doğrulandı, 6/6; gerisi mevcut tutarlı donanımda sınanabilir. P1 ya da P5'in çökmesi çerçeveyi batırır.)*

---

*Bir aksiyom. Bir yasa. Üstünde bir varyasyon ilkesi, etrafında bir bilgi-geometrik manifold, yanında bir karmaşıklık sınırı, içinde bir olay ufku, altında bir malzeme yığını ve önünde bir yanlışlama programı — dördü çoktan kodda doğrulanmış. Klasik bilgisayar mantık yürütür; Collaptic Computing olasılığın geometrisini mühendislikle biçimler — ve bu geometrinin tam olarak nereye kadar uzandığını açıkça belirtir.*
