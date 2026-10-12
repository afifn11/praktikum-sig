# Praktikum 2: Aplikasi Google Map 2

## Deskripsi
Modul kedua membahas tentang manajemen data spasial tingkat lanjut menggunakan sistem klasifikasi **Layer**. Praktikum ini mencakup proses pengolahan data mentah provinsi berformat JSON, konversi silang menuju format CSV, serta segmentasi data wilayah (provinsi dan kabupaten/kota) agar informasi spasial tersusun dengan rapi tanpa penumpukan visual (*cluttering*).

## Tujuan Praktikum
- Mampu mendemonstrasikan pengorganisasian tata letak data menggunakan fitur *Layer* secara independen di Google My Maps.
- Mampu melakukan partisi *tagging* data spasial berskala nasional (berdasarkan gugus pulau) dan berskala regional (berdasarkan batas kabupaten/kota).
- Melakukan proses koreksi galat koordinat GPS (*debugging*) secara manual di atas kanvas peta.

## Isi Direktori
Folder ini berisi dataset keruangan (`.csv`) yang telah dipisahkan ke dalam beberapa *file* terpisah untuk memfasilitasi pembuatan *layer*, meliputi:
- **Data Provinsi di Indonesia:** `sumatera.csv`, `jawa-bali.csv`, `kalimantan.csv`, `sulawesi.csv`, dan `indonesia_timur.csv`.
- **Data Kabupaten/Kota:** Klasifikasi wilayah Kabupaten/Kota administrasi secara khusus di seluruh Pulau Jawa (Praktikum Mandiri).