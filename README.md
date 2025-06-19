# **Proyek Akhir: Menangani Permasalahan Perusahaan Edutech**

## Pemahaman Bisnis

Jaya Jaya Institut, sebuah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000, dikenal dengan reputasinya yang baik dalam menghasilkan lulusan berkualitas. Meskipun demikian, institusi ini menghadapi masalah serius terkait dengan tingginya tingkat mahasiswa yang tidak menyelesaikan pendidikannya, atau yang lebih dikenal dengan istilah dropout. Masalah ini membutuhkan perhatian mendalam untuk dianalisis agar pihak institut dapat mengambil langkah-langkah preventif yang lebih tepat, seperti memberikan intervensi kepada mahasiswa yang berisiko mengalami dropout.

Jaya Jaya Institut berencana untuk memanfaatkan data mahasiswa guna melakukan analisis dan prediksi menggunakan metode machine learning. Dengan adanya prediksi ini, diharapkan dapat membantu institusi dalam merancang strategi pembinaan yang lebih efektif. Selain itu, mereka juga membutuhkan dashboard visualisasi yang dapat memantau performa mahasiswa secara berkala, memungkinkan identifikasi lebih dini terhadap mahasiswa yang mungkin berisiko dropout.

### Permasalahan Bisnis

Proyek ini berfokus pada penyelesaian beberapa permasalahan bisnis yang dihadapi oleh Jaya Jaya Institut, di antaranya:

1. **Tingginya Tingkat Dropout**

   Tingginya angka mahasiswa yang dropout dapat merugikan reputasi institusi dan kualitas pendidikan yang diberikan. Hal ini dapat mengurangi kepercayaan calon mahasiswa dan orang tua terhadap Jaya Jaya Institut.

2. **Kehilangan Pendapatan**

   Setiap mahasiswa yang dropout berarti hilangnya pendapatan dari biaya kuliah dan sumber pendapatan lainnya, yang dapat berdampak pada kestabilan finansial institusi.

3. **Pengaruh terhadap Akreditasi**

   Tingkat kelulusan yang rendah dapat mempengaruhi status akreditasi institut, yang berpotensi menurunkan daya tarik institusi di mata calon mahasiswa.

5. **Keterbatasan dalam Analisis dan Prediksi Dropout**

   Hingga saat ini, belum ada pemahaman yang cukup mengenai faktor-faktor yang mempengaruhi tingginya angka dropout. Selain itu, belum ada sistem yang dapat digunakan untuk memprediksi mahasiswa yang berisiko mengalami dropout, yang dapat membantu institusi dalam melakukan intervensi lebih dini.

### Cakupan Proyek
1. Mengumpulkan dan memproses data mahasiswa.
2. Menganalisis data untuk menemukan pola dan faktor-faktor yang mempengaruhi dropoutnya mahasiswa.
3. Membangun model prediktif menggunakan algoritma Random Forest Classifier.
4. Pembuatan Business Dashboard: Mendesain dan membangun dashboard yang dapat menampilkan indikator dropout secara visual, serta mendukung pengambilan keputusan pihak Jaya jaya institution berdasarkan data yang ada.
5. Insight dan Rekomendasi: Memperoleh insight berbasis data dan memberikan rekomendasi konkret (recommendation action item) untuk menurunkan tingkat dropout.


### Persiapan

Sumber data: Dataset yang digunakan pada proyek ini merupakan data mahasiswa perguruan tinggi Jaya Jaya Institut yang dapat diakses melalui [Data Students Jaya Jaya Institut]("https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance"). 

Kumpulan dataset *Students Performance* diperoleh dari berbagai lembaga pendidikan tinggi, yang terdiri dari beberapa basis data terpisah. Dataset ini mencakup informasi terkait mahasiswa yang terdaftar dalam berbagai program gelar sarjana, seperti agronomi, desain, pendidikan, keperawatan, jurnalisme, manajemen, layanan sosial, dan teknologi. Data yang tersedia meliputi informasi yang diperoleh saat pendaftaran mahasiswa, seperti jalur akademik, demografi, serta faktor sosial-ekonomi, serta kinerja akademik mahasiswa pada akhir semester pertama dan kedua.

Dataset Students Performance terdiri dari 37 fitur dan 4424 entry data. Penjelasan fitur yang terdapat pada dataset ini termasuk:
1. `Marital_status` : Status pernikahan mahasiswa
2. `Application_mode` : Metode aplikasi yang digunakan oleh mahasiswa 
3. `Application_order` : Urutan Pendaftaran mahasiswa
4. `Course` : Jurusan yang diambil oleh mahasiswa
5. `Daytime_evening_attendance` :  Waktu kelas yang dihadiri 
6. `Previous_qualification` :  Kualifikasi yang diperoleh oleh mahasiswa sebelum mendaftar di pendidikan tinggi
7. `revious_qualification_grade` : Nilai kualifikasi sebelumnya
8. `Nacionality` : Kewarganegaraan mahasiswa
9. `Mothers_qualification` :  Kualifikasi ibu mahasiswa
10. `Fathers_qualification` : Kualifikasi ayah mahasiswa
11. `Mothers_occupation` : Pekerjaan ibu siswa
12. `Fathers_occupation` : Pekerjaan ayah siswa
13. `Admission_grade` : Nilai penerimaan
14. `Displaced` : Menunjukkan apakah mahasiswa tersebut orang terlantar atau tidak
15. `Educational_special_needs` : menunjukkan apakah mahasiswa memiliki kebutuhan pendidikan khusus
16. `Debtor` : Menunjukkan apakah siswa adalah debitur
17. `Tuition_fees_up_to_date` : Menunjukkan apakah biaya kuliah menunggak
18. `Gender` : Jenis kelamin
19. `Scholarship_holder` : Menunjukkan apakah mahasiswa mendapatkan beasiswa
20. `Age_at_enrollment`: Usia mahasiswa ketika mendaftar.
21. `International` :  Menunjukkan apakah mahasiswa merupakan international student atau bukan.
22. `Curricular_units_1st_sem_credited` : Jumlah satuan kurikulum yang dikreditkan oleh mahasiswa pada semester pertama
23. `Curricular_units_1st_sem_enrolled` :  Satuan kurikulum yang didaftarkan oleh mahasiswa pada semester pertama
24. `Curricular_units_1st_sem_evaluations` : Jumlah evaluasi terhadap satuan kurikulum di semester pertama
25. `Curricular_units_1st_sem_approved` :  Jumlah satuan kurikulum yang disetujui oleh mahasiswa pada semester pertama.
26. `Curricular_units_1st_sem_grade` :  Nilai yang diiperolah pada semester pertama
27. `Curricular_units_1st_sem_without_evaluations` : Jumlah satuan kurikulum tanpa evaluasi pada semester pertama
28. `Curricular_units_2nd_sem_credited`: Jumlah satuan kurikulum yang dikreditkan pada semester kedua
29. `Curricular_units_2nd_sem_enrolled` : Jumlah satuan kurikulum yang didaftarkan oleh mahasiswa pada semester kedua
30. `Curricular_units_2nd_sem_evaluations` : Jumlah evaluasi terhadap satuan kurikulum di semester pertama
31. `Curricular_units_2nd_sem_approved` : Satuan kurikulum yang disetujui oleh mahasiswa pada semester kedua.
32. `Curricular_units_2nd_sem_grade` : Nilai yang diiperolah pada semester kedua
33. `Curricular_units_2nd_sem_without_evaluations` :  Jumlah satuan kurikulum tanpa evaluasi pada semester kedua
34. `Unemployment_rate` : Tingkat pengangguran
35. `Inflation_rate` : Tingkat inflasi
36. `GDP` : Indikator ekonomi yang mempengaruhi kesuksesan akademik dan kemungkinan siswa mengalami dropout
37. `Status` : Target: berupa status mahasiswa saat ini


**Setup environment:**

Berikut langkah-langkah untuk mempersiapkan environment:
1. Menjalankan Notebook
- Jika menggunakan Anaconda, jalankan perintah berikut:
    ```
    conda create --name main-ds python=3.9
    conda activate main-ds
    pip install -r requirements.txt
    ```
- Jika menggunakan Shell/Terminal, jalankan perintah berikut:
    ```
    pip install pipenv
    pipenv install
    pipenv shell
    pip install -r requirements.txt
    ```
    
-  Jalankan file `notebook.ipynb` untuk melihat seluruh hasil analisis data beserta insight yang diperoleh dari data. Anda dapat menggunakan Jupyter notebook atau IDE lokal lainnya, atau anda dapat memanfaatkan IDE lain seperti Google Collab jika ingin menjalanakan proyek secara online.

2. Menjalankan Streamlit
- Akses melalui link berikut: https://dashboard-data-science-institution-labibaadinda.streamlit.app/
    
- Jika ingin menjalankan di lokal, jalankan perintah : 
    ```
    streamlit run app.py
    ```

3. Menjalankan Dashboard

**Akses Dashboard Metabase**



**Langkah 1: Instal Docker**

1. **Unduh dan Instal Docker Desktop**:

   **Instal Docker di Windows**:

      * Kunjungi [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) dan unduh installer.

   **Instal Docker di Linux**:

      * Di **Ubuntu** atau distribusi berbasis Debian, jalankan perintah berikut:

      ```bash
      sudo apt update
      sudo apt install docker.io
      ```
      
      * Untuk distribusi lain, silakan ikuti petunjuk [instalasi Docker di Linux](https://docs.docker.com/engine/install/).


2. **Verifikasi Instalasi Docker**:
      Setelah instalasi selesai, buka **Command Prompt** atau **PowerShell** dan jalankan perintah berikut untuk memastikan Docker terinstal dengan benar:

      ```bash
      docker --version
      ```

   Jika perintah ini mengembalikan versi Docker, berarti Docker sudah siap digunakan.

**Langkah 2: Menjalankan Dashboard Metabase dan Menyambungkan Database Kustom**

1. **Salin file `metabase.db.mv.db` ke lokal komputer**

2. **Jalankan Metabase dengan volume untuk file database**:

      Gunakan perintah berikut untuk menyambungkan file database **`metabase.db.mv.db`** ke dalam container Metabase:

      ```bash
      docker run -d --name metabase -v metabase_data:/metabase.db -p 3000:3000 metabase/metabase 
      ```
      Perintah ini digunakan untuk menjalankan aplikasi Metabase dalam Docker. Dengan perintah ini, sebuah container baru akan dibuat dengan metabase, menjalankan file data Metabase volume tersebut (**`metabase.db.mv.db`**), dan menghubungkan port container ke port di host supaya bisa diakses melalui browser. 


**Langkah 3: Akses Metabase**

   > Setelah container berjalan, dapat mengakses **Metabase** melalui URL berikut di browser:
      ```
      http://localhost:3000
      ```

**Informasi Login**

   Setelah akses Metabase, untuk login, gunakan informasi berikut:

   * **Email**: `labibaadinda11@gmail.com`
   * **Password**: `root123`

   Dengan informasi login ini, pengguna dapat mengakses Metabase dan melihat dashboard serta data dari file **`metabase.db.mv.db`**.


## Business Dashboard

Jaya Jaya Institution Dashboard dirancang untuk membantu institusi dalam melakukan analisis serta monitoring terhadap data mahasiswa yang berhubungan dengan resiko dropout.

Dashboard ini menampilkan:

**Dashboard 1 (Status vs Scholarship Holder)**
* Dashboard ini menunjukkan perbandingan antara mahasiswa yang tidak menerima beasiswa (73.3%) dan mahasiswa penerima beasiswa (26.7%) dari total 3,630 mahasiswa.

**Dashboard 2 (Jumlah Student berdasarkan Staatus)**
* Data juga menampilkan status mahasiswa secara keseluruhan: 49.9% lulus (Graduate), 32.1% putus sekolah (Dropout), dan 17.9% masih terdaftar (Enrolled) dari total 4,424 mahasiswa.

**Dashboard 3 (Feature Importance)**
* Dashboard ini menampilkan faktor-faktor yang paling penting atau berpengaruh (dengan koefisien Abs tertinggi) yang mungkin memengaruhi status mahasiswa (misalnya, kelulusan atau putus sekolah).
* Beberapa fitur yang disebutkan adalah: Approval\_rate, Course, Tuition\_fees\_up\_to\_date, Scholarship\_holder, Average\_grade, Debtor, Age\_at\_enrollment, Mothers\_occupation, Application\_mode, Total\_approved\_Curricular\_units, dan Marital\_status.

**Dashboard 4 (Jumlah Graduate dan Dropout Berdasarkan Previous Qualification)**
* Dashboard ini menyajikan jumlah mahasiswa yang lulus dan putus sekolah berdasarkan kualifikasi sebelumnya.
* Terlihat bahwa ada perbedaan dalam jumlah "total students" untuk setiap "Previous qualification" antara kelompok Dropout dan Graduate.

**Dashboard 5 (Mahasiswa dropout berdasarkan Gender)**
* Dashboard ini mengilustrasikan proporsi mahasiswa yang putus sekolah berdasarkan gender.
* Dari total 1,421 mahasiswa yang putus sekolah, 50.7% adalah perempuan dan 49.3% adalah laki-laki.

**Dashboard 6 (Pengangguran Berdasarkan Status Mahasiswa)**
* Dashboard ini menunjukkan status pengangguran berdasarkan status mahasiswa (Graduate, Enrolled, Dropout).
* Dari total 162 kasus, 50% adalah lulusan (Graduate), 30% masih terdaftar (Enrolled), dan 20% adalah putus sekolah (Dropout).

**Dashboard 7 (Jumlah Graduate dan Dropout Berdasarkan Marital Status)**
* Dashboard ini menyajikan data jumlah mahasiswa yang lulus dan putus sekolah berdasarkan status pernikahan.
* Grafik menunjukkan perbandingan "total students" untuk berbagai "Marital status" antara kelompok Dropout dan Graduate.

**Dashboard 8 (Dropout vs Graduate berdasarkan Rata-rata nilai)**
* Dashboard ini membandingkan rata-rata nilai (grade) antara mahasiswa yang putus sekolah dan mahasiswa yang lulus untuk semester 1 dan semester 2.
* Rata-rata nilai semester 1 untuk mahasiswa putus sekolah adalah 784.88, dan semester 2 adalah 619.69.
* Untuk mahasiswa yang lulus, rata-rata nilai semester 1 adalah 1,600.37, dan semester 2 adalah 1,609.1.

## Menjalankan Sistem Machine Learning

Prototype sistem machine learning saya dijalankan menggunakan Streamlit, sebuah framework Python untuk membangun antarmuka web interaktif. Untuk menjalankan sistem, pengguna cukup mengakses link berikut :

🌐 [Dashboard Prediksi Status Kelulusan atau Dropout Mahasiswa Menggunakan Model Pembelajaran Mesin ](https://dashboard-data-science-institution-labibaadinda.streamlit.app/)🌐

Di halaman tersebut, pengguna dapat menginput data mahasiswa sesuai dengan field yang teredia pada antar muka.
Setelah mengisi seluruh data dengan benar, anda dapat menekan tombol Predict untuk menampilkan hasil prediksi dari mahasiswa tersebut.
Dan sistem akan menampilkan hasil prediksi berupa status risiko (dropout atau graduate) serta probabilitas risikonya.
Sistem ini menggunakan model Random Forest yang telah dilatih sebelumnya dengan akurasi 91.5978%.
Selain itu anda juga dapat menjalankan proyek ini di komputer lokal anda dengan menjalankan perintah berikut.

```
streamlit run app.py
```

## Conclusion

Pada proyek ini telah dilakukan analisis data untuk menentukan faktor-faktor apa saja yang mempengaruhi angka Dropout mahasiswa pada Jaya Jaya Instition. Selain itu dilakukan pelatihan model yang mampu  melakukan prediksi apakah mahasiswa akan mengalami dropout(keluar) ataupun graduated(lulus) berdasarkan data akademik, demografis dan sosial, serta Ekonomi/Keaungan.

**1. Faktor-Faktor yang Mempengaruhi Dropout maupun Graduate**

- `Scholarship_holder`
  Mahasiswa penerima beasiswa cenderung memiliki komitmen akademik yang tinggi dan bantuan finansial, yang mengurangi tekanan ekonomi dan meningkatkan peluang kelulusan. Mahasiswa dengan beasiswa umumnya menunjukkan performa akademik yang baik dan memiliki dukungan ekonomi yang memadai.

- `Average_grade`

  Nilai rata-rata akademik merupakan indikator langsung dari kinerja belajar mahasiswa.
  Mahasiswa dengan nilai rata-rata tinggi memiliki kecenderungan lebih besar untuk lulus tepat waktu, sedangkan nilai rendah bisa menjadi sinyal risiko dropout.

- Dan beberapa fitur lain berdasarkan important feature yaitu  `Debtor`(penanggung utang), `Age_at_enrollment`(usia), `Mather_occupation`(pekerjaan ibu), `applicatioon model`(cara mendaftar perguruan tinggi), `Total_approve_curricular_units`(total unit semester yang disetujui)

**2. Pelatihan Model Prediksi**

  Model terbaik yang digunakan dalam proyek ini adalah Random Forest, dengan hasil evaluasi berikut:

* **Accuracy:** 0.915978
* **Precision:** 0.912766
* **Recall:** 0.955457
* **F1-Score:** 0.933624

Model Random Forest merupakan model terbaik dengan akurasi tertinggi dibandingkan dengan model lain seperti
Logistic Regression dan SVM. Model Random Forest memiliki performa model yang seimbang secara keseluruhan dimana akurasi, presisi, recall, dan f1-score cukup bagus.

### Rekomendasi Action Items

Berikut beberapa rekomendasi action items yang dapat dilakukan Institut guna menyelesaikan permasalahan atau mencapai target mereka untuk menurunkan angka dropout dan meningkatkan keberhasilan akademik mahasiswa.

1. Peningkatan Dukungan bagi Mahasiswa Penerima Beasiswa dan Non-Beasiswa:
   * Kembangkan program dukungan yang disesuaikan. Misalnya, mahasiswa non-beasiswa memiliki tingkat dropout yang lebih tinggi, mungkin diperlukan program bantuan finansial darurat atau skema pembayaran yang lebih fleksibel. Mahasiswa beasiswa juga memiliki angka dropout, perlu ditinjau syarat dan dukungan beasiswa.

2. Program Intervensi Dini untuk Mahasiswa dengan Kualifikasi Sebelumnya yang Rentan:
    * Action Item: Identifikasi "Previous qualification" yang memiliki tingkat dropout yang lebih tinggi.
    * Tujuan: Rancang program pembinaan, tutorial tambahan, atau bimbingan akademik khusus untuk mahasiswa yang masuk dengan kualifikasi tersebut, guna membantu mereka beradaptasi dan berhasil di lingkungan akademik Institut.

3. Program Dukungan Gender-Spesifik untuk Mengurangi Dropout:
    * Action Item: Meskipun proporsi dropout laki-laki dan perempuan hampir seimbang (50.7% perempuan, 49.3% laki-laki), Institut dapat menggali lebih dalam alasan di balik dropout untuk masing-masing gender.
    * Tujuan: Jika ditemukan faktor pendorong yang berbeda, kembangkan program dukungan yang disesuaikan (misalnya, program mentoring untuk laki-laki atau dukungan keseimbangan kehidupan-studi untuk perempuan).

4. Program Bimbingan Karir dan Pengembangan Diri untuk Mengatasi Pengangguran Lulusan:
    * Action Item: Mengingat 50% pengangguran berasal dari lulusan (Graduate), perkuat pusat karir Institut.
    * Tujuan: Sediakan pelatihan keterampilan yang relevan dengan pasar kerja, lokakarya persiapan wawancara, bimbingan karir individu, dan fasilitasi magang atau peluang kerja.

5. Intervensi Akademik untuk Mahasiswa dengan Rata-rata Nilai Rendah:
    * Action Item: Fokus pada mahasiswa yang memiliki rata-rata nilai semester 1 dan 2 yang lebih rendah, terutama mereka yang cenderung dropout.
    * Tujuan: Tawarkan program les privat, kelompok belajar, bimbingan akademik, atau sistem peringatan dini bagi mahasiswa yang menunjukkan penurunan kinerja akademik. Promosikan juga sumber daya akademik yang tersedia.

6. Penggunaan Model Machine Learning untuk Membantu melakukan Pemantauan serta Prediksi Dini
   * Hasil prediksi dapat menjadi landasan untuk mengambil tindakan solutif untuk permasalahan maraknya angka dropout. Selain itu Dapat juga dipertimbangkan untuk pembuatan dashboard bagi pihak institusi untuk memantau mahasiswa dengan resiko tinggi mengalami dropout.