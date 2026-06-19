# Örnek: Protein Katlanması

Protein katlanması özünde bir enerji minimizasyonu problemidir: bir amino asit zinciri, en düşük serbest enerjili üç boyutlu yapıya oturur. Bu, bilgisel çöküşün şekliyle aynıdır; bu yüzden Collaptics'ye en doğal oturan durumlardan biridir.

## Eşleme

- Proteinin konformasyonu, yapılandırma `x`'tir.
- Molekülün serbest-enerji yüzeyi, bilgisel potansiyel `V(x)`'tir.
- Doğal katlanmış yapı, baskın minimumdur — bir Çöküş Tekilliği.

Protein *hesaplanmaz*. Çöküşle *keşfedilir*: enerji yüzeyini altkatmana kodla, alanın yokuş aşağı akmasına izin ver, çöküşün oturduğu yapıyı oku.

## Çerçeve neden yardımcı olur

Klasik katlanma simülasyonu, hareket denklemlerini integre etmek ya da konformasyonları aramak için muazzam hesap harcar. Collaptics, minimizasyonu fiziksel bir altkatmana doğrudan yaptırmayı önerir — `V` üzerindeki iniş donanımda, paralel, rezonans dinamiğinin hızında gerçekleşir.

## Dürüst uyarılar

- **Yerel minimumlar.** Bir protein yanlış-katlanmış bir durumda kinetik olarak tuzaklanabilir; bu tam olarak [`../../simulation/RESULTS.md`](../../simulation/RESULTS.md)'teki `P5b` tuzaklanma davranışıdır. Collaptics, garantili küresel değil, *erişilebilir* minimumu bulur.
- **Bariyer yüksekliği.** Katlanma büyük bariyerler aşmayı gerektirdiğinde çöküş süresi `exp(βΔV)` ile büyür — her yöntemin karşılaştığı aynı Arrhenius duvarı.

Yani Collaptics katlanmayı sihirle çözmez. Onu fiziksel bir çöküş olarak yeniden çerçeveler ve manzara geçilebilecek kadar düz olduğunda bir enerji/verim avantajı sunar — ki bu da, cesaret verici biçimde, gerçek proteinlerin güvenilir biçimde katlandığı rejimdir.

---

Bkz. [`hash-tersine-cevirme.md`](hash-tersine-cevirme.md) · [`dil-modeli-cikarimi.md`](dil-modeli-cikarimi.md)
