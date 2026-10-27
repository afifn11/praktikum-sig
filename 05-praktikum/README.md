# Praktikum 5: Aplikasi Quantum GIS (QGIS) 2

## Deskripsi
Modul kelima ini difokuskan pada pengenalan dan pembuatan format data geospasial modern berbasis web, yaitu **GeoJSON**. Praktikum ini juga mengeksplorasi teknik integrasi perpaduan antara data spasial (titik koordinat dan luasan poligon) dengan data atribut non-spasial (tabel data relasional) menggunakan fitur *Attribute Table* di dalam Quantum GIS (QGIS).

## Tujuan Praktikum
- Memahami struktur sintaksis dan cara membuat berkas format GeoJSON secara visual menggunakan antarmuka pemetaan *web* (geojson.io).
- Mengintegrasikan himpunan data (*dataset*) GeoJSON secara langsung ke dalam kanvas proyek QGIS.
- Mampu memanajemen, memodifikasi, dan menambahkan kolom data atribut non-spasial (kualitatif dan kuantitatif seperti populasi, luas wilayah, dan nilai PDB/GDP) pada layer peta menggunakan *Attribute Table* QGIS.

## Isi Direktori
Folder ini mendokumentasikan *file project* QGIS, *file* GeoJSON mentah, dan himpunan *file* *Shapefile* hasil konversi yang telah diinjeksi dengan data atribut kependudukan dan ekonomi:
- **Project QGIS:** `praktikum_qgis2.qgz` dan `praktikum_qgis4.qgz` (Tugas Mandiri).
- **Data Titik (Point) Jabodetabek:** 
  - `jabotabek.geojson` dan konversi `jabotabek.shp` (beserta file pendukungnya).
  - Berisi data atribut: Nama Kota, Luas, Populasi (2024), dan GDP.
- **Data Area (Polygon) Provinsi Pulau Jawa (Praktikum Mandiri):**
  - Dataset 6 Provinsi di Pulau Jawa (Banten, DKI Jakarta, Jawa Barat, Jawa Tengah, D.I. Yogyakarta, Jawa Timur) dalam format `.geojson` dan `.shp`.
  - Berisi data atribut tambahan: Tahun, Populasi, dan Luas Wilayah.