# Örnek: Kombinatoryal Optimizasyon

Kombinatoryal optimizasyon Collaptics'ye en doğrudan uyan alandır, çünkü çerçeveye ilham veren donanım platformları — tutarlı Ising makineleri, osilatör Ising makineleri, memristör dizileri — tam da bu problemleri çözmek için kuruldu. Collaptics kısmen, bu makinelerin ne yaptığını ortak bir dilde anlatma girişimidir.

## Eşleme

Birçok optimizasyon problemi bir Ising/karesel enerjinin minimizasyonu olarak yazılabilir:

```
V(s) = −½ · Σ_ij J_ij s_i s_j − Σ_i h_i s_i
```

Eşleşmeler `J_ij` ve alanlar `h_i` problemi kodlar; en düşük enerjili yapılandırma `s` optimumdur. Collaptics dilinde `V` bilgisel potansiyeldir, baskın minimumu Çöküş Tekilliğitir, altkatmanın oturması bilgisel çöküştür.

## Collaptics ne sunar

- **Enerji verimliliği.** `V` üzerindeki iniş, bir işlemcinin durumlar arasında adımlaması yerine fizikle — eşleşmiş osilatörler arasındaki kazanç yarışıyla — yapılır.
- **Yerel paralellik.** Tüm eşleşmeler aynı anda etkir; alan difüzyonla birçok yapılandırmayı eşzamanlı keşfeder.
- **Bedava tavlama.** Sürüş `Ω`'yı (ya da gürültü `D`'yi) süpürmek, fiziksel bir tavlama takvimidir.

## Collaptics ne sunmaz

- **En kötü durum zorluğunu çözmez.** NP-zor problemlerde çözüm süresi zor örneklerde hâlâ `exp(βΔV)` ile büyür (test P6). Karmaşıklık sınıflarını değiştirmez.
- **Garantili değil, yaklaşık.** Alan *erişilebilir* çekiciye oturur; yerel minimum olabilir (test P5b). Çıktı yüksek-kaliteli bir adaydır, optimumluk sertifikası değil.
- **Manzaraya bağlı.** Enerji yüzeyi camsı ya da aldatıcı olan problemler zor kalır.

Gerçekçi iddia, Ising-makinesi literatürünün zaten desteklediği iddiadır: yararlı bir problem sınıfında *iyi yaklaşık çözümlere* fiziksel, enerji-verimli bir yol — evrensel bir optimize edici değil.

---

Bkz. [`dil-modeli-cikarimi.md`](dil-modeli-cikarimi.md) · [`protein-katlanmasi.md`](protein-katlanmasi.md) · [`hash-tersine-cevirme.md`](hash-tersine-cevirme.md)
