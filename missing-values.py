"""
Eksik Değerler (Missing Values), bir veri setinde bazı gözlemler için
ilgili değişkenlerin değerlerinin bulunmadığı durumu ifade eder.
Eksik değerler, analiz ve modelleme sürecinde çeşitli sorunlara yol açabilir
ve bu nedenle düzgün bir şekilde işlenmeleri gerekir.
"""
##Eksik değerleri yakalamak
#df.isnull().sum().sum() ##veri setinde kaç tane eksik değer olduğunu gösteririr
#df.isnull().sum() ##veri setindeki her bir sütundaki eksik değer sayısını verir.
#msno.bar(df) ##eksik değer bar grafiği
#msno.matrix(df) ## eksik değer matrisi
#msno.heatmap(df) ##eksik değerlerin ısı haritası
""""
import pandas as pd
import numpy as np

# Örnek bir veri seti
data = {
    'Age': [25, np.nan, 30, 45, np.nan],
    'Salary': [50000, 60000, np.nan, 45000, 50000],
    'Experience': [5, np.nan, 10, 15, 8]
}

df = pd.DataFrame(data)

# Her sütundaki eksik değer sayısını bulalım
print("Eksik değer sayısı:")
print(df.isnull().sum())

# Eksik değere sahip satırları yakalama
print("\nEksik değere sahip satırlar:")
print(df[df.isnull().any(axis=1)])

# Eksik değerlerin yüzdesini hesaplama
print("\nEksik değer yüzdesi:")
print(df.isnull().sum() / len(df) * 100)
"""
##Eksik değerlerinin problemini çözme
###1-Eksik değerleri doldurma
#df['column'].fillna(df['column'].mean(), inplace=true) ##mean imputation
#df['column'].fillna(df['column'].median(), inplace=true) ##median imputation
#df['column'].fillna(df['column'].mode()[0], inplace=true) ##mode imputation
#df['column'].fillna(0, inplace=true) #belirli bir değer ile doldurma
#df.fillna(method='ffill', inplace=True)  ## İleri doldurma (geri içinde 'bfiil')
###2-Eksik değerleri çıkarma
#df.dropna(inplace=true) ## eksik değere sahip satırları çıkarma
#df.dropna(axis=1, inplace=true) ##eksik değere sahip sütunları çıkarma
###3-Gelişmiş Doldurma Yöntemleri
#df_filled = KNNImputer(n_neighbors=5).fit_transform(df) ##KNN Imputation (K En Yakın Komşu İle Doldurma)
#df_filled = IterativeImputer().fit_transform(df) ##MICE (Multiple Imputation by Chained Equations)
###4-Eksik değerlerin anlamlı olabileceği durumlar
#df['column_missing'] = df['column'].isnull().astype(int) #
###5-Eksik veriyi tahmin etme
"""
import pandas as pd
import numpy as np

# Örnek veri seti
data = {
    'Age': [23, np.nan, 38, 44, np.nan],
    'Salary': [50000, 60000, np.nan, 45000, 50000],
    'Experience': [5, np.nan, 7, 6, 8]
}

df = pd.DataFrame(data)

# Eksik değerleri ortalama ile doldurma
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Eksik değeri medyan ile doldurma
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# Eksik değeri mod ile doldurma
df['Experience'].fillna(df['Experience'].mode()[0], inplace=True)

print(df)
"""
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Örnek veri seti
data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 55000, 70000, 48000],
    'Age': [25, np.nan, 30, 45, np.nan]
}
df = pd.DataFrame(data)

# 1. Eksik olmayan satırları seç ve model eğit
train_data = df[df['Age'].notnull()]
test_data = df[df['Age'].isnull()]

# Kategorik veriyi sayısal hale getirme (X_train ve X_test aynı sütunlara sahip olacak)
X_train = pd.get_dummies(train_data[['Gender', 'Salary']], drop_first=True)
X_test = pd.get_dummies(test_data[['Gender', 'Salary']], drop_first=True)

# Eksik olan sütunları X_test'e eklemek ve doldurmak (modelin gördüğü sütunların tam olduğundan emin ol)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

# Modeli eğit
model = LinearRegression()
model.fit(X_train, train_data['Age'])

# 2. Eksik olan satırlardaki değerleri tahmin et
df.loc[df['Age'].isnull(), 'Age'] = model.predict(X_test)

# Sonuç
print(df)
"""
