# Ejecutable para Linux
pyinstaller --onefile --windowed --noconfirm --exclude-module PySide6 --exclude-module tkinter --add-data "templates:templates" --add-data "static:static" --icon=static/Logo/icono.png --name NetDrop app.py

# Ejecutable para Windows
pyinstaller --onefile --windowed --noconfirm --exclude-module PySide6 --exclude-module tkinter --add-data "templates;templates" --add-data "static;static" --icon=static/Logo/Logo.ico --name NetDrop app.py

# El Setup de Windows se crea con Inno Setup Compiler, usando el archivo setup.iss
& "C:\Users\migue\AppData\Local\Programs\Inno Setup 6\ISCC.exe" distribucion\NetDrop-Setup.iss