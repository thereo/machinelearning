# -*- coding: utf-8 -*-
"""Submission 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vDLWaIO37aHcsuQ4ZJ_Yi48xr_uKkncY
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

"""# Tahap Data Loading

Pada tahap ini, saya memuat dataset churn pelanggan menggunakan pustaka `pandas`. Dataset ini berisi data pelanggan yang digunakan untuk memprediksi apakah seorang pelanggan akan churn atau tidak. Data ini mencakup berbagai fitur seperti usia, jenis kelamin, durasi langganan, frekuensi penggunaan, dan lain-lain.
"""

df = pd.read_csv("customer_churn_dataset-training-master.csv")

"""# Tahap Exploratory Data Analysis (EDA)

Pada tahap Exploratory Data Analysis (EDA), saya membuat berbagai visualisasi untuk memahami distribusi data dan hubungan antar fitur. Dengan EDA, kita dapat mengidentifikasi pola yang mungkin berguna untuk pemodelan prediktif.
"""

df.head()

df.info()

df.describe()

"""# Tahap Data Cleaning

Pada tahap ini, saya membersihkan data dari nilai-nilai yang hilang, duplikat, dan anomali. Nilai yang hilang dapat menyebabkan bias dalam model, oleh karena itu perlu dihapus atau diimputasi. Selain itu, deteksi dan penghapusan data duplikat dilakukan untuk memastikan kualitas data yang akan digunakan dalam analisis lebih lanjut.
"""

df = df.drop('CustomerID', axis=1)

df.isnull().sum()

df.dropna(inplace=True)

df.duplicated().sum()

"""# Tahap Feature Engineering

Pada tahap ini, saya melakukan rekayasa fitur dengan menambahkan, mengubah, atau mengelompokkan fitur yang sudah ada agar lebih informatif bagi model. Salah satu teknik yang digunakan adalah mengonversi variabel kategorikal seperti `Gender` dan `Subscription Type` menjadi format numerik dengan menggunakan teknik encoding.
"""

le = LabelEncoder()
df['Churn'] = le.fit_transform(df['Churn'])

df = pd.get_dummies(df, drop_first=True)

"""# Tahap Splitting Data

Dataset dibagi menjadi dua bagian, yaitu training set dan test set, dengan rasio 80:20. Data training digunakan untuk melatih model, sedangkan data test digunakan untuk mengevaluasi kinerja model pada data yang belum pernah dilihat sebelumnya.
"""

X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""# Tahap Pemodelan

Pada tahap ini, saya membangun model prediksi churn pelanggan menggunakan algoritma Random Forest Classifier. Algoritma ini bekerja dengan membangun beberapa pohon keputusan dari subset data yang berbeda dan menggabungkan hasil prediksi dari semua pohon untuk menghasilkan prediksi final yang lebih akurat.
"""

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

"""# Tahap Evaluasi Model

Pada tahap ini, saya mengevaluasi kinerja model dengan menggunakan cross-validation
"""

y_pred = model.predict(X_test)

scores = cross_val_score(model, X, y, cv=5)
print(scores)
print(f"Average accuracy: {scores.mean():.4f}")

cm = confusion_matrix(y_test, y_pred)
print(cm)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Churn', 'Churn'], yticklabels=['No Churn', 'Churn'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()

importances = model.feature_importances_
features = X.columns
indices = np.argsort(importances)

plt.figure(figsize=(10, 6))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()