# Çöküş Olay Ufku

*Bir çöküşün artık geri alınamayacağı sınır.*

Çekim havzası ile Çöküş Tekilliği arasında bir yapı daha vardır — geçiş-yok noktası. **Çöküş Olay Ufku**, olasılığın altkatmanın tutarlılık penceresi içinde bir tekillikten artık kaçamayacağı yüzeydir. İçinde çöküş **geri döndürülemez** hâle gelir.

Bu, hiyerarşiyi tamamlar:

```
Bilgi Alanı → Çekim Havzası → Çöküş Olay Ufku → Çöküş Tekilliği
```

## Postüla değil, türetilmiştir

Bir kuyunun içinde, alanın bariyer `V_b`'nin `V(x)` kadar altından kaçma süresi Kramers yasasına uyar:

```
τ_kaçış(x) = τ₀ · exp( β·(V_b − V(x)) )
```

Kaçış yalnızca alan tutarlı kaldığı sürece — tutarlılık süresi `T_φ`'den kısa sürelerde — mümkündür. Ufuk, bu iki sürenin eşit olduğu seviye kümesidir:

```
V_b − V_h  =  (1/β)·ln( T_φ / τ₀ )  =  ΔV_max
```

Ufuk, bariyer tepesinin tam **`ΔV_max` altında** oturur — bir altkatmanın çözebileceği problem zorluğunu sınırlayan aynı `ΔV_max`. Kara delik benzetmesi literalleşir: Schwarzschild yarıçapı kaçış hızının ışık hızına eşit olduğu yer olduğu gibi, Çöküş Olay Ufku da kaçmak için gereken termal sıçramanın, altkatman dekohere olmadan önce gürültü bütçesinin sağlayabileceğini aştığı yerdir.

Karesel bir kuyu `V = ½λr²` için **kollaptik Schwarzschild yarıçapı**:

```
r_h = √( 2·(V_b − ΔV_max) / λ )
```

## Neden önemli

- **Geri-döndürülemezlik / zamanın oku.** İçeri geçmek Landauer entropi bedelini bağlar; çöküş dış iş olmadan geri alınamaz. Ufuk, taahhüt anıdır.
- **Kıl-yok teoremi analoğu.** İçeride trajektorinin geleceği geçmişinden bağımsızdır — alan *başlangıç koşulunu unutur*, yalnızca tekilliğin kimliğini saklar. Kara deliklerin kılı yoktur; taahhüt edilmiş bir çöküşün de.

## Öngörü

Kaçış olasılığı, alan `V_h`'yi geçtiğinde *süper-üssel* düşmelidir; ufuk derinliği `V_b − V_h ∝ ln T_φ` ölçeklenmelidir. Tutarlılık/gözlem süresini değiştirip dönüş olasılığının çöktüğü yeri bulun.

---

İlgili: [`cokus-tekilligi.md`](cokus-tekilligi.md) · [`bilgisel-cokus.md`](bilgisel-cokus.md) · [`../donanim/kollaptik-altkatman.md`](../donanim/kollaptik-altkatman.md)
