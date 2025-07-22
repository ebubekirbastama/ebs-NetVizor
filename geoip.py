# geoip.py
import requests

def get_ip_location(ip):
    """
    IP adresinden şehir, ülke ve koordinat bilgisi döner.
    API: ipinfo.io (ücretsiz, kısıtlı)
    """
    try:
        resp = requests.get(f"https://ipinfo.io/{ip}/json", timeout=3)
        data = resp.json()
        city = data.get("city", "Bilinmiyor")
        country = data.get("country", "Bilinmiyor")
        loc = data.get("loc", "")  # "lat,lon"
        return city, country, loc
    except Exception:
        return "Bilinmiyor", "Bilinmiyor", ""
