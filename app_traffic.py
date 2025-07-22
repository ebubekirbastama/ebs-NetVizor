# app_traffic.py
import psutil

def get_active_connections():
    """
    Aktif TCP ve UDP bağlantılarını ve ilgili uygulama bilgilerini döner.
    Return: list of dict
    """
    conns = psutil.net_connections()
    result = []
    for c in conns:
        # LISTEN durumundakileri atla, ve uzak adresi olmayanları da
        if c.status != psutil.CONN_LISTEN and c.raddr:
            try:
                proc = psutil.Process(c.pid)
                pname = proc.name()
            except Exception:
                pname = "Bilinmiyor"
            result.append({
                "pid": c.pid,
                "process_name": pname,
                "laddr": f"{c.laddr.ip}:{c.laddr.port}",
                "raddr": f"{c.raddr.ip}:{c.raddr.port}",
                "status": c.status
            })
    return result
