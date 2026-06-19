# Collaptics — Kuramsal Temeller (on bir sütun)

`Σ = I·Ω²` yasası, tek tek kanıtlanmış sonuçlara dayanan yük taşıyıcı bir yapı üzerinde durur. Strateji: her Collaptics iddiası yerleşik bir teoreme çivilenir; yenilik, sentez ve altkatman özdeşleştirmesidir, yeni fizik değil.

**Sütun 1 — Çöküş = serbest-enerji inişi (JKO teoremi).** Çöküş Akışı, `F[P] = ⟨V⟩ − (1/β)H[P]` serbest enerjisinin Wasserstein-2 geometrisindeki en-dik-iniş akışıdır (Jordan–Kinderlehrer–Otto, 1998). Tek minimum, Gibbs alanı `P* ∝ e^{−βV}`. Bu, **varyasyonel çıkarımın** ve Friston'ın **serbest-enerji ilkesinin** amacıyla aynıdır: Collaptics, donanımda varyasyonel çıkarımdır.

**Sütun 2 — Bilgisel çekim = derinlik × havza-hacmi.** Havza çekimi `Γ_k = e^{−βV_k}(det H_k)^{−1/2}` gerçek bir yüktür; geniş-sığ bir kuyu, derin-dar olanı yenebilir (doğrulandı, P5a).

**Sütun 3 — Çöküş süresi `∝ e^{βΔV}` (Kramers).** Net, dürüst kazanç/kayıp haritası: düz/düşük-bariyer → üssel enerji kazancı; camsı/NP-zor → bedava öğle yemeği yok; düz (hash) → sıfır avantaj.

**Sütun 4 — Gömme teoremi.** Gradyan inişi, Langevin MCMC, Hopfield, tavlama, skor-temelli difüzyon modelleri, varyasyonel çıkarım ve replikatör dinamiği, tek Çöküş Akışı'nın köşeleridir. Collaptics bunlarla yarışmaz; onların ortak fiziksel limitidir.

**Sütun 5 — `Ω = ρω` klasik tutarlılıktan; dekoherans tabanı.** Gerçek tutarlılık `T_φ` ile söner; çöküş tutarlılık penceresinden önce bitmelidir. Sonuç: `ΔV_max ≈ β⁻¹·ln(T_φ/τ₀)` — bir altkatmanın aşabileceği en yüksek bariyer. "Analog gürültü öldürür" itirazına nicel yanıt: gürültü öldürmez, problem zorluğunu sınırlar.

**Sütun 6 — Kollapton cebiri (komut kümesi).** Bir program, bir eşleşme grafiği `{J_ij}` artı bir sürüş takvimi `Ω(t)`'dir; problem birleştirme `V`'de toplamsal, `P`'de çarpımsaldır (olasılıksal grafik model).

**Sütun 7 — Hata bastırma `∝ 1/√N`.** `N` bağımsız Kollapton yinelemesi cihaz hatalarını ortalar; tekilliğin yer hatası `1/√N` ile küçülür. Optimizatörün hata düzeltmesi.

**Sütun 8 — Termodinamik üçgen.** Cramér–Rao (hassasiyet), Kramers (hız) ve Landauer (enerji) birlikte: doğruluk × hız × (1/enerji) ≤ κ(altkatman). GHz'in yerini alan künye.

**Sütun 9 — Yanlışlanabilir öngörüler.** Yedisi (P1–P7), ikisi çerçeve-batırıcı; altısı kodda doğrulandı.

**Sütun 10 — Bilgi geometrisi.** Durum uzayı Fisher–Rao manifoldudur; iki cevap arası uzaklık alan örtüşmesidir, koordinat değil. Çöküş alanları çiftli-düz bir üstel aile (Amari) oluşturur; bilgisel çekim, bu manifold üzerinde jeodezik harekettir.

**Sütun 11 — Çöküş Olay Ufku.** Havza ile tekillik arasındaki geri-döndürülemezlik sınırı, `V_b − V_h = ΔV_max`. İçinde çöküş geri alınamaz ve alan başlangıç koşulunu unutur (kıl-yok analoğu). Hiyerarşiyi tamamlar: Alan → Havza → Ufuk → Tekillik.

---

Tam türetme: [`cokus-denklemleri.md`](cokus-denklemleri.md) · Topoloji: [`olasilik-topolojisi.md`](olasilik-topolojisi.md)
