import os
import urllib.request
from Funciones.ip import sacar_ip

def esta_cerrado():
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        return True
    try:
        urllib.request.urlopen(f"http://{sacar_ip()}:5000/", timeout=1)
        return False 
    except Exception: 
        return True 