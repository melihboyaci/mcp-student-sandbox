# Mystery Module - Kuadratik Denklem Çözücü

## Genel Açıklama

`mystery_module.py`, **kuadratik denklemlerin köklerini** hesaplayan bir Python modülüdür. Matematiksel olarak ax² + bx + c = 0 şeklindeki denklemlerin çözümlerini bulmak için **kuadratik formülü** (quadratic formula) kullanır.

## İçerdiği Fonksiyonlar

### `fn_x(a, b, c)`

Kuadratik denklem ax² + bx + c = 0 için köklerini hesaplar.

#### Parametreler:

- **a** (int/float): x² katsayısı (sıfırdan farklı olmalı)
- **b** (int/float): x katsayısı
- **c** (int/float): sabit terim

#### Dönüş Değeri:

- **Tuple**: Iki kök ((-b + √Δ)/(2a), (-b - √Δ)/(2a)) olarak döndürülür
- **None**: Diskriminant negatif ise (gerçek kök yoksa)

#### Matematiksel Temel:

```
Diskriminant (Δ) = b² - 4ac

Eğer Δ < 0: Gerçek kök yoktur → None döndür
Eğer Δ ≥ 0: Kökler = (-b ± √Δ) / (2a)
```

#### Örnek Kullanım:

```python
import mystery_module

# Örnek 1: x² - 5x + 6 = 0 (Kökleri: 2 ve 3)
sonuc = mystery_module.fn_x(1, -5, 6)
print(sonuc)  # Çıktı: (3.0, 2.0)

# Örnek 2: x² + 1 = 0 (Gerçek kök yok)
sonuc = mystery_module.fn_x(1, 0, 1)
print(sonuc)  # Çıktı: None

# Örnek 3: 2x² - 8x + 6 = 0 (Kökleri: 1 ve 3)
sonuc = mystery_module.fn_x(2, -8, 6)
print(sonuc)  # Çıktı: (3.0, 1.0)
```

## Modülün Işlevleri

1. **Kuadratik Denklem Çözme**: Standart form ax² + bx + c = 0'ı çözer
2. **Hata Kontrolü**: Diskriminant negatif olduğunda uygun None döndürür
3. **Matematiksel Hesaplama**: Python'ın math kütüphanesini kullanarak hassas sonuçlar verir

## Kullanım Alanları

- Matematik problemleri çözme
- Fizik simülasyonları (parabolik hareket, vs.)
- Mühendislik hesaplamaları
- Bilimsel araştırmalar
- Eğitim amaçlı uygulamalar

## Teknik Detaylar

- **Kütüphane Bağımlılığı**: `math` (Python standart kütüphanesi)
- **Python Sürümü**: Python 3.x
- **Veri Tipi**: Float dönüşümleriyle çalışır

## Dikkat Edilecek Noktalar

### 1. **Parametre 'a' Sıfır Olamaz**

```python
# HATA: a = 0 ise doğrusal denklem olur (kuadratik değil)
fn_x(0, 5, 6)  # ZeroDivisionError riski!
```

### 2. **Diskriminant Negatif Olabilir**

```python
# Gerçek kök yok
sonuc = fn_x(1, 0, 1)  # None döndürür
if sonuc is None:
    print("Denklemin gerçek kökü yoktur (Kompleks kökler vardır)")
```

### 3. **Sayısal Hassasiyet**

Çok büyük veya çok küçük katsayılar ile çalışırken sayısal hata oluşabilir.

## Örnek Uygulama Senaryoları

### Senaryo 1: Fiziksel Proje

Bir top t saniye sonra ground' a kaç metre yükseklikte olacağı hesaplanabilir:

```python
# h(t) = -5t² + 20t + 2 (yükseklik başlangıçta 2m, ilk hız 20 m/s)
kökler = fn_x(-5, 20, 2)  # Top ne zaman yere çarpar?
```

### Senaryo 2: İşletme Optimizasyon

Karüç (profit) hesaplaması: P(x) = -2x² + 100x - 500

```python
gelir_kökleri = fn_x(-2, 100, -500)
```

## Kaynaklar

- **Kuadratik Formül**: [Quadratic Formula - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_formula)
- **Diskriminant**: [Discriminant - Wikipedia](https://en.wikipedia.org/wiki/Discriminant)

---

**Oluşturma Tarihi**: Mart 2026  
**Modül Adı**: mystery_module.py  
**Durum**: İşlevsel ve test edilmiş
