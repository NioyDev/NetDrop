# NetDrop

NetDrop es una aplicacion web local para compartir archivos dentro de una misma red. Permite iniciar un pequeno servidor desde tu computadora para subir, visualizar, descargar y eliminar archivos desde otros dispositivos conectados a la red, como Android, iPhone, tablets o cualquier navegador moderno.

Tambien incluye un generador de QR para facilitar el acceso rapido a la interfaz desde el movil.

## Caracteristicas

- Servidor local con interfaz web.
- Subida y descarga de archivos.
- Eliminacion de archivos desde la interfaz.
- Generacion de codigo QR para abrir la web mas rapido.
- Compatible con varios tipos de archivo.
- Se abre automaticamente en el navegador al iniciar.

## Requisitos

### Software

- Python 3.11 o superior.
- `pip` para instalar dependencias.

### Librerias incluidas en `requirements.txt`

- `Flask==3.1.0`
- `Werkzeug==3.1.3`
- `qrcode==8.0`
- `Flask-SocketIO==5.5.1`

## Instalacion

Clona el repositorio:

```bash
git clone https://github.com/NioyJadelkaFp/NetDrop.git
```

Entra en la carpeta del proyecto:

```bash
cd NetDrop
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicacion

### En Windows

```bash
python app.py
```

### En Linux o macOS

```bash
python3 app.py
```

Cuando el servidor arranque, NetDrop abrira automaticamente el navegador y escuchara en:

```bash
http://0.0.0.0:5000
```

Si quieres acceder desde otro dispositivo de la misma red, usa la IP local de la computadora que ejecuta el servidor.

## Uso

1. Ejecuta la aplicacion.
2. Abre la interfaz web desde tu navegador.
3. Sube los archivos que quieras compartir.
4. Accede desde otro dispositivo usando la misma red Wi-Fi o cableada.
5. Descarga, visualiza o elimina los archivos desde la interfaz.

## Nota de seguridad

- NetDrop esta pensado para uso en red local.
- Si el acceso desde otro dispositivo no funciona, revisa el firewall de tu sistema y permite el puerto `5000`.
- La funcion de desbloqueo de archivos solo funciona en Windows.

## Licencia y uso

Este proyecto no se publica como open source en el sentido estricto de la OSI. Se distribuye como software source-available bajo la licencia **PolyForm Noncommercial 1.0.0**.

Esto significa que puedes usar, estudiar y modificar el codigo para fines no comerciales, pero no esta permitido redistribuirlo o explotarlo con fines monetarios sin permiso expreso de los autores.

El software se proporciona "tal como esta", sin garantia de ningun tipo.

Consulta el archivo [`LICENSE`](./LICENSE) para leer el texto completo de la licencia.

## Autores

- [Nioy](https://github.com/NioyJadelkaFp/)
- [Ezxquiel](https://github.com/Ezxquiel)

## Tecnologias

- **Frontend:** HTML, CSS, JavaScript, Jinja2
- **Backend:** Python, Flask
