# Ciencia de Datos e IA Aplicada: de los datos a las decisiones

Programa online de **14 semanas** para profesionales que quieren usar ciencia de datos, machine learning e IA generativa para tomar mejores decisiones en su organización. Combina teoría breve, notebooks prácticos en Python, casos de negocio reales y un proyecto final.

> Este repositorio contiene **todo el material del curso**: programa, módulos, notebooks ejecutables, ejercicios, rúbricas y la guía para impartirlo. Está pensado para que puedas lanzarlo como tu propio curso (en una plataforma, con cohortes y mentores) o usarlo para estudiar por tu cuenta.

---

## ¿Para quién es?

- Profesionales de negocio, ingeniería, finanzas, marketing, operaciones o salud que trabajan con datos y quieren dar el salto a modelos predictivos.
- Analistas que dominan Excel/SQL y quieren aprender Python y machine learning.
- Gestores que necesitan **entender y evaluar** proyectos de datos e IA, aunque no programen a diario.

**Requisitos previos:** matemáticas de bachillerato (álgebra, funciones, porcentajes) y ganas de programar. No se necesita experiencia previa en Python: las semanas 0–1 de fundamentos lo cubren.

## Formato

| Elemento | Detalle |
|---|---|
| Duración | 14 semanas (2 de fundamentos + 9 de contenido + 3 de proyecto final) |
| Dedicación | 6–8 horas por semana |
| Clases | Vídeos grabados cortos (10–20 min) + lecturas |
| Mentoría | 1 sesión en vivo semanal de 90 min en grupos reducidos (≤ 25 personas) |
| Práctica | 1 notebook guiado + 1 caso práctico por módulo |
| Evaluación | Cuestionarios, entregas semanales y proyecto final |
| Certificado | Al completar ≥ 80 % de las entregas y aprobar el proyecto final |
| Herramientas | Python, Jupyter/Google Colab, pandas, scikit-learn, statsmodels, NetworkX, PyTorch y la API de Claude |

## Mapa del programa

| Semana | Módulo | Pregunta de negocio que responde |
|---|---|---|
| 0–1 | [00 · Fundamentos de Python para datos](modulos/00-fundamentos-python/) | ¿Cómo cargo, limpio y exploro mis datos? |
| 2 | [01 · Estadística para la toma de decisiones](modulos/01-estadistica/) | ¿Cuánto me puedo fiar de lo que veo en una muestra? |
| 3 | [02 · Datos no estructurados: clustering y reducción de dimensión](modulos/02-aprendizaje-no-supervisado/) | ¿Qué grupos naturales hay en mis clientes/productos? |
| 4 | [03 · Regresión y predicción](modulos/03-regresion/) | ¿Cuánto venderé / cuánto costará? |
| 5 | [04 · Clasificación y pruebas de hipótesis](modulos/04-clasificacion-e-hipotesis/) | ¿Este cliente abandonará? ¿Funcionó mi test A/B? |
| 6 | [05 · Deep learning](modulos/05-deep-learning/) | ¿Cómo aprovecho imágenes, texto y relaciones no lineales? |
| 7 | Semana de recuperación y entrega intermedia | — |
| 8 | [06 · Sistemas de recomendación](modulos/06-sistemas-de-recomendacion/) | ¿Qué producto ofrezco a cada usuario? |
| 9 | [07 · Redes y grafos](modulos/07-redes-y-grafos/) | ¿Quién influye en quién? ¿Qué comunidades existen? |
| 10 | [08 · Analítica predictiva con series temporales](modulos/08-series-temporales/) | ¿Cuál será la demanda del próximo trimestre? |
| 11 | [09 · IA generativa y modelos de lenguaje](modulos/09-ia-generativa/) | ¿Cómo integro LLMs de forma fiable en mis procesos? |
| 12–14 | [Proyecto final](proyecto-final/) | Resolver un problema real de principio a fin |

El detalle semana a semana (objetivos, actividades, entregables y horas) está en **[PROGRAMA.md](PROGRAMA.md)**.

## Estructura del repositorio

```
.
├── README.md                  ← estás aquí
├── PROGRAMA.md                ← calendario detallado y resultados de aprendizaje
├── requirements.txt           ← dependencias de Python
├── modulos/
│   └── NN-nombre/
│       ├── README.md              ← objetivos, lecciones, caso práctico, autoevaluación y lecturas
│       ├── apuntes.md             ← teoría completa de cada lección
│       ├── diapositivas.pdf / .md ← diapositivas (PDF listo para usar; .md editable con Marp)
│       ├── notebook.ipynb         ← práctica guiada, ejecutable en local o en Colab
│       ├── cuestionario.md        ← cuestionario evaluable de 10 preguntas con solucionario
│       ├── recursos-abiertos.md   ← vídeos (YouTube) y lecturas gratuitas, con su licencia
│       ├── guiones.md             ← guiones para grabar los vídeos (instructores)
│       └── soluciones.ipynb       ← soluciones de los ejercicios (instructores)
├── proyecto-final/                ← enunciado, hitos, plantilla de informe y rúbrica
├── docs/
│   ├── guia-del-instructor.md        ← cómo impartir cada semana y las sesiones en vivo
│   ├── evaluacion-y-certificado.md   ← sistema de calificación y criterios
│   ├── recursos-y-licencias.md       ← qué se puede hacer con cada recurso externo
│   └── como-lanzar-el-curso.md       ← plataforma, precios, mentores, marketing
└── scripts/
    ├── ejecutar_notebooks.py      ← comprueba que todos los notebooks se ejecutan sin errores
    └── generar_diapositivas.sh    ← regenera los PDF de las diapositivas tras editarlas
```

## Cómo empezar (estudiantes)

**Opción A – Google Colab (sin instalar nada):** abre cualquier `notebook.ipynb` en GitHub y pulsa *Open in Colab*, o súbelo en [colab.research.google.com](https://colab.research.google.com).

**Opción B – En tu ordenador:**

```bash
git clone <url-de-este-repositorio>
cd AI-and-Data-Science-
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Todos los notebooks usan conjuntos de datos incluidos en las librerías (scikit-learn, statsmodels, NetworkX) o generados en el propio notebook, así que funcionan sin descargar nada. El módulo 09 necesita una clave de la API de Anthropic para las celdas que llaman al modelo; sin ella, esas celdas se saltan y el resto del notebook se ejecuta igual.

## Cómo comprobar el material (instructores)

```bash
python scripts/ejecutar_notebooks.py          # ejecuta todos los notebooks
python scripts/ejecutar_notebooks.py 03 04    # solo los módulos 03 y 04
scripts/generar_diapositivas.sh               # regenera los PDF de las diapositivas (requiere Node.js y Chrome)
```

**Vídeos:** el curso todavía no incluye vídeos grabados. Mientras los produces con los `guiones.md` y las diapositivas de cada módulo, puedes usar los vídeos gratuitos enlazados en cada `recursos-abiertos.md`. Antes de hacerlo, revisa [docs/recursos-y-licencias.md](docs/recursos-y-licencias.md) para saber qué permite cada licencia.

## Licencia

El material está pensado para que lo adaptes. Si vas a comercializarlo, elige una licencia explícita (por ejemplo, CC BY-NC-SA 4.0 para el contenido y MIT para el código) y añádela en un archivo `LICENSE`.
