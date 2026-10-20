# Praktikum 4: Aplikasi Quantum GIS (QGIS) 1

## Deskripsi
Modul keempat ini merupakan transisi dari pemetaan berbasis *web* (Google Maps) menuju pemetaan berbasis *desktop* menggunakan perangkat lunak **Quantum GIS (QGIS)**. Praktikum ini berfokus pada konfigurasi ruang kerja SIG profesional, integrasi *basemap* melalui *XYZ Tiles connection*, penggunaan ekstensi *plugin*, serta pemrosesan dan konversi format data spasial.

## Tujuan Praktikum
- Memahami antarmuka dan manajemen proyek pada aplikasi *desktop* QGIS.
- Mengonfigurasi referensi peta dasar (*basemap*) seperti *OpenStreetMap* dan Google Maps menggunakan koneksi *XYZ Tiles*.
- Menginstal dan memanfaatkan *Plugin Manager* (KML Tools) untuk mengekstraksi data.
- Mengimpor data luasan poligon berformat XML/KML hasil digitasi Google Maps dan mengonversinya menjadi format persistensi standar industri geospasial, yaitu **ESRI Shapefile (.shp)**.

## Isi Direktori
Folder ini mendokumentasikan *file project* QGIS dan himpunan *file* *Shapefile* (termasuk `.shp`, `.shx`, `.dbf`, dan `.prj`) dari hasil konversi data poligon:
- **Project QGIS:** `praktikum_sig1.qgz` dan `praktikum_gis2.qgz`.
- **Data Shapefile Wilayah:** 
  - Batas Administrasi Provinsi DKI Jakarta.
  - Batas Administrasi D.I. Yogyakarta (Tugas Mandiri).
  - Batas Administrasi Kota Depok (Tugas Mandiri).