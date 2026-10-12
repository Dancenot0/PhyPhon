# pyphon/_res.py
"""Localizacion fiable de los datos que viajan dentro del paquete PyPhonOS.

Ayuda a que las aplicaciones encuentren locales/, theme.json y assets/fonts
tanto cuando corren desde el repositorio como desde el wheel instalado.
"""
import os

PKG_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(PKG_DIR, "assets")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
LOCALES_DIR = os.path.join(PKG_DIR, "locales")
THEME_JSON = os.path.join(PKG_DIR, "theme.json")

__all__ = ["PKG_DIR", "ASSETS_DIR", "FONTS_DIR", "LOCALES_DIR", "THEME_JSON"]
