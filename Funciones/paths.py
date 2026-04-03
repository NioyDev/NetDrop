import os
import sys

APP_NAME = "NetDrop"


def project_root():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def resource_root():
    if getattr(sys, "frozen", False):
        return sys._MEIPASS
    return project_root()


def data_root():
    base = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    return os.path.join(base, APP_NAME)


def upload_dir():
    return os.path.join(data_root(), "File")


def qr_dir():
    return os.path.join(data_root(), "QR")


def static_dir():
    return os.path.join(resource_root(), "static")


def templates_dir():
    return os.path.join(resource_root(), "templates")


def logo_path():
    return os.path.join(static_dir(), "Logo", "icono.png")


def qr_path():
    return os.path.join(qr_dir(), "Qr.png")


def ensure_runtime_dirs():
    os.makedirs(upload_dir(), exist_ok=True)
    os.makedirs(qr_dir(), exist_ok=True)
    return upload_dir(), qr_dir()
