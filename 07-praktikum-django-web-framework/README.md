# Praktikum 7: WebGIS dengan Python Web Django Framework

## Deskripsi
Modul ketujuh ini mempraktikkan pembangunan aplikasi **WebGIS Fullstack** berbasis *open-source* menggunakan *web framework* **Python Django**. Praktikum ini mengintegrasikan arsitektur MVT (*Model-View-Template*) Django dengan pustaka pemetaan interaktif **Leaflet.js** dan peta dasar **OpenStreetMap** serta **Esri Satellite**, hingga pemrosesan data geospasial *real-time* berbasis API JSON dari **BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)**.

## Tujuan Praktikum
- Menguasai *environment setup* Python (`venv`), instalasi Django Framework, serta inisialisasi struktur *Project* (`webumkm`) dan *App* (`petaindonesia`, `gempabumi`).
- Mampu mengkonfigurasi alur kerja arsitektur **MVT (Model-View-Template)** Django, mulai dari penanganan *routing* HTTP pada `urls.py`, logika respons pada `views.py` / `view_peta.py`, hingga pemetaan tampilan pada *Template* HTML.
- Memvisualisasikan peta GIS interaktif menggunakan **Leaflet.js**, mengimplementasikan penanda (*marker*), *basemap layer control*, skala peta, serta *sidebar filter* berbasis wilayah (Jabodetabek).
- Mengintegrasikan data geospasial eksternal berbasis API JSON *real-time* (Data Gempa Terkini M 5.0+ BMKG) dan mengklasifikasikan visualisasi *circleMarker* berdasarkan skala kedalaman gempa.

## Isi Direktori
Folder ini mendokumentasikan seluruh *environment*, konfigurasi *project* utama Django, serta modul-modul aplikasi WebGIS yang dikembangkan:
- **Virtual Environment:** `webgis/` (Lingkungan kerja khusus Python 3.11+ dan Django 5.2).
- **Django Main Project (`webumkm/`):**
  - Config & Settings (`settings.py`, `urls.py`, `asgi.py`, `wsgi.py`).
  - Basis Data Bawaan (`db.sqlite3`) dan Skrip Pengelola (`manage.py`).
- **Modul App 1: Peta Indonesia & Jabodetabek (`petaindonesia/`):**
  - **Views:** Logika tampilan `welcome`, `petasatu` (Peta Nasional), dan `petadua` (Peta Interaktif Jabodetabek).
  - **Templates (`petaindonesia/templates/petaindonesia/`):** 
    - `petasatu.html`: Visualisasi peta Indonesia berpusat pada koordinat `-2.5489, 118.0149` dengan fitur *Layer Control* (OpenStreetMap & Esri Satellite) dan *Scale Control*.
    - `petadua.html`: Peta interaktif wilayah Jabodetabek (Jakarta, Bogor, Depok, Tangerang, Bekasi) dilengkapi *sidebar* tombol *filter* per kota.
- **Modul App 2: Peta Gempa Terkini BMKG (`gempabumi/`):**
  - **Views & Parser (`views.py`):** Integrasi *Live Data Fetching* dari Endpoint JSON BMKG (`gempaterkini.json`) serta logika pemilah kedalaman gempa (Dangkal `<70 km`, Menengah `70-300 km`, Dalam `>300 km`).
  - **Templates (`gempabumi/templates/gempabumi/index.html`):** Visualisasi peta tematik gempa interaktif dengan *circleMarker* berkode warna kedalaman beserta *side panel* rincian magnitudo, lokasi, waktu, dan potensi tsunami.