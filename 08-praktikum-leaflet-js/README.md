# Praktikum 8: Visualisasi Peta Interaktif Berbasis Web dengan Leaflet.js & Integrasi Data GeoJSON

## Deskripsi
Praktikum ini berfokus pada pembangunan aplikasi **WebGIS** berbasis **Django** dan **Leaflet.js** untuk memvisualisasikan data spasial interaktif di web. Aplikasi mencakup penggunaan berbagai *tile provider* (OpenStreetMap & Esri), overlay vektor dasar (Marker, Circle, Polygon), pemuatan data spasial JSON 34 Provinsi Indonesia dengan pencarian interaktif, serta peta tematik **Choropleth** Pulau Jawa yang menggabungkan batas wilayah GeoJSON (`31.geojson`–`36.geojson`) dengan statistik pertanian dan demografi (`profil_petani_jawa.json`).

---

## Tujuan Pembelajaran
1. Mengonfigurasi proyek Django dengan layanan file statis (`STATICFILES_DIRS`) untuk menyajikan dataset JSON/GeoJSON.
2. Mengimplementasikan peta interaktif **Leaflet.js** dengan berbagai *basemap* (OpenStreetMap, Esri WorldStreetMap, Esri WorldTopoMap) serta kontrol layer.
3. Menambahkan elemen vektor (Marker kustom, Circle, Polygon) beserta *popup* bergaya CSS kustom.
4. Mengintegrasikan data spasial `provinces.json` secara dinamis menggunakan `fetch()` dan membangun sidebar pencarian interaktif (`flyTo`).
5. Membangun peta tematik **Choropleth** dengan menggabungkan file GeoJSON multi-provinsi dan data statistik, lengkap dengan filter metrik dinamis, panel info *hover*, dan legenda otomatis.

---

## Struktur Direktori
```text
08-praktikum-leaflet-js/
├── .gitignore
├── README.md
├── webgis/                                  # Virtual environment Python
└── webumkm/                                 # Direktori proyek Django
    ├── manage.py
    ├── db.sqlite3
    ├── webumkm/
    │   ├── settings.py                      # Konfigurasi app & static files
    │   └── urls.py                          # Routing utama proyek
    ├── petaindonesia/
    │   ├── view_peta.py                     # View untuk ketiga modul peta
    │   ├── urls.py                          # Routing aplikasi petaindonesia
    │   └── templates/
    │       └── petaindonesia/
    │           ├── peta_dasar.html          # Modul 1: Peta dasar & overlay
    │           ├── peta_provinsi.html       # Modul 2: 34 Provinsi & pencarian
    │           └── petani_jawa.html         # Modul 3: Choropleth Pulau Jawa
    └── static/
        └── json/
            ├── provinces.json               # Koordinat 34 provinsi Indonesia
            ├── profil_petani_jawa.json      # Data statistik pertanian Pulau Jawa
            └── 31.geojson - 36.geojson      # Batas wilayah provinsi di Pulau Jawa
```

---

## Rute Endpoint (URL Routes)

| Endpoint | View Function | Template | Deskripsi |
| :--- | :--- | :--- | :--- |
| `/` | `RedirectView` | — | Redirect otomatis ke `/dasar/` |
| `/dasar/` | `view_peta.peta_dasar` | `peta_dasar.html` | Peta dasar Leaflet dengan basemap OSM/Esri, Marker, Circle, Polygon, & CSS Popup |
| `/provinsi/` | `view_peta.peta_provinsi` | `peta_provinsi.html` | Peta 34 provinsi Indonesia dari `provinces.json` dengan sidebar pencarian & `flyTo` |
| `/petani_jawa/` | `view_peta.petani_jawa` | `petani_jawa.html` | Peta Choropleth Pulau Jawa (Kepadatan Penduduk & Jumlah Petani) dengan legenda & hover info |

---

## Cara Menjalankan Proyek
1. Aktifkan virtual environment:
   ```powershell
   .\webgis\Scripts\Activate.ps1
   ```
2. Masuk ke direktori proyek Django dan jalankan server pengembangan:
   ```powershell
   cd webumkm
   python manage.py runserver
   ```
3. Buka browser dan akses:
   - `http://127.0.0.1:8000/dasar/`
   - `http://127.0.0.1:8000/provinsi/`
   - `http://127.0.0.1:8000/petani_jawa/`
