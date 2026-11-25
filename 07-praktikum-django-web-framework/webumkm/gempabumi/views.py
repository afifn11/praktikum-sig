import json
import urllib.error
import urllib.request
from django.shortcuts import render


BMKG_API_URL = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"


def _classify_depth(depth_str):
    """Parse depth string like '10 km' and return numeric depth, color, and label."""
    try:
        numeric = float(depth_str.lower().replace("km", "").strip())
    except (ValueError, AttributeError):
        return 0.0, "gray", "Tidak diketahui"

    if numeric < 70:
        return numeric, "red", "Dangkal (< 70 km)"
    if numeric <= 300:
        return numeric, "orange", "Menengah (70-300 km)"
    return numeric, "green", "Dalam (> 300 km)"


def _parse_coordinates(coord_str):
    """Parse BMKG 'lat,lng' coordinate string into (lat, lng) floats."""
    try:
        parts = [p.strip() for p in coord_str.split(",")]
        return float(parts[0]), float(parts[1])
    except (ValueError, AttributeError, IndexError):
        return None, None


def index(request):
    earthquakes = []
    error_message = None

    req = urllib.request.Request(
        BMKG_API_URL,
        headers={"User-Agent": "Django-WebGIS-Praktikum/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            raw_list = payload.get("Infogempa", {}).get("gempa", [])[:15]

            for idx, item in enumerate(raw_list):
                lat, lng = _parse_coordinates(item.get("Coordinates", ""))
                if lat is None or lng is None:
                    continue
                depth_km, color, depth_category = _classify_depth(item.get("Kedalaman", ""))
                earthquakes.append({
                    "id": idx,
                    "tanggal": item.get("Tanggal", "-"),
                    "jam": item.get("Jam", "-"),
                    "magnitude": item.get("Magnitude", "-"),
                    "kedalaman": item.get("Kedalaman", "-"),
                    "depth_km": depth_km,
                    "color": color,
                    "depth_category": depth_category,
                    "wilayah": item.get("Wilayah", "-"),
                    "potensi": item.get("Potensi", "-"),
                    "lat": lat,
                    "lng": lng,
                })
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
        error_message = f"Gagal mengambil data dari BMKG: {exc}"

    context = {
        "earthquakes": earthquakes,
        "earthquakes_json": json.dumps(earthquakes),
        "error_message": error_message,
    }
    return render(request, "gempabumi/index.html", context)
