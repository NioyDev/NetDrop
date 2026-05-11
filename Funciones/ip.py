import socket as sok

def sacar_ip():
    """Obtiene la IP real de la máquina en la red local (ej. 192.168.x.x)"""
    try:
        # Creamos un socket temporal UDP
        s = sok.socket(sok.AF_INET, sok.SOCK_DGRAM)
        # Intentamos "conectar" a una IP externa (Google DNS). 
        # Como es UDP, no envía datos ni necesita internet real, solo obliga al OS a decirnos nuestra IP.
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        # Fallback seguro por si la PC no está conectada a ninguna red
        ip = "127.0.0.1" 
    return ip