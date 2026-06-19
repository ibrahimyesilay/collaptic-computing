# Örnek: Dil Modeli Çıkarımı

Büyük dil modelleri zaten olasılıksal makinelerdir. Üretimin her adımı, bir sonraki token üzerinde bir olasılık dağılımı üretir; model sonra ondan örnekler. Asıl nesne dağılımdır — altındaki ikili aritmetik yalnızca bugünün donanımının onu *taklit etme* biçimidir.

Collaptics için en doğrudan açılım budur: dağılımı trilyonlarca ikili işlemle hesaplamak yerine donanımda temsil etmek.

## Eşleme

```
Soru → Olasılık Topolojisi → Çöküş Tekilliği → Bilgisel Çöküş → Cevap
```

- İstem ve model, olası devamlar üzerinde bir bilgisel potansiyel tanımlar.
- En olası devam, baskın çekicidir.
- Bir token örneklemek, alanın tek bir sonuca çöküşüdür.

## Neden zorlama bir benzetme değil

Çerçevenin gömme teoremi (bkz. [`../matematik/kuramsal-temeller.md`](../matematik/kuramsal-temeller.md)), **skor-temelli difüzyon modellerinin** Çöküş Akışı'nın bir köşesi olduğunu gösterir: ters-difüzyon örneklemesi tam olarak `dx = −Ω²∇V dt + √(2D)ξ`'tir, `V = −(1/β)·log p` ile. Modern üretici modeller zaten Collaptics'nin çekirdek denkleminin ayrıklaştırılmış, taklit edilmiş bir sürümünü çalıştırır. Olasılıksal bir altkatman onu yerel (native) çalıştırırdı.

Kazanç enerjidedir. Çöküş Yasası, çözme gücünün sabit bilgi ve sabit manzarada `Ω²` ile ölçeklendiğini söyler — tutarlı bir altkatman, sayısal bir makinenin işlemlerle ödediği hassasiyeti fizikten satın alır.

## Nereye uyar, nereye uymaz

- **İyi uyum:** öğrenilmiş düz manzaralarda çıkarım ve örnekleme — tam da eğitilmiş bir modelin sağladığı şey.
- **Uymaz:** düz ya da çekişmeli manzaralar veya garantili küresel optimum gerektiren görevler. Collaptics örnekler ve yakınsar; kapsamlı arama yapmaz.

Gerçekçi iddia dar ve somuttur: "Collaptics sinir ağlarının yerini alır" değil, "olasılıksal bir modelin çıkarım adımı fiziksel bir çöküştür ve onu olasılıksal bir altkatmanda çalıştırmak çok daha ucuz olabilir."

---

Bkz. [`protein-katlanmasi.md`](protein-katlanmasi.md) · [`optimizasyon.md`](optimizasyon.md)
