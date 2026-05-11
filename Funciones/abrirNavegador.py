from Funciones.ip import sacar_ip
import webbrowser

def abrir_navegador():
    ip = sacar_ip()
    urls = f"http://{ip}:5000/"
    webbrowser.open(urls)
