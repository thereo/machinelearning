# Laporan Proyek Machine Learning - Thereo Sebastiano Rosi

## Domain Proyek

Customer churn atau pergantian pelanggan merupakan salah satu tantangan terbesar yang dihadapi bisnis di berbagai industri. Ketika pelanggan memutuskan untuk berhenti menggunakan produk atau layanan, perusahaan mengalami kerugian pendapatan dan peningkatan biaya untuk mendapatkan pelanggan baru. 

Customer churn merupakan masalah serius bagi bisnis karena dapat mengakibatkan:
  - Kehilangan Pendapatan: Pelanggan yang churn tidak lagi memberikan pendapatan.
  - Biaya Akuisisi Pelanggan: Mendapatkan pelanggan baru jauh lebih mahal daripada mempertahankan pelanggan yang sudah ada.
  - Reputasi yang Rusak: Tingkat churn yang tinggi dapat mempengaruhi reputasi perusahaan.
  - Penurunan Moral Karyawan: Customer churn dapat menurunkan moral karyawan, terutama tim customer service dan sales.

Bagaimana Menyelesaikan Customer Churn:

  1. Identifikasi Penyebab Churn: Lakukan analisis untuk memahami faktor-faktor yang mendorong pelanggan untuk churn. Gunakan data dan feedback pelanggan untuk mengidentifikasi area yang perlu ditingkatkan.
  2. Tingkatkan Customer Experience: Berikan pengalaman pelanggan yang positif di semua titik kontak, termasuk customer service, produk, dan marketing.
  3. Personalisasi Interaksi: Berikan penawaran dan komunikasi yang dipersonalisasi berdasarkan kebutuhan dan preferensi setiap pelanggan.
  4. Bangun Loyalitas Pelanggan: Berikan program loyalitas, penghargaan, dan insentif untuk mempertahankan pelanggan.
  5. Prediksi dan Cegah Churn: Gunakan machine learning untuk memprediksi pelanggan yang berisiko churn dan lakukan intervensi proaktif untuk mempertahankan mereka.

Perusahaan dapat meningkatkan pertumbuhan mereka dan meningkatkan keberadaan basis pelanggan mereka  dengan memprediksi churn pelanggan secara akurat dan menerapkan lebih banyak lagi strategi retensi yang tepat waktu dan lebih terfokus.
  
[Turbocharging growth by taking retention analytics to the next level](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2024/turbocharge-growth-retention-analytics.pdf&ved=2ahUKEwi_mv22se2IAxXozDgGHaoeA0AQFnoECBMQAQ&usg=AOvVaw1e6cJBHRLQaKMJF7-9coLW) 

## Business Understanding

### Problem Statements
  - Bagaimana cara mengurangi tingkat customer churn dan meningkatkan retensi pelanggan?
  - Bagaimana cara mengidentifikasi pelanggan yang berisiko churn secara akurat dan tepat waktu?
  - Bagaimana cara mengembangkan strategi retensi pelanggan yang lebih efektif, personal, dan tepat sasaran?

### Goals
  - Mengurangi tingkat customer churn dan meningkatkan retensi pelanggan.
  - Mengembangkan model machine learning yang mampu memprediksi pelanggan yang berisiko churn dengan akurasi tinggi.
  - Memberikan rekomendasi strategi retensi yang lebih personal dan tepat sasaran berdasarkan hasil prediksi model.

### Solution statements
  - Membangun model machine learning menggunakan algoritma Random Forest Classifier untuk memprediksi probabilitas customer churn. Model ini akan dilatih dengan data historis pelanggan yang mencakup berbagai fitur seperti demografi, riwayat pembelian, dan interaksi pelanggan.
  -  Menganalisis feature importances dari model Random Forest Classifier untuk mengidentifikasi faktor-faktor penting yang mempengaruhi customer churn. Informasi ini akan digunakan untuk mengembangkan strategi retensi yang lebih tepat sasaran.

## Data Understanding
Dataset yang digunakan dalam proyek ini memiliki 440.833 entri dengan 12 fitur yang relevan dengan churn pelanggan. Dataset ini berisi informasi tentang karakteristik pelanggan seperti usia, jenis kelamin, durasi berlangganan, jumlah panggilan dukungan, tipe kontrak, dan total pengeluaran.

[Kaggle](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset).

- **Duplicated Values**: Tidak ditemukan duplikat dalam dataset. Setiap entri unik.
- **Null Values**: Dataset telah diperiksa terhadap missing values, dan menemukan bahwa setiap kolom yang memiliki nilai null sebanyak 1

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
  - CustomerID: ID unik pelanggan.
  - Age: Usia pelanggan.
  - Gender: Jenis kelamin pelanggan.
  - Tenure: Durasi pelanggan menggunakan layanan.
  - Usage Frequency: Frekuensi penggunaan layanan.
  - Support Calls: Jumlah panggilan dukungan pelanggan.
  - Payment Delay: Apakah pelanggan mengalami keterlambatan pembayaran.
  - Subscription Type: Jenis langganan pelanggan.
  - Contract Length: Panjang kontrak langganan.
  - Total Spend: Total pengeluaran pelanggan selama berlangganan.
  - Last Interaction: Waktu terakhir pelanggan berinteraksi dengan layanan.
  - Churn: Apakah pelanggan churn atau tidak (label target).

Sebelum membangun model prediktif, dilakukan Exploratory Data Analysis (EDA) untuk memahami karakteristik dan pola data customer churn. 
  - EDA diawali dengan menampilkan beberapa baris pertama data dan melihat informasi umum seperti tipe data dan nilai yang hilang. 
  - Statistik deskriptif seperti rata-rata, standar deviasi, dan kuantil juga dihitung untuk setiap variabel numerik.

## Data Preparation

Data customer churn mentah seringkali tidak siap untuk langsung digunakan dalam pembangunan model machine learning. Oleh karena itu, diperlukan tahap data preparation untuk membersihkan, mentransformasi, dan mempersiapkan data agar sesuai dengan kebutuhan model dan meningkatkan kinerja prediksi.

Berikut adalah proses data preparation yang dilakukan pada dataset customer churn:
  1. Menghapus variabel yang tidak relevan: Variabel CustomerID dihapus karena hanya berisi ID unik setiap pelanggan dan tidak memiliki hubungan dengan prediksi churn.
  2. Menangani missing values: Data diperiksa untuk missing values.
  3. Label Encoding: Variabel target Churn diubah menjadi format numerik (0 dan 1) menggunakan Label Encoding.
  4. One-Hot Encoding: Variabel kategorikal lainnya diubah menjadi variabel dummy menggunakan one-hot encoding.
  5. Splitting Data:  Membagi dataset menjadi dua bagian: training set dan testing set dengan rasio 80:20
  6. Standarisasi Data: Proses transformasi data numerik agar memiliki rata-rata 0 dan deviasi standar 1

Tujuan :
  1. Variabel yang tidak relevan dapat menambah dimensi data dan memperlambat proses pelatihan model, tanpa memberikan informasi yang bermanfaat.
  2. Missing values dapat menyebabkan bias dalam model dan mengurangi akurasi prediksi.
  3. Sebagian besar algoritma machine learning memerlukan variabel target dalam format numerik.
  4. Algoritma machine learning tidak dapat memproses data kategorikal secara langsung. One-hot encoding mengubah variabel kategorikal menjadi format numerik yang dapat dipahami oleh model.
  5. Hal ini penting untuk mengetahui seberapa baik model dapat menggeneralisasi ke data baru dan menghindari overfitting.
  6. Standarisasi data dilakukan agar fitur-fitur dengan skala yang berbeda tidak mendominasi proses pelatihan model.

## Modeling

Pada tahap modeling, algoritma Random Forest Classifier digunakan untuk membangun model prediktif customer churn. Random Forest adalah algoritma ensemble learning yang bekerja dengan membangun banyak pohon keputusan (decision trees) dan menggabungkan hasil prediksi dari setiap pohon untuk menghasilkan prediksi akhir.

Parameter yang Digunakan:
  - n_estimators = 100: Jumlah pohon keputusan dalam forest.
  - random_state = 42: Nilai seed untuk menjamin reproducibility hasil.

Kelebihan Random Forest:
  - Kinerja tinggi: Random Forest seringkali menghasilkan akurasi prediksi yang tinggi.
  - Robust terhadap overfitting: Karena menggunakan banyak pohon keputusan yang dilatih pada subset data yang berbeda.
  - Mampu menangani data high-dimensional: Dapat menangani dataset dengan banyak variabel.
  - Memberikan feature importances: Dapat mengidentifikasi variabel yang paling penting dalam prediksi.

Kekurangan Random Forest:
  - Kompleksitas: Model Random Forest bisa menjadi kompleks dan sulit diinterpretasi.
  - Membutuhkan memori yang besar: Terutama jika forest memiliki banyak pohon keputusan.
  - Waktu pelatihan yang lama: Dibandingkan dengan beberapa algoritma lain, Random Forest dapat membutuhkan waktu pelatihan yang lebih lama.

Model Random Forest dilatih menggunakan data training yang telah di-scale menggunakan StandardScaler. Scaling data dilakukan untuk menyeragamkan skala variabel numerik, sehingga mencegah variabel dengan skala lebih besar mendominasi proses pelatihan.

## Evaluation

Kinerja model Random Forest Classifier dievaluasi menggunakan beberapa metrik

  - Cross-validation dengan 5 fold digunakan untuk mengevaluasi kinerja model. Hasil cross-validation menunjukkan bahwa model memiliki accuracy rata-rata sekitar 0.9996 (atau 99%).
  - Selain itu, confusion matrix digunakan untuk memvisualisasikan kinerja model. Confusion matrix menunjukkan hanya menunjukkan bahwa 2 false positive dan 31 false negative 
  - Feature importances dari model Random Forest juga dianalisis untuk mengidentifikasi variabel yang paling berpengaruh dalam prediksi churn. Visualisasi feature importances menunjukkan Support Calls dan Total Spend adalah yang paling berpengaruh terhadap churn

Cara Kerja Metrik
  - Cross-validation adalah teknik untuk mengevaluasi kinerja model machine learning dengan membagi dataset menjadi beberapa bagian (fold). Model dilatih pada sebagian data dan diuji pada sisa data. Proses ini diulang beberapa kali, dengan setiap fold bergantian menjadi data uji. Hasil evaluasi dari setiap fold kemudian di rata-ratakan untuk mendapatkan estimasi kinerja model yang lebih robust.
  - Confusion Matrix adalah tabel yang memvisualisasikan kinerja model klasifikasi. Tabel ini menunjukkan jumlah TP, TN, FP, dan FN.
  - Feature importances mengukur seberapa penting setiap variabel dalam prediksi model Random Forest. Variabel dengan feature importances yang tinggi memiliki pengaruh yang lebih besar terhadap prediksi model.

Pengembangan model machine learning menggunakan algoritma Random Forest Classifier berhasil dilakukan untuk memprediksi probabilitas customer churn. Analisis feature importances dari model memberikan insight mengenai faktor-faktor penting yang mempengaruhi churn. Hasil prediksi dan analisis ini akan dimanfaatkan untuk mengembangkan strategi retensi pelanggan yang lebih personal dan tepat sasaran, yang diharapkan dapat mengurangi tingkat customer churn dan meningkatkan retensi pelanggan.

**---Ini adalah bagian akhir laporan---**

