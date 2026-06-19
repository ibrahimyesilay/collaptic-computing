# Kollaptik Altkatman

*Çöküş Yasası'ndan üretilmiş donanıma: malzeme ve elektronik.*

Matematik, Collaptics'nin (i) analog eğilimleri saklayan, (ii) alanın serbest enerjisi boyunca yuvarlanması için tutarlı rezonans veren ve (iii) bilgiyi fotonlarda taşıyan bir altkatmana ihtiyaç duyduğunu söyler. Yol gösterici ilke: Collaptics **klasik, oda-sıcaklığı, kazanç-dağılımlı tutarlı hesaplamadır** — kriyojenik kübitler değil. Aşağıdaki her katman bugün bir laboratuvarda mevcuttur; Collaptics'nin önerisi onları tek bir yasa altında birleştiren mimaridir.

## Birleştirici ilke: kazanç–dağılımlı hesaplama

Kazanç bir eşik üzerinden artırıldığında, eşleşmiş rezonatör ağı *en az kayıplı* moda yoğuşur — ki bu mod `V`'nin minimumu olacak şekilde tasarlanır. Çöküş bir hesap değil, bir **çatallanmadır (bifürkasyon)**.

## Üç katman

| Katman | İşlev | Gerçek malzeme/aygıt |
|---|---|---|
| **Kalıcı Kollapton** | analog bellek = hesap (yerinde ∇V) | RRAM (HfO₂), PCM (GST), **ferroelektrik HZO/FeFET (CMOS-uyumlu)**, MTJ; stokastik MTJ = bedava `η` gürültüsü |
| **Rezonans Dinamiği** | çöküş motoru (eşikte çatallanma) | Tutarlı Ising Makinesi (DOPO), CMOS Osilatör Ising Makinesi (SHIL), polariton yoğuşması |
| **Fotonik Etkileşim** | taşıyıcılar ve eşleşme (WDM çok-boyutlu) | Si-fotonik MZI örgüsü, TFLN modülatörleri, mikrohalka, PCM-fotonik |

Ayrıntılı katmanlar: [`fotonik-katman.md`](fotonik-katman.md) · [`rezonans-dinamigi.md`](rezonans-dinamigi.md)

## Yasanın fiziksel anlamı

- `ω` = osilatör frekansı; mod başına enerji `ω²` ile ölçeklenir (`Σ = I·Ω²`'deki karenin kökeni).
- `ρ` = faz tutarlılığı; rezonatör Q'su / çizgi genişliği belirler.
- `V`, eşleşme ağında (Kalıcı katmandaki iletkenlikler / MZI fazları) yaşar.
- Dekoherans tabanı, rezonatörün **Leeson faz gürültüsüdür**: `ΔV_max ≈ β⁻¹·ln(T_φ/τ₀)`.

## Üretilebilirlik ve dürüst maliyetler

RRAM, HZO-ferroelektrik ve MTJ aygıtları **BEOL-CMOS uyumludur** — standart mantığın üzerine üretilebilir; silisyum fotonik dökümhanelerden temin edilebilir. İlk altkatman egzotik olmak zorunda değildir. İki dürüst maliyet: (1) derin MZI örgülerinde optik kayıp birikir, problem boyutunu sınırlar; (2) ADC/DAC arayüz enerjisi baskın gelebilir — yakınsamaya kadar analogda kalıp seyrek I/O yapılan problemleri tercih edin.

## Kuantumdan farkı

Collaptics **oda sıcaklığında klasik dalga tutarlılığıdır**. Seyreltme buzdolabı yok, mikrosaniyelik `T₂` yok, 1000:1 hata düzeltme yükü yok. Kuantumun üssel Hilbert-uzayı vaadini, *üretilebilir, ılık, dayanıklı* analog çöküşle değiştirir — daha dar ama sevk edilebilir bir avantaj.

---

Bkz. [`fotonik-katman.md`](fotonik-katman.md) · [`rezonans-dinamigi.md`](rezonans-dinamigi.md) · [`spekulatif-altkatmanlar.md`](spekulatif-altkatmanlar.md)
