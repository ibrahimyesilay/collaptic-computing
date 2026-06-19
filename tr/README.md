# Collaptic Computing (Collaptics)

> **Collaptics bir uygulama değildir. Bilginin ikili (binary) kalmak zorunda olup olmadığını sorma girişimidir.**

*Olasılık Alanları, Fotonik Rezonans ve Bilgisel Çöküş üzerine kurulu, ikili-sonrası (post-binary) bir hesaplama paradigması.*

[![DOI](https://zenodo.org/badge/1272820222.svg)](https://doi.org/10.5281/zenodo.20739592)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](../LICENSE)

> 🇬🇧 İngilizce sürüm için ana dizine bakın: [`../README.md`](../README.md)

---

## Özet

Collaptic Computing, hesaplamanın olası ikili-sonrası bir yönünü araştıran kuramsal bir araştırma çerçevesidir.

Bilgiyi bit olarak temsil etmek yerine Collaptics, bilgiyi dinamik **olasılık alanları** olarak temsil eder. Mantığı transistörler ve mantık kapılarıyla yürütmek yerine Collaptics, hesaplamayı **rezonans, çekim havzası oluşumu ve bilgisel çöküş** üzerinden önerir.

**Collaptics yeni bir fizik iddiası değildir.** Her adım; stokastik dinamik, bilgi geometrisi ve katıhâl fiziğindeki yerleşik sonuçlara dayanır. Collaptics, transistör-sonrası hesaplama mimarileri üzerine tartışma başlatmak için tasarlanmış kavramsal bir çerçevedir — ve basit bir fikrin kırılmadan ne kadar ileri götürülebileceğini sınamak içindir.

Çerçeve tek bir kurucu yasayla yönetilir:

```
Σ = I · Ω²            ( Ω = ρ · ω )
```

> *Bir çöküşün çözme gücü (Σ), alanın gizil bilgisi (I) ile altkatmanın tutarlı rezonansının karesinin (Ω²) çarpımına eşittir — fotonun frekansı ω, faz tutarlılığı ρ ile ölçeklenir.*

---

## Temel Kavramlar

**Kollapton** — temel bilgi birimi. Bir Kollapton, ikili bir değer yerine bir *olasılık dağılımı* saklar.

**Bilgisel Çekim** — bilgi, olasılık uzayında çarpıklıklar yaratır; problemler, çözümlerin üzerinde yuvarlandığı manzarayı bizzat büker.

**Çekim Havzaları** — olasılığın doğal olarak aktığı potansiyel çözüm bölgeleri.

**Çöküş Tekilliği** — bir bilgisel topolojideki en derin çekici: cevabın kendisi.

**Çöküş Olay Ufku** — bir çöküşün geri döndürülemez hâle geldiği sınır. Hiyerarşiyi tamamlar:

```
Bilgi Alanı → Çekim Havzası → Çöküş Olay Ufku → Çöküş Tekilliği
```

**Bilgisel Çöküş** — dağıtık bir olasılık alanının tek bir kararlı çözüme yakınsaması. *Makine hesaplamaz; oturur (yerine yerleşir).*

→ Tam çerçeve tek dokümanda: [`Collaptics Beyaz Bülten (TR)`](../whitepaper/Collaptic_Computing_Whitepaper_TR_v1.0.md). Ayrıntılı işleyiş: [`temeller/`](temeller/). Türetmeler: [`matematik/`](matematik/). Donanım: [`donanim/`](donanim/). Örnekler: [`ornekler/`](ornekler/).

---

## Depo Yapısı

```
tr/
├── beyaz-bulten/    çerçevenin tamamı, tek doküman
├── temeller/        temel kavramlar, her biri tek sayfa
├── matematik/       Çöküş Yasası'nın türetilmesi; bilgi geometrisi
├── donanim/         malzeme ve elektronik; ileriye dönük altkatmanlar
├── ornekler/        işlenmiş örnekler — dürüst bir olumsuz sonuç dâhil
└── (simülasyon)     → ortak kod ana dizinde: ../simulation/
```

---

## Durum

| | |
|---|---|
| **Sürüm** | 1.0 |
| **Hâl** | Kuramsal çerçeve — sayısal olarak doğrulandı |
| **Tür** | Çalışma belgesi (working paper) |
| **Sayısal doğrulama** | Tamamlandı — 6/6 temel öngörü yeniden üretildi ([`../simulation`](../simulation/)) |
| **Fiziksel prototip** | Henüz yok |
| **Fiziksel temel** | Yerleşik fizik; yeni fizik yasası iddia edilmez |

Simülasyon, Collaptics'nin donanım olarak çalıştığını **kanıtlamaz**. Yalnızca çerçevenin denklemlerinin iç tutarlı olduğunu ve stokastik dinamiğin bilinen sonuçlarını yeniden ürettiğini gösterir — fazlası değil. Fiziksel iddialar sınanmamıştır.


---

## Sayısal Kontroller

Çöküş Yasası'nın altı öngörüsü saf Python ile (yalnızca numpy) yeniden üretiliyor:

| | Öngörü | Sonuç |
|---|---|---|
| P1 | çözme gücü `σ² ∝ Ω⁻²` ile keskinleşir | eğim **−1.989** (hedef −2) |
| P2 | tutarlılık, sıcaklıkla değiştirilebilir (`Ω²/D`) | **%0.20** sapma |
| P3 | Cramér–Rao doğruluk tavanı `Var ≥ 1/(I·Ω²)` | Σ **9.033** / 9.000 |
| P5a | havzalar derinlik × genişlikle çeker — *genişlik derinliği yenebilir* | **0.394** / 0.384 |
| P5b | yüksek bariyerler alanı tuzaklar (dürüst sınır) | doğrulandı |
| P6 | çözüme-varış süresi `τ ∝ exp(βΔV)` (Arrhenius) | eğim **0.991** |

```bash
cd ../simulation
python3 collapse_sim.py        # rapor
python3 test_predictions.py    # testler; hata olursa sıfırdan farklı çıkış kodu
```

P5b ve P6 en önemlileridir: Collaptics'nin **nerede durduğunu** işaretlerler. Collaptics, düz ve geçilebilir manzaralar için bir enerji/verim fikridir — zor problemleri bedavaya çözen bir sihir **değildir**. Collaptics'nin hiçbir avantaj sağlamadığı işlenmiş bir örnek için bkz. [`ornekler/hash-tersine-cevirme.md`](ornekler/hash-tersine-cevirme.md).

---

## Neden Collaptics?

Modern hesaplama temel ölçeklenme sınırlarına yaklaşıyor. Collaptics, gelecekteki hesaplama sistemlerinin olasılığı ikili mantıkla *taklit etmek* yerine *doğrudan* olasılık alanları üzerinde çalışıp çalışamayacağını araştırır — ve mevcut birçok olasılıksal hesaplama platformunun (Ising makineleri, memristör dizileri, tutarlı optik işlemciler) ayrı aygıtlar yerine tek bir temel yasanın örnekleri olarak anlaşılıp anlaşılamayacağını sorar.

---

## Yazar

Ibrahim Yesilay · 2026

## Lisans

[Creative Commons Atıf-GayriTicari 4.0 Uluslararası (CC BY-NC 4.0)](../LICENSE) — atıf vererek **ticari olmayan** amaçlarla serbestçe kullanın, paylaşın ve uyarlayın. Ticari kullanım bu lisans kapsamında verilmez; tüm ticari haklar yazara aittir. Ticari lisans için yazarla iletişime geçin.
