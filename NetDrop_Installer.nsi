; NetDrop Installer Script
; Este script crea un instalador profesional para NetDrop

!include "MUI2.nsh"
!include "x64.nsh"

; Configuración General
Name "NetDrop"
OutFile "dist\NetDrop_Installer.exe"
InstallDir "$PROGRAMFILES\NetDrop"
InstallDirRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop" "InstallLocation"

; Icono del instalador
!define MUI_ICON "static\Logo\Logo.ico"
!define MUI_UNICON "static\Logo\Logo.ico"

; Páginas del asistente
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; Idioma
!insertmacro MUI_LANGUAGE "Spanish"

; Información
VIProductVersion "1.0.0.0"
VIAddVersionKey "ProductName" "NetDrop"
VIAddVersionKey "CompanyName" "NetDrop"
VIAddVersionKey "FileDescription" "Sistema de Compartición de Archivos"
VIAddVersionKey "FileVersion" "1.0"

; Sección de instalación
Section "Instalar NetDrop"
  SetOutPath "$INSTDIR"
  
  ; Mostrar estado
  DetailPrint "Copiando archivos..."
  
  ; Copiar el exe
  File "dist\NetDrop.exe"
  
  ; Copiar carpetas
  DetailPrint "Copiando templates..."
  SetOutPath "$INSTDIR\templates"
  File /r "templates\*.*"
  
  DetailPrint "Copiando archivos estáticos..."
  SetOutPath "$INSTDIR\static"
  File /r "static\*.*"
  
  DetailPrint "Copiando funciones..."
  SetOutPath "$INSTDIR\Funciones"
  File /r "Funciones\*.*"
  
  SetOutPath "$INSTDIR"
  
  ; Crear acceso directo en Menú Inicio
  DetailPrint "Creando accesos directos..."
  CreateDirectory "$SMPROGRAMS\NetDrop"
  CreateShortCut "$SMPROGRAMS\NetDrop\NetDrop.lnk" "$INSTDIR\NetDrop.exe" "" "$INSTDIR\static\Logo\Logo.ico" 0
  CreateShortCut "$SMPROGRAMS\NetDrop\Desinstalar NetDrop.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\static\Logo\Logo.ico" 0
  
  ; Crear acceso directo en Escritorio
  CreateShortCut "$DESKTOP\NetDrop.lnk" "$INSTDIR\NetDrop.exe" "" "$INSTDIR\static\Logo\Logo.ico" 0
  
  ; Registrar en el registro de Windows
  DetailPrint "Registrando en Windows..."
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop" "DisplayName" "NetDrop - Sistema de Compartición de Archivos"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop" "UninstallString" "$INSTDIR\Uninstall.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop" "InstallLocation" "$INSTDIR"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop" "DisplayIcon" "$INSTDIR\static\Logo\Logo.ico"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop" "Publisher" "NetDrop"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop" "DisplayVersion" "1.0"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop" "NoModify" 1
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop" "NoRepair" 1
  
  ; Crear desinstalador
  WriteUninstaller "$INSTDIR\Uninstall.exe"
  
  DetailPrint "¡Instalación completada!"
SectionEnd

; Sección de desinstalación
Section "Uninstall"
  DetailPrint "Desinstalando NetDrop..."
  
  ; Eliminar archivos
  RMDir /r "$INSTDIR"
  
  ; Eliminar accesos directos
  RMDir /r "$SMPROGRAMS\NetDrop"
  Delete "$DESKTOP\NetDrop.lnk"
  
  ; Eliminar del registro
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NetDrop"
  
  DetailPrint "¡Desinstalación completada!"
SectionEnd
