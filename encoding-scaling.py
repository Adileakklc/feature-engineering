#Encoding kategorik verileri sayısal formatlara dönüştürme işlemidir. Makine öğrenmesi ve veri analizi süreçlerinde, modellerin kategorik
#verilerle çalışması zor olduğundan, bu tür verileri sayısal değerlere çevirmek gerekir.

##Label Encoding, kategorik değişkenlerin sınıflarını, her bir sınıfa bir sayısal değer atayarak dönüştüren bir tekniktir.
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Örnek veri
df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue', 'Green']})

# Label Encoder oluştur
label_encoder = LabelEncoder()

# Label Encoding uygulama
df['Color_encoded'] = label_encoder.fit_transform(df['Color'])
#Label encoding'de alfabetik sıralama dikkate alınır.
print(df)
"""
##One-Hot Encoding, kategorik değişkenlerin her sınıfı için ayrı bir sütun oluşturur
# ve o sınıfın gözlemde olup olmadığına göre bu sütunlara 1 ya da 0 değeri atar.
# kategoriler arasında herhangi bir sıralama olmadığında veya sıralama ilişkisini bozmak istemediğimizde tercih ederiz.
"""
import pandas as pd

# Örnek veri seti
df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue', 'Green']})

# One-Hot Encoding uygulama
df_one_hot = pd.get_dummies(df['Color'], prefix='Color').astype(int)

print(df_one_hot)
"""
##Rare Encoding, nadir görülen kategorilerin birleştirilip "Rare" gibi yeni bir kategori oluşturulması işlemidir.
# Bu işlem, modelde nadir kategorilerin aşırı öğrenmeye yol açmasını engelleyip genel performansını artırabilir.
# Çok sayıda kategorik değişkeni olan veri setlerinde boyut küçültme ve performans artırma amaçlı kullanılabilir.
"""
import pandas as pd

# Örnek veri seti
df = pd.DataFrame({
    'City': ['Ankara', 'Istanbul', 'Adana', 'Istanbul', 'Bursa', 'Elazığ', 'Elazığ', 'Adana', 'Malatya', 'Bursa']
})

# Her şehrin gözlem sayısına göre nadir olup olmadığını kontrol etme
threshold = 0.2  # Eşik değeri, %20'nin altındaki frekanslar nadir kabul edilir
city_counts = df['City'].value_counts(normalize=True)

# Nadir görülen şehirleri 'Rare' kategorisi altında toplama
df['City_Encoded'] = df['City'].apply(lambda x: 'Rare' if city_counts[x] < threshold else x)

print(df)
"""
##Feature Scaling(Özellik Ölçeklendirme), makine öğrenmesi ve veri analizi süreçlerinde verilerin boyutlarının standartlaştırılması
# ya da belirli bir aralığa getirilmesi işlemidir. Bu işlem, modelin performansını artırır ve öğrenme sürecini hızlandırır.


