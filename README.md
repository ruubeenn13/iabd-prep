# IABD Prep 2026

Repositorio de prácticas y apuntes del plan de preparación para el Curso de Especialización en Inteligencia Artificial y Big Data, IES Severo Ochoa, Elche (inicio octubre 2026, 600h).

## Resumen del plan

Plan comprimido de 7 semanas, del 10 de agosto al 27 de septiembre, centrado en los tres bloques con más peso del curso: Python, MongoDB y AWS. El resto de tecnologías (Hadoop, Spark, Kafka, NiFi, Airflow, Hugging Face e IoT) se cubren en clase desde cero y no entran en esta preparación.

| Dato | Valor |
|---|---|
| Duración | 7 semanas (10 ago a 27 sep) |
| Ritmo | 6 a 8 horas por semana |
| Total estimado | ~50 horas |
| Bloques | Python, MongoDB, AWS |
| Buffer | 28 sep al 4 oct (repaso) |

## Estructura del repo

```
iabd-prep/
├── 00-python/                  Semanas 1-2
│   ├── 01-sintaxis-basica/         variables, tipos y operadores
│   ├── 02-estructuras/             listas, diccionarios, tuplas y sets
│   ├── 03-comprehensions/          hecho
│   ├── 04-control-de-flujo/        condicionales y bucles
│   ├── 05-unpacking/               hecho
│   ├── 06-funciones/               definicion, parametros, *args y **kwargs
│   ├── 07-modulos-y-errores/       modulos, paquetes y manejo de errores
│   └── 08-python-para-datos/       numpy y pandas
├── 01-mongodb/                 Semanas 3-4 (se desglosa al llegar)
└── 02-aws/                     Semanas 5-7 (se desglosa al llegar)
```

Cada unidad lleva su propio `apuntes.md` (teoría) y `ejercicios.py` (código). Los bloques de MongoDB y AWS se detallan en sus unidades cuando se empiezan.

## Progreso

| Semana | Bloque | Estado |
|---|---|---|
| 1 | Python base | En progreso |
| 2 | Python para datos | Pendiente |
| 3 | MongoDB: intro y modelado | Pendiente |
| 4 | Agregaciones y PyMongo | Pendiente |
| 5 | AWS core (S3, EC2) | Pendiente |
| 6 | AWS datos y serverless | Pendiente |
| 7 | Athena y repaso | Pendiente |

## Configuración del entorno

1. Clona el repo
```bash
git clone https://github.com/ruubeenn13/iabd-prep.git
cd iabd-prep
```

2. Crea y activa el entorno virtual
```bash
python -m venv .venv
# Windows (cmd):        .venv\Scripts\activate.bat
# Windows (PowerShell): .venv\Scripts\Activate.ps1
# macOS/Linux:          source .venv/bin/activate
```

3. Instala las dependencias
```bash
pip install -r requirements.txt
```

4. Variables de entorno (solo a partir de MongoDB, semana 3)
```bash
cp .env-example .env        # Windows: copy .env-example .env
```

5. Edita `.env` con tus credenciales reales (nunca lo subas a GitHub).

## Sobre el curso

El curso completo (600h) cubre almacenamiento NoSQL con MongoDB, Cloud con AWS, Big Data con Hadoop y Spark, flujos de datos con Kafka, NiFi y Airflow, IA y transfer learning con Hugging Face, e IoT con Node-RED e InfluxDB. Esta preparación solo adelanta los tres primeros bloques. Referencia del profesor: aitor-medrano.github.io/iabd

## Nota sobre el código

El código y las soluciones de los ejercicios están escritos y entendidos a mano, como parte del aprendizaje. Los comentarios explicativos pueden estar generados con ayuda de IA. El repositorio ignora los archivos de configuración de herramientas de IA (Claude, Copilot, Cursor, etc.) mediante `.gitignore`.

## Licencia

MIT.
