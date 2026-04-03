#!/usr/bin/env python
import os
import sys
from pathlib import Path

import PyInstaller.__main__


def add_data_args(root: Path, folder_name: str):
    folder = root / folder_name
    if not folder.exists():
        return []

    args = []
    for path in folder.rglob("*"):
        if path.is_file() and "File" not in path.parts and "QR" not in path.parts:
            relative_parent = path.relative_to(root).parent
            args.extend(["--add-data", f"{path}{os.pathsep}{relative_parent}"])
    return args


ROOT = Path(__file__).resolve().parent
ICON_PATH = ROOT / "static" / "Logo" / "Logo.ico"

args = [
    str(ROOT / "app.py"),
    "-F",
    "-w",
    "--name",
    "NetDrop",
    "--icon",
    str(ICON_PATH),
    "--clean",
    "--noconfirm",
    "--collect-all",
    "flask",
    "--collect-all",
    "werkzeug",
    "--specpath",
    str(ROOT / "build"),
    "--paths",
    str(ROOT),
]

args += add_data_args(ROOT, "templates")
args += add_data_args(ROOT, "static")

print("Empaquetando NetDrop...")

try:
    PyInstaller.__main__.run(args)
    print("\nListo. Busca NetDrop.exe en la carpeta dist/")
except Exception as e:
    print(f"\nError: {e}")
    sys.exit(1)
