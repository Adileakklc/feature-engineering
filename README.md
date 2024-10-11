# feature-engineering

## Genel Bakış

Bu proje, makine öğrenmesi süreçlerinde özellik mühendisliği tekniklerini uygulamayı amaçlar. Projede aykırı değerlerin tespiti, eksik verilerin yönetimi, kategorik değişkenlerin kodlanması ve ölçeklendirilmesi ile yeni özellikler türetilmesi konuları ele alınmaktadır.

## Proje Yapısı

- **outliers.py**: Aykırı değerlerin tespiti ve yönetimi (Z-Skoru, IQR yöntemi).
- **missing-values.py**: Eksik veri analizi ve doldurma yöntemleri (ortalama, medyan, KNN imputation).
- **encoding-scaling.py**: Kategorik verilerin kodlanması ve sayısal verilerin ölçeklendirilmesi (Label Encoding, One-Hot Encoding, Normalizasyon).
- **feature-extraction.py**: Veriden anlamlı yeni özelliklerin çıkarılması (regex ile isimlerden unvan çıkarımı, tarihsel özellikler).

## Nasıl Çalıştırılır

1. Projeyi klonlayın:
   ```bash
   git clone https://github.com/adileakklc/feature-engineering.git
   ```

3. İlgili Python dosyasını çalıştırın:
   ```bash
   python outliers.py
   python missing-values.py
   python encoding-scaling.py
   python feature-extraction.py
   ```

