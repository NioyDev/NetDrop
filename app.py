from flask import Flask, redirect, render_template, send_file, request, jsonify
from Funciones import Qr_Generator
from Funciones import Show_File as Show_File
from flask_socketio import SocketIO, send
import os
import webbrowser
import socket as sok
from werkzeug.utils import secure_filename
import secrets
import subprocess
import platform

Files_Carpet = './static/File/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3', 'wav', 'aac', 'avi', 'mov', 'zip', 'rar', 'py', 'js', 'html', 'css', 'java', 'm4a', 'opus'}
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
socketio = SocketIO(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

Qr_Generator.Generar_QR()

@app.route('/')
def index():
    File = Show_File.Show_File()
    return render_template('index.html', File=File)

@app.route('/descarga/<string:File>', methods=['GET'])
def Descarga(File=''):
    if request.method == 'GET':
        try:
            # Sanitizar nombre de archivo
            File = secure_filename(File)
            
            Base_Ruta = os.path.dirname(__file__)
            Url_File = os.path.join(Base_Ruta, 'static/File', File)
            
            # Verificar que la ruta está dentro del directorio permitido (prevenir path traversal)
            Url_File = os.path.abspath(Url_File)
            Files_Carpet_Abs = os.path.abspath(Files_Carpet)
            
            if not Url_File.startswith(Files_Carpet_Abs):
                return "Acceso denegado", 403
            
            # Verificaciones de seguridad
            if not os.path.exists(Url_File):
                return "Archivo no encontrado", 404
            
            if not os.path.isfile(Url_File):
                return "No es un archivo válido", 400
            
            # Enviar archivo para descarga
            return send_file(Url_File, as_attachment=True, download_name=File)
        
        except Exception as e:
            # Loguear error
            print(f"Error al descargar archivo: {e}")
            return "Error al procesar la descarga", 500
    else:
        # Si no es GET, redirigir de vuelta a la página principal
        return redirect('/')


@app.route('/unblock/<string:File>', methods=['POST'])
def unblock_file(File=''):
    """Desbloquea un archivo en Windows usando Unblock-File"""
    try:
        # Sanitizar nombre de archivo
        File = secure_filename(File)
        
        Base_Ruta = os.path.dirname(__file__)
        Url_File = os.path.join(Base_Ruta, 'static/File', File)
        
        # Verificar que la ruta está dentro del directorio permitido
        Url_File = os.path.abspath(Url_File)
        Files_Carpet_Abs = os.path.abspath(Files_Carpet)
        
        if not Url_File.startswith(Files_Carpet_Abs):
            return jsonify({'success': False, 'message': 'Acceso denegado'}), 403
        
        # Verificar que el archivo existe
        if not os.path.exists(Url_File):
            return jsonify({'success': False, 'message': 'Archivo no encontrado'}), 404
        
        # Si es Windows, intentar desbloquear
        if platform.system() == 'Windows':
            try:
                # Ejecutar comando PowerShell para desbloquear
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

@app.route('/qr')
def qr():
    Qr_Generator.Generar_QR()
    return redirect('/qrgenerator')

@app.route('/upload', methods=['POST'])
def update():
    if request.method == 'POST':
        # Validar que existe el archivo
        if 'UPFile' not in request.files:
            return redirect('/update')
        
        f = request.files.get('UPFile')
        
        # Validar que el archivo no está vacío
        if not f or f.filename == '':
            return redirect('/update')
        
        # Sanitizar nombre de archivo
        filename = secure_filename(f.filename)
        
        # Validar extensión de archivo
        if not allowed_file(filename):
            return redirect('/update')
        
        try:
            # Crear directorio si no existe
            os.makedirs(Files_Carpet, exist_ok=True)
            f.save(os.path.join(Files_Carpet, filename))
        except Exception as e:
            print(f"Error al guardar archivo: {e}")
            return redirect('/update')
    
    return redirect('/update')

def abrir_navegador():
    # Obtenemos la dirección IP de la máquina
    hostname = sok.gethostname()
    Ip = sok.gethostbyname(hostname)

    Urls = "http://" + Ip + ":5000/"
    webbrowser.open(Urls)

if __name__ == '__main__':
    Qr_Generator.Generar_QR()
    abrir_navegador()
    socketio.run(app, debug=False, host="0.0.0.0", port=5000)