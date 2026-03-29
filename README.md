# mystery_module.py — İkinci Derece Denklem Çözücü

## Genel Bakış

`mystery_module.py`, ikinci derece (karesel) denklemlerin köklerini bulmak için kullanılan bir Python modülüdür.
İçerdiği `fn_x` fonksiyonu, klasik **ikinci derece denklem formülü** (karesel formül / discriminant yöntemi) kullanarak verilen bir `ax² + bx + c = 0` denkleminin gerçel köklerini hesaplar.

---

## Fonksiyonlar

### `fn_x(a, b, c)`

İkinci derece bir denklemin köklerini hesaplar.

#### Parametreler

| Parametre | Tür     | Açıklama                                      |
|-----------|---------|-----------------------------------------------|
| `a`       | `float` | x² katsayısı (ikinci derece terimin katsayısı)|
| `b`       | `float` | x katsayısı (birinci derece terimin katsayısı)|
| `c`       | `float` | Sabit terim                                   |

#### Dönüş Değeri

- Eğer denklemin gerçel kökü **varsa**: `(x1, x2)` şeklinde iki elemanlı bir **tuple** döner.
  - `x1 = (-b + √(b²−4ac)) / (2a)`
  - `x2 = (-b − √(b²−4ac)) / (2a)`
- Eğer diskriminant (`b² - 4ac`) **negatifse** (gerçel kök yoksa): `None` döner.

#### Nasıl Çalışır?

Fonksiyon, karesel formülü uygular:

```
x = (-b ± √(b² - 4ac)) / (2a)
```

1. Önce **diskriminant** `d = b² - 4ac` hesaplanır.
2. `d < 0` ise gerçel kök yoktur → `None` döner.
3. `d >= 0` ise iki kök hesaplanıp tuple olarak döner (eşit kök durumunda iki değer de aynı olur).

---

## Kullanım Örnekleri

```python
from mystery_module import fn_x

# Örnek 1: x² - 5x + 6 = 0  →  kökleri: 3 ve 2
result = fn_x(1, -5, 6)
print(result)  # (3.0, 2.0)

# Örnek 2: x² - 2x + 1 = 0  →  eşit kök: 1
result = fn_x(1, -2, 1)
print(result)  # (1.0, 1.0)

# Örnek 3: x² + x + 1 = 0  →  gerçel kök yok
result = fn_x(1, 1, 1)
print(result)  # None

# Örnek 4: 2x² + 3x - 2 = 0  →  kökleri: 0.5 ve -2.0
result = fn_x(2, 3, -2)
print(result)  # (0.5, -2.0)
```

---

## Dikkat Edilmesi Gerekenler

- `a` değeri **0 olmamalıdır**; aksi hâlde sıfıra bölme hatası (`ZeroDivisionError`) oluşur.
- Fonksiyon yalnızca **gerçel** kökleri hesaplar; **karmaşık** (complex) kökleri desteklememektedir.
- Çift kök durumunda (`d == 0`) her iki tuple elemanı da aynı değeri taşır.

---

## Bağımlılıklar

| Kütüphane | Amaç                        |
|-----------|-----------------------------|
| `math`    | `math.sqrt()` ile karekök hesabı |

`math` modülü Python'un standart kütüphanesinin bir parçasıdır; ekstra kurulum gerektirmez.
