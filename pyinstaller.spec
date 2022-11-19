# coding: utf-8 -*-


import sys
import os
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path
path = os.path.abspath("D:/Data/DataU/SextoSemestre/IngSoftII/Repositorio/TutoriasRepo/src")
path_fonts=os.path.abspath("D:/Data/DataU/SextoSemestre/IngSoftII/Repositorio/TutoriasRepo/src/fonts")
path_images=os.path.abspath("D:/Data/DataU/SextoSemestre/IngSoftII/Repositorio/TutoriasRepo/src/images")
a = Analysis(
    ["main.py"],
    pathex=[path],
    binaries=[],
    datas=[(path_fonts,"path_fonts"),(path_images,"path_images")],
    hookspath=[kivymd_hooks_path,"D:/Data/DataU/SextoSemestre/IngSoftII/Repositorio/TutoriasRepo/src"],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    debug=False,
    strip=False,
    upx=True,
    name="ucentral_tutorias",
    icon="D:/Data/DataU/SextoSemestre/IngSoftII/output/ucentral_s_logo.ico",
    console=False,
)
