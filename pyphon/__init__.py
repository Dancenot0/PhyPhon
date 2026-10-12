# PyPhonOS
"""PyPhonOS - kit de interfaz (UI) movil para Python construido sobre SDL2.

Instalacion:  pip install pyphonos

Uso rapido (la UI exige tener SDL2 + SDL_ttf + SDL_image disponibles):
    from pyphon.core.app import MobileApp
    from pyphon.core.navigator import Screen
    from pyphon.renderer.colors import Palette, Color
    from pyphon.widgets import Button, Label

Las tipografias Roboto, locales y el tema por defecto viajan dentro del
paquete instalado en pyphon/assets, pyphon/locales y pyphon/theme.json.
"""

__version__ = "0.1.0"
__title__ = "PyPhonOS"
__author__ = "PyPhon Contributors"
__license__ = "MIT"

from pyphon.renderer.colors import Color, Palette      # noqa: F401
from pyphon.renderer.icons import IconDB               # noqa: F401


__all__ = ["core", "renderer", "events", "widgets", "Color", "Palette", "IconDB"]