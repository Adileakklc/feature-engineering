"""Aykırı değer (outlier), bir veri setinde diğer gözlemlerden
belirgin şekilde farklı olan, veri grubunun genel desenine uymayan gözlemdir.
Bu tür değerler, veri setindeki normal dağılımdan uzak olup,
genellikle aşırı yüksek veya düşük olabilir."""
"""
1. Eşik değer belirle
2. Aykırılara eriş.
3. Hızlıca aykırı değer var mı yok mu .
"""
##Z-Skoru ile Aykırı değer yakalama
import numpy as np
import pandas as pd
"""
#Örnek veri
data = {'Değer': [10,11,13,15,90,13.12,14]}
df = pd.DataFrame(data)

#Z-Skoru hesaplama
df['Z-skoru']= (df['Değer']-df['Değer'].mean())/df['Değer'].std()

outliers = df[np.abs(df['Z-skoru'])> 2]
print(outliers)
print(df)
"""
"""""
##IQR (Interquartile Range) Yöntemi ile Aykırı Değer Yakalama
# Örnek veri
data = {'Değer': [10,11,13,15,19,13,12,14]}
df = pd.DataFrame(data)

# IQR hesaplama
Q1 = df['Değer'].quantile(0.25)
Q3 = df['Değer'].quantile(0.75)
IQR = Q3 - Q1

# Aykırı değerlerin tespiti
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['Değer'] < lower_bound) | (df['Değer'] > upper_bound)]
print(outliers)
"""
"""
##Boxplot ile görsel olarak aykırı değerleri görmek
import matplotlib.pyplot as plt

# Örnek veri
data = {'Değer': [10,11,13,15,19,13,12,14]}
df = pd.DataFrame(data)

# Boxplot oluşturma
plt.boxplot(df['Değer'])
plt.title('Aykırı Değerler')
plt.show()
"""
"""
import pandas as pd
import numpy as np

# Gelişmiş aykırı değer tespit fonksiyonu
def detect_outliers(dataframe, method="iqr", z_threshold=3, exclude_columns=[]):
    -
    *******************************
    Veri setinde aykırı değerleri tespit eden bir fonksiyon. Hem Z-skoru hem de IQR yöntemini destekler.

    Parameters:
    dataframe (pd.DataFrame): Aykırı değerlerin aranacağı veri seti.
    method (str): 'iqr' veya 'zscore' kullanarak aykırı değer tespiti yapılır.
    z_threshold (float): Z-skoru için eşik değeri.
    exclude_columns (list): Aykırı değer tespitinden hariç tutulacak sütunların listesi.

    Returns:
    pd.DataFrame: Aykırı değerler işaretlenmiş bir DataFrame döndürür.
  -*******************************

    # Aykırı değerleri işaretlemek için boş bir DataFrame
    outliers = pd.DataFrame(index=dataframe.index)

    # Verideki sayısal sütunları bulma
    numeric_cols = [col for col in dataframe.columns if dataframe[col].dtype != 'O' and col not in exclude_columns]

    for col in numeric_cols:
        if method == "iqr":
            # IQR yöntemi ile aykırı değer tespiti
            Q1 = dataframe[col].quantile(0.25)
            Q3 = dataframe[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Aykırı değerleri işaretleme
            outliers[col] = ((dataframe[col] < lower_bound) | (dataframe[col] > upper_bound)).astype(int)

        elif method == "zscore":
            # Z-skoru yöntemi ile aykırı değer tespiti
            z_scores = (dataframe[col] - dataframe[col].mean()) / dataframe[col].std()
            outliers[col] = (np.abs(z_scores) > z_threshold).astype(int)

    return outliers

# Örnek veri seti
data = {
    'Age': [10,11,13,15,19,13,12,14,90],
    'Salary': [5000, 5500, 6000, 6500, 7000, 4900, 500000, 5500, 5800],
    'Customer_ID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009']
}

df = pd.DataFrame(data)

# Aykırı değerleri tespit etme (IQR yöntemi ile)
iqr_outliers = detect_outliers(df, method="iqr", exclude_columns=['Customer_ID'])
print("IQR Yöntemi ile Aykırı Değerler:")
print(iqr_outliers)

# Aykırı değerleri tespit etme (Z-skoru yöntemi ile)
zscore_outliers = detect_outliers(df, method="zscore", z_threshold=2, exclude_columns=['Customer_ID'])
print("\nZ-Skoru Yöntemi ile Aykırı Değerler:")
print(zscore_outliers)
"""
"""
import pandas as pd
import numpy as np

# Gelişmiş aykırı değer tespit fonksiyonu (IQR yöntemi kullanılıyor)
def detect_outliers(dataframe, method="iqr", z_threshold=3, exclude_columns=[]):
   
   # Aykırı değerleri tespit eden fonksiyon. IQR yöntemini veya Z-skoru yöntemini kullanabilir.
    
    outliers = pd.DataFrame(index=dataframe.index)
    numeric_cols = [col for col in dataframe.columns if dataframe[col].dtype != 'O' and col not in exclude_columns]

    for col in numeric_cols:
        if method == "iqr":
            Q1 = dataframe[col].quantile(0.25)
            Q3 = dataframe[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers[col] = ((dataframe[col] < lower_bound) | (dataframe[col] > upper_bound)).astype(int)

    return outliers


# Aykırı değerlerin olduğu satırları filtreleme fonksiyonu
def get_outliers(dataframe, outliers_df):
    """
#Aykırı değer olarak işaretlenmiş satırları filtreler ve döndürür.
    """
    outliers_rows = dataframe[outliers_df.sum(axis=1) > 0]  # Eğer herhangi bir sütunda aykırı değer varsa satırı getir
    return outliers_rows


# Örnek veri seti
data = {
    'Age': [10,11,13,15,19,13,12,14,90],
    'Salary': [5000, 5500, 6000, 6500, 7000, 4900, 500000, 5500, 5800],
    'Customer_ID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009']
}

df = pd.DataFrame(data)

# Aykırı değerleri tespit et (IQR yöntemi)
iqr_outliers = detect_outliers(df, method="iqr", exclude_columns=['Customer_ID'])

# Aykırı değer satırlarına erişim
outliers_in_df = get_outliers(df, iqr_outliers)

print("Aykırı Değer Satırları:")
print(outliers_in_df)
"""

"""
Aykırı değer probleminin çözüm yolları
-Aykırı değerleri kaldırmak -> df_cleaned = df[(df['Age'] >= age_lower_bound) & (df['Age'] <= age_upper_bound)]
-Aykırı değerleri dönüştürmek (winsorizing)-> df['Age'] = np.where(df['Age'] > age_upper_bound, age_upper_bound, np.where(df['Age'] < age_lower_bound, age_lower_bound, df['Age']))
-Aykırı değerleri ihmal etmek (robust modeller) -> model = HuberRegressor().fit(X_train, y_train)
-Log Dönüşümü -> df['Salary_log'] = np.log(df['Salary'])
"""
