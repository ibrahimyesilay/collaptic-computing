# Rezonans Dinamiği Katmanı

*Çöküş motoru: cevaba oturan eşleşmiş osilatör ağı.*

Bu, Collaptics altkatmanının hesaplama kalbidir. `0` ile `1` arasında gerilim anahtarlamak yerine makine rezonansla — frekans, faz, girişim, genlik — çalışır. Anahtarlamaz; titreşir ve oturduğu desen çözümdür.

## Çöküş bir çatallanmadır, hesap değil

Eşleşmiş, kazançla sürülen bir osilatör ağı eşik altında geniş, gürültülü bir durumda bekler. Kazanç eşikten geçirilince modlar yarışır ve **en az kayıplı** tek mod kazanıp büyür — bir çatallanma. Kayıp manzarası en düşük-kayıplı mod `V`'nin minimumu olacak şekilde tasarlanırsa, bu kazanan-her-şeyi-alır olayı *bizzat çöküştür*. Kazancı artırmak tavlama takvimidir.

Bu ilke — dağılımlı bir sistemin en-düşük-kayıp yapılandırmasını bulmasına izin vererek hesaplamak — **kazanç–dağılımlı hesaplamadır**.

## Platformlar

- **Tutarlı Ising Makinesi (CIM/DOPO).** Halka içinde dejenere optik parametrik osilatörler faz 0 veya π alır; eşikte ağ en düşük Ising enerjili faz desenine oturur. 100.000+ spin, oda sıcaklığı. Bu katmanın bugünkü en yakın gerçeklemesi.
- **Osilatör Ising Makinesi (OIM).** Eşleşmiş LC/halka/spin-tork osilatörleri, çift frekansta alt-harmonik enjeksiyon kilitlemesiyle (SHIL) 0/π'ye ikilenir. Düz CMOS'ta kurulur.
- **Polariton yoğuşması.** Yarı-ışık yarı-madde bozonlar en yüksek-kazançlı moda yoğuşur; yoğuşma minimuma çöküştür. Doğru malzemeyle oda sıcaklığında.

## Ω = ρ·ω fiziksel olarak nereden gelir

- `ω`: osilatör frekansı (DOPO için ~100 THz, CMOS OIM için GHz). Mod başına enerji ω² ile gider — `Σ = I·Ω²`'deki karenin kökeni.
- `ρ`: faz tutarlılığı; çizgi genişliği belirler, `ρ ≈ 1 − Δν/ν`, tutarlılık süresi `T_φ = 1/(π·Δν)`.

Kullanılabilir sürüş `Ω = ρ·ω`'dır: faz-kilitli değilse yüksek frekans işe yaramaz.

## Asıl sınır dekoheranstır

`T_φ`, rezonatörün faz gürültüsüyle (Leeson modeli) belirlenir ve aşılabilecek bariyer yüksekliğini sınırlar: `ΔV_max ≈ β⁻¹·ln(T_φ/τ₀)`. Daha yüksek Q → daha uzun `T_φ` → daha zor problem. Somut bir malzeme yol haritası.

---

Bkz. [`fotonik-katman.md`](fotonik-katman.md) · [`kollaptik-altkatman.md`](kollaptik-altkatman.md) · [`spekulatif-altkatmanlar.md`](spekulatif-altkatmanlar.md)
