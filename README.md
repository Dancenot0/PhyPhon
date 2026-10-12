# PyPhonOS


<div align="center">
  <a href="docs/index.html"><strong>Leer la documentación completa →</strong></a>
</div>

---

Kit de interfaz (UI) movil para Python con estetica tipo *Material Design 3*,
construido sobre SDL2. Incluye sistema de widgets, layout, tema dinámico,
navegacion por pilas, internacionalizacion, animaciones, inspector y mas.

> Distribucion de ejemplo para PyPI con nombre **`pyphonos`** e importacion
> raiz **`pyphon`** (requiere Python >= 3.9).

## Instalacion

```bash
pip install pyphonos
```

### Dependencias nativas

El kit usa [PySDL2](https://pypi.org/project/PySDL2/) (instalado automaticamente).
Ademas, en tiempo de ejecucion tu sistema necesita las librerias compartidas:

- **SDL2**
- **SDL2_ttf** (tipografias TTF)
- **SDL2_image** (PNG/JPG)

En Windows puedes copiar las DLL (`SDL2.dll`, `SDL2_ttf.dll`, `SDL2_image.dll`)
junto al ejecutable o dejarlas en el `PATH`; o bien instalar el extra `binary`
que las incluye automaticamente:

```bash
pip install "pyphonos[binary]"
``` En Linux usa tu gestor de paquetes
(p. ej. `libsdl2-dev libsdl2-ttf-2.0-0 libsdl2-image-2.0-0`). En macOS, `brew install sdl2 sdl2_ttf sdl2_image`.

## Uso rapido

```python
from pyphon.core.app import MobileApp
from pyphon.core.navigator import Screen
from pyphon.renderer.colors import Palette, Color
from pyphon.widgets import Button, Label, VerticalLayout


class Home(Screen):
    def build(self):
        root = VerticalLayout(width=360, height=800, padding=24, spacing=16)
        root.background_color = Palette.BACKGROUND
        root.add_widget(Label(text="Hola PyPhonOS", size=32, color=Palette.PRIMARY))
        self.add(root)

def main():
    app = MobileApp(titulo="Mi app", ancho=360, alto=800)
    app.load_bundled_resources()   # locales + tema incluidos en el wheel
    app.push_screen(Home())
    app.run()

if __name__ == "__main__":
    main()
```

Tambien puedes ver los ejemplos en `examples/` (calculadora y demo completa).

## Estructura

```
pyphon/            # paquete raiz de importacion
  core/            # app, ventana, tema, i18n, navegacion, animacion...
  renderer/        # canvas SDL2, colores, efectos, iconos, tipografia
  events/          # senales y manejador de eventos
  widgets/         # catalogo de widgets y layouts
  assets/fonts/    # tipografias Roboto (package data del wheel)
  locales/         # es.json, en.json (package data del wheel)
  theme.json       # tema por defecto (package data del wheel)
examples/        # programas de ejemplo
pyproject.toml  # metadatos de publicacion en PyPI
```

## Desarrollo y publicacion

```bash
# Genera sdist + wheel
python -m build

# Prueba local en un entorno limpio
pip install dist/pyphonos-0.1.0-py3-none-any.whl

# Publicar en TestPyPI primero
python -m twine upload --repository testpypi dist/*

# Publicar en PyPI
python -m twine upload dist/*
```

> Necesitas una cuenta en [PyPI](https://pypi.org) y en [Test PyPI](https://test.pypi.org)
> y crear un token API (o credenciales) para `twine`.

## Versionado

Versiones: `0.1.0`. Actualiza `version` en `pyproject.toml` y en
`pyphon/__init__.py` al preparar cada lanzamiento.

## Licencia

MIT. Ver `LICENSE`.