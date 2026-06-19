# Bilgisel Çöküş

*Collaptics'nin tanımlayıcı mekanizması: dağıtık bir olasılık alanının tek bir beliren çözüme yakınsaması.*

```
Klasik:  Girdi → Komutlar → Çıktı
Collaptics:     Olasılık Alanı → Rezonans → Çekici → Çöküş → Beliren Çözüm
```

Sistem son derece dağıtık, yüksek-entropili bir durumdan başlar — milyonlarca, milyarlarca aday çözüm bir arada bulunur. Rezonans ve bilgisel çekim aracılığıyla alan yeniden örgütlenir ve sonunda tek bir baskın yapıya doğru **çöker**. O çöküş cevaptır.

> Makine hesaplamaz. Yakınsar. Mantık yürütmez; oturur.

## Arkasındaki tek denklem

Çöküş, tek bir stokastik akışın — **Çöküş Akışı'nın** — evrimidir:

```
dx/dt  =  −Ω²·∇V(x)  +  √(2D)·ξ(t)
```

Alan, tutarlı rezonansın belirlediği `Ω²` hızıyla `−∇V` boyunca yokuş aşağı yuvarlanır; bu sırada gürültü `ξ` onu keşifte tutar. Tutarlılık arttıkça (ya da gürültü azaldıkça) alan en derin çekiciye keskinleşir. Tam türetme: [`../matematik/cokus-denklemleri.md`](../matematik/cokus-denklemleri.md).

## Gürültü bir kusur değil, bir kaynaktır

İkili hesaplamada gürültü hatadır. Collaptics'de `√(2D)·ξ` gürültü terimi **arama mekanizmasıdır** — alanın sığ tuzaklardan kaçıp keşfetmesini sağlar. `Ω²/D` oranı tam olarak bir ters sıcaklık gibi davranır: tutarlılığı artırmak, alanı soğutmakla aynıdır (doğrulandı: test P2).

## Çöküş ne zaman başarısız olur

Çöküş, doğru cevaba ancak alan havzalar arası bariyerleri aşabildiğinde varır. Bariyerler yüksekken alan **kinetik olarak tuzaklanır** ve yanlış kuyuya oturur — çöküş süresi `exp(βΔV)` ile büyür (doğrulandı: test P5b, P6). Bütün çerçevenin dürüst sınırı budur: düz, geçilebilir manzaralarda enerji/verim avantajı; evrensel bir çözücü değil.

---

İlgili: [`kollapton.md`](kollapton.md) · [`cokus-tekilligi.md`](cokus-tekilligi.md) · [`bilgi-geometrisi.md`](bilgi-geometrisi.md)
