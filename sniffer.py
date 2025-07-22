# sniffer.py
import pydivert

def protocol_name(proto_val):
    protocol_map = {
        1: "ICMP",
        6: "TCP",
        17: "UDP"
    }
    return protocol_map.get(proto_val, f"Diğer ({proto_val})")

def start_sniffing(callback):
    """
    Tüm ağ paketlerini dinler, filtre uygulanmadan callback fonksiyonuna gönderir.
    callback: (dict) -> None, paket bilgilerini alır.
    """
    try:
        with pydivert.WinDivert("true") as w:
            for packet in w:
                try:
                    info = {
                        "src_ip": packet.src_addr,
                        "dst_ip": packet.dst_addr,
                        "src_port": packet.src_port,
                        "dst_port": packet.dst_port,
                        "protocol": protocol_name(packet.protocol),
                        "direction": "inbound" if packet.is_inbound else "outbound",
                        "length": len(packet.raw) if packet.raw else 0
                    }
                    callback(info)
                except Exception as inner_err:
                    print(f"[⚠️ Paket işlenirken hata]: {inner_err}")
    except Exception as err:
        print(f"[❌ Sniffer başlatılamadı]: {err}")
