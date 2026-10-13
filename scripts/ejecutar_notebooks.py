"""Ejecuta los notebooks de los módulos y comprueba que no fallan.

Uso:
    python scripts/ejecutar_notebooks.py          # todos los módulos
    python scripts/ejecutar_notebooks.py 03 04    # solo los módulos indicados

Los notebooks se ejecutan en memoria: los archivos del repositorio no se modifican.
"""

import sys
import time
from pathlib import Path

import nbformat
from nbconvert.preprocessors import CellExecutionError, ExecutePreprocessor

RAIZ = Path(__file__).resolve().parents[1]


def main(filtros):
    notebooks = sorted((RAIZ / "modulos").glob("*/notebook.ipynb"))
    if filtros:
        notebooks = [nb for nb in notebooks if nb.parent.name.split("-")[0] in filtros]
    if not notebooks:
        sys.exit("No se encontraron notebooks para: " + " ".join(filtros))

    fallos = []
    for ruta in notebooks:
        inicio = time.time()
        nb = nbformat.read(ruta, as_version=4)
        ejecutor = ExecutePreprocessor(timeout=900, kernel_name="python3")
        try:
            ejecutor.preprocess(nb, {"metadata": {"path": str(ruta.parent)}})
            print(f"OK     {ruta.parent.name:35s} {time.time() - inicio:6.1f} s")
        except CellExecutionError as error:
            print(f"FALLO  {ruta.parent.name:35s}")
            fallos.append((ruta, error))

    for ruta, error in fallos:
        print(f"\n--- {ruta.relative_to(RAIZ)} ---\n{str(error)[-2000:]}")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
