import os
from Funciones.paths import upload_dir


def Show_File():
    Ruta = upload_dir()
    archivos = []

    if os.path.exists(Ruta):
        lista_archivos = sorted(os.listdir(Ruta))

        for nombre_archivo in lista_archivos:
            ruta_completa = os.path.join(Ruta, nombre_archivo)

            if os.path.isfile(ruta_completa):
                archivos.append({
                    "nombre": nombre_archivo,
                    "ruta": f"/file/{nombre_archivo}",
                    "tipo": nombre_archivo.split(".")[-1].lower() if '.' in nombre_archivo else '',
                    "fecha": os.path.getmtime(ruta_completa)
                })

    return archivos
