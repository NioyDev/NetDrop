import qrcode as qr
import socket as sok
from PIL import Image
from Funciones.paths import ensure_runtime_dirs, logo_path, qr_path


def Generar_QR():
    ensure_runtime_dirs()
    logo_file = logo_path()
    qr_output_path = qr_path()

    hostname = sok.gethostname()
    ip = sok.gethostbyname(hostname)
    urls = "http://" + ip + ":5000/"

    new_qr = qr.QRCode(version=1, box_size=100, border=0)
    new_qr.add_data(urls)
    new_qr.make(fit=True)

    img = new_qr.make_image(fill='black', back_color='white')

    try:
        logo = Image.open(logo_file)
        imgW, imgH = img.size
        logo_size = imgW // 4
        logo = logo.resize((logo_size, logo_size))
        logo_x = (imgW - logo_size) // 2
        logo_y = (imgH - logo_size) // 2
        img.paste(logo, (logo_x, logo_y), logo)
    except Exception as e:
        print(f"Advertencia: No se pudo insertar el logo: {e}")

    img.save(qr_output_path)
