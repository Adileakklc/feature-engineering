#Feature Extraction (Özellik Çıkarımı), veriden anlamlı ve faydalı özellikler türetme işlemidir.
##binary features
"""
import seaborn as sns

# Titanic veri setini yükleme
df = sns.load_dataset('titanic')

# Sütun adlarını kontrol etme
print(df.columns)

# deck sütununa göre yeni bir binary sütun oluşturma
df["NEW_DECK_BOOL"] = df["deck"].notnull().astype('int')

# Sonuçları görme
print(df[["deck", "NEW_DECK_BOOL"]].head())
"""
##text features
"""
import pandas as pd

# Örnek veri seti
data = {'Name': ['Dr. John Smith', 'Mr. Alex Doe', 'Dr. Jane Doe', 'Miss Lucy Hale', 'Mr. John Doe'],
        'Survived': [1, 0, 1, 1, 0]}
df = pd.DataFrame(data)

# Yeni özellikler oluşturma
df["NEW_NAME_COUNT"] = df["Name"].str.len()  # İsim uzunluğu
df["NEW_NAME_WORD_COUNT"] = df["Name"].apply(lambda x: len(str(x).split(" ")))  # Kelime sayısı

# "Dr" ile başlayan isimleri tespit etme
df["NEW_NAME_DR"] = df["Name"].apply(lambda x: 1 if x.startswith("Dr") else 0)

# "NEW_NAME_DR" gruplarına göre "Survived" ortalamasını hesaplama
result = df.groupby("NEW_NAME_DR").agg({"Survived": "mean"})

print(df)
print(result)
"""
##date features
"""
import pandas as pd
from datetime import date

# Titanic veri setini doğru dosya yolu ile yükleme
dff = pd.read_csv(r"C:\Users\user\Downloads\Titanic-Dataset.csv")

# İlk birkaç satırı görüntüleme
print(dff.head())

# Eğer Timestamp veya tarih içeren başka bir sütun yoksa, bir tarih sütunu ekleyin
dff['Timestamp'] = pd.to_datetime('2023-10-07')  # Bu kısım örnek tarih ile doldurulmuş

# Yıl çıkarma
dff['year'] = dff['Timestamp'].dt.year

# Ay çıkarma
dff['month'] = dff['Timestamp'].dt.month

# Yıl farkı
dff['year_diff'] = date.today().year - dff['Timestamp'].dt.year

# Ay farkı (iki tarih arasındaki ay farkı)
dff['month_diff'] = (date.today().year - dff['Timestamp'].dt.year) * 12 + date.today().month - dff['Timestamp'].dt.month

# Gün adı
dff['day_name'] = dff['Timestamp'].dt.day_name()

# İşlem sonrası ilk 5 satırı gösterme
print(dff.head())
"""

