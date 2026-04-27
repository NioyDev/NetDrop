import os
from Funciones.paths import upload_dir
from datetime import datetime


def Show_File():
    Ruta = upload_dir()
    archivos = []

    if os.path.exists(Ruta):
        lista_archivos = sorted(os.listdir(Ruta))

        for nombre_archivo in lista_archivos:
            ruta_completa = os.path.join(Ruta, nombre_archivo)

            if os.path.isfile(ruta_completa):

                # 1. Obtenemos el timestamp en segundos
                timestamp = os.path.getmtime(ruta_completa)
    
                # 2. Lo convertimos a una fecha legible (Día/Mes/Año)
                fecha_legible = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y')

                archivos.append({
                    "nombre": nombre_archivo,
                    "ruta": f"/file/{nombre_archivo}",
                    "tipo": nombre_archivo.split(".")[-1].lower() if '.' in nombre_archivo else '',
                    "fecha": fecha_legible
                })
    return archivos
