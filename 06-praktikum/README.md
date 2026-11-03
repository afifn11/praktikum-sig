# Praktikum 6: Aplikasi Quantum GIS (QGIS) 3

## Deskripsi
Modul keenam ini mempraktikkan proses perancangan dan visualisasi **Peta Tematik (Choropleth)**. Praktikum ini mengedepankan integrasi antara manipulasi keruangan spasial dan komputasi matematis basis data atribut, yang pada akhirnya diekspresikan melalui klasifikasi simbologi warna untuk menemukan pola keruangan ( *spatial pattern*) dari suatu fenomena kewilayahan.

## Tujuan Praktikum
- Menguasai fungsionalitas *Geoprocessing* tingkat dasar, khususnya **Merge Vector Layers**, untuk menggabungkan beberapa entitas batas wilayah administratif yang terpisah menjadi satu kesatuan lapisan spasial utuh.
- Mampu menggunakan **Field Calculator** untuk mengkomputasi dan menghasilkan kolom turunan matematis baru (seperti indeks kepadatan penduduk) secara otomatis di dalam *Attribute Table*.
- Memvisualisasikan data kuantitatif ke dalam peta tematik menggunakan metode klasifikasi **Categorized Symbology** berserta penyesuaian rentang warna ( *Color Ramp*).

## Isi Direktori
Folder ini mendokumentasikan *file project* QGIS, dataset wilayah dasar, dan himpunan *file Shapefile* luaran (*output*) integrasi peta tematik:
- **Project QGIS:** `peta_tematik_jakarta.qgz` dan `praktikum_qgis5.qgz` (Tugas Mandiri).
- **Peta Tematik Kepadatan Penduduk DKI Jakarta 2024:** 
  - Himpunan data gabungan `dki_jakarta.shp` (beserta file `.shx`, `.dbf`, `.prj`, dll).
  - Meliputi kalkulasi luasan daratan dan rasio kepadatan per jiwa.
- **Peta Tematik Pulau Jawa (Praktikum Mandiri):**
  - Dataset *Shapefile* Peta Tematik Kepadatan Penduduk Provinsi se-Pulau Jawa.
  - Dataset *Shapefile* Peta Tematik Persebaran Fasilitas Pelayanan Kesehatan (RSU, RS Khusus, Puskesmas) Tahun 2025 bersumber dari data BPS.