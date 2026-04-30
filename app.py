from flask import Flask, redirect, render_template, send_file, request, jsonify
from Funciones import Qr_Generator
from Funciones import Show_File as Show_File
from Funciones.paths import ensure_runtime_dirs, qr_path, static_dir, templates_dir
import os
import webbrowser
import socket as sok
from werkzeug.utils import secure_filename
import secrets
import subprocess
import platform


# Crear carpetas persistentes para archivos subidos y QR
Files_Carpet, QR_Carpet = ensure_runtime_dirs()
ALLOWED_EXTENSIONS = {
    'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3', 'wav', 'aac',
    'avi', 'mov', 'zip', 'rar', 'py', 'js', 'html', 'css', 'java', 'm4a', 'opus'
}
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB


# Crear Flask con rutas absolutas a recursos empaquetados
app = Flask(__name__, template_folder=templates_dir(), static_folder=static_dir())
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Función para verificar si el archivo tiene una extensión permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    File = Show_File.Show_File()
    return render_template('index.html', File=File)


@app.route('/file/<path:File>', methods=['GET'])
def uploaded_file(File=''):
    File = secure_filename(File)
    Url_File = os.path.join(Files_Carpet, File)
    Url_File = os.path.abspath(Url_File)
    Files_Carpet_Abs = os.path.abspath(Files_Carpet)

    if not Url_File.startswith(Files_Carpet_Abs):
        return "Acceso denegado", 403

    if not os.path.exists(Url_File):
        return "Archivo no encontrado", 404

    if not os.path.isfile(Url_File):
        return "No es un archivo válido", 400

    return send_file(Url_File)


@app.route('/descarga/<string:File>', methods=['GET'])
def Descarga(File=''):
    if request.method == 'GET':
        try:
            File = secure_filename(File)
            Url_File = os.path.join(Files_Carpet, File)

            Url_File = os.path.abspath(Url_File)
            Files_Carpet_Abs = os.path.abspath(Files_Carpet)

            if not Url_File.startswith(Files_Carpet_Abs):
                return "Acceso denegado", 403

            if not os.path.exists(Url_File):
                return "Archivo no encontrado", 404

            if not os.path.isfile(Url_File):
                return "No es un archivo válido", 400

            return send_file(Url_File, as_attachment=True, download_name=File)

        except Exception as e:
            print(f"Error al descargar archivo: {e}")
            return "Error al procesar la descarga", 500
    else:
        return redirect('/')


@app.route('/eliminar/<path:File>', methods=['POST'])
def eliminar_file(File=''):
    try:
        File = secure_filename(File)
        Url_File = os.path.join(Files_Carpet, File)

        Url_File = os.path.abspath(Url_File)
        Files_Carpet_Abs = os.path.abspath(Files_Carpet)

        if not Url_File.startswith(Files_Carpet_Abs):
            return jsonify({'success': False, 'message': 'Acceso denegado'}), 403

        if not os.path.exists(Url_File):
            return jsonify({'success': False, 'message': 'Archivo no encontrado'}), 404

        if not os.path.isfile(Url_File):
            return jsonify({'success': False, 'message': 'No es un archivo válido'}), 400

        os.remove(Url_File)
        return jsonify({'success': True, 'message': 'Archivo eliminado correctamente'}), 200

    except Exception as e:
        print(f"Error al eliminar archivo: {e}")
        return jsonify({'success': False, 'message': 'Error al eliminar el archivo'}), 500


@app.route('/unblock/<string:File>', methods=['POST'])
def unblock_file(File=''):
    """Desbloquea un archivo en Windows usando Unblock-File."""
    try:
        File = secure_filename(File)
        Url_File = os.path.join(Files_Carpet, File)

        Url_File = os.path.abspath(Url_File)
        Files_Carpet_Abs = os.path.abspath(Files_Carpet)

        if not Url_File.startswith(Files_Carpet_Abs):
            return jsonify({'success': False, 'message': 'Acceso denegado'}), 403

        if not os.path.exists(Url_File):
            return jsonify({'success': False, 'message': 'Archivo no encontrado'}), 404

        if platform.system() == 'Windows':
            try:
                command = f'Unblock-File -Path "{Url_File}"'
                subprocess.run(
                    ['powershell', '-NoProfile', '-Command', command],
                    check=True,
                    capture_output=True,
                    timeout=10
                )
                print(f"Archivo desbloqueado: {Url_File}")
                return jsonify({'success': True, 'message': 'Archivo desbloqueado correctamente'}), 200
            except subprocess.TimeoutExpired:
                return jsonify({'success': False, 'message': 'Timeout al desbloquear'}), 500
            except subprocess.CalledProcessError as e:
                print(f"Error desbloqueo: {e.stderr.decode() if e.stderr else str(e)}")
                return jsonify({'success': False, 'message': 'No se pudo desbloquear el archivo'}), 500
        else:
            return jsonify({'success': False, 'message': 'Esta función solo funciona en Windows'}), 400

    except Exception as e:
        print(f"Error en desbloqueo: {e}")
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@app.route('/update')
def UpDate():
    return render_template('Up_Data.html')


@app.route('/qrgenerator')
def QR_Generador():
    return render_template('Qr_Generator.html')


@app.route('/qr-image')
def qr_image():
    if not os.path.exists(qr_path()):
        Qr_Generator.Generar_QR()
    return send_file(qr_path())


@app.route('/qr')
def qr():
    Qr_Generator.Generar_QR()
    return redirect('/qrgenerator')


@app.route('/upload', methods=['POST'])
def update():
    if request.method == 'POST':
        if 'UPFile' not in request.files:
            return redirect('/update')

        f = request.files.get('UPFile')

        if not f or f.filename == '':
            return redirect('/update')

        filename = secure_filename(f.filename)

        # 1. Validar si la extensión está permitida
        if allowed_file(filename):
            # 2. Definir la ruta completa usando la carpeta de archivos
            file_path = os.path.join(Files_Carpet, filename)
            
            # 3. Guardar el archivo físicamente
            f.save(file_path)
            
            # Redirigir al inicio para ver el archivo cargado
            return redirect('/')
        else:
            # Si el archivo NO es permitido, redirigir de vuelta con error
            print(f"Extensión no permitida: {filename}")
            return redirect('/update')

    return redirect('/update')

def abrir_navegador():
    hostname = sok.gethostname()
    try:
        ip = sok.gethostbyname(hostname)
    except Exception:
        ip = "127.0.0.1"

    urls = "http://" + ip + ":5000/"
    webbrowser.open(urls)


if __name__ == '__main__':
    Qr_Generator.Generar_QR()
    abrir_navegador()
    app.run( debug=True, host="0.0.0.0", port=5000)
