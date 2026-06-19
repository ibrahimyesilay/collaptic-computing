# Fotonik Etkileşim Katmanı

*Taşıyıcı olarak fotonlar: düşük kayıp ve aynı anda birçok serbestlik derecesi.*

Bir elektron genelde tek bir şey için — yükü için — kullanılır. Bir foton ise birçok bağımsız niceliği aynı anda taşır: dalga boyu, faz, kutuplanma, genlik, uzamsal mod, varış zamanı. Tek bir dalga kılavuzunun bir telin taşıyamayacağını taşımasının nedeni budur; Collaptics altkatmanının taşıyıcı katmanı bu yüzden ışıktan kuruludur.

## Bu katmanın görevleri

Kollaptonları düşük kayıpla taşımak ve eşleştirmek; problemin eşleşmelerini `J_ij` ayarlamak; rezonans takvimini `Ω(t)` sürmek; oturmuş alanı okumak.

## Yapı taşları

- **Programlanabilir eşleşme — Si-fotonik MZI örgüleri.** Mach–Zehnder interferometre örgüsü (Reck/Clements ayrışımı) ışıkta keyfi doğrusal dönüşüm uygular; `J_ij` matrisi optik olarak yazılır.
- **Hızlı sürüş — ince-film lityum niyobat (TFLN).** Pockels etkisiyle 100 GHz üzeri elektro-optik modülasyon; tavlama takvimini sürer.
- **Paralel kanallar — mikrohalka + dalga-boyu çoğullama (WDM).** Her dalga boyu bağımsız bir kanal; birçok Kollapton farklı renklerde aynı anda taşınır.
- **Kalıcı optik ağırlık — dalga kılavuzu üzerinde PCM.** GST yamaları ağırlığı optik saklar; belleği ve taşıyıcıyı tek aygıtta birleştirir.
- **Kütlesel paralellik — Kerr frekans tarakları.** Tek pompadan yüzlerce tutarlı tarak çizgisi.

## Alanın okunması

Oturmuş ışığın fazı ve genliği **homodin / heterodin algılama** ile geri kazanılır; faz, Kollaptonun `μ` ve `φ`'sini verir, tekrarlı okumalar varyansı (dolayısıyla çözme gücü `Σ`'yı) verir.

## Dürüst sınır

Derin bir örgüde ekleme kaybı birikir; bu, problem boyutunu sınırlar ve özyinelemeli kodlamayı derin ileri-beslemeli kodlamaya tercih ettirir. Okumalar sık ise analog-sayısal arayüz enerjisi baskın gelebilir.

---

Bkz. [`rezonans-dinamigi.md`](rezonans-dinamigi.md) · [`kollaptik-altkatman.md`](kollaptik-altkatman.md)
