# IABD Prep 2026

Preparacion para el Curso de Especializacion en Inteligencia Artificial y Big Data (IABD).
IES Severo Ochoa, Elche. Inicio en octubre de 2026.

Referencia del temario del curso: https://aitor-medrano.github.io/iabd

## Objetivo

Llegar al curso con base solida en los tres bloques con mas peso y que mas cuesta arrancar en frio: Python (lenguaje y datos), MongoDB y AWS. El resto de tecnologias del curso (Hadoop, Spark, Kafka, NiFi, Airflow, Hugging Face e IoT) se ven en clase desde cero, asi que no forman parte de esta preparacion.

## Plan de estudio

13 semanas, del 30 de junio al 28 de septiembre. Ritmo aproximado de 7 a 8 horas por semana. El plan va por delante segun el dominio real: Python base es rapido, asi que se deja mas colchon para Mongo y AWS, que son mas densos. Cada bloque cierra con un examen y un miniproyecto, y al final hay un proyecto integrador.

Bloque 1 - Python (semanas 1 a 5)
- Semanas 1 y 2: Python base (sintaxis, estructuras, comprehensions, unpacking, control de flujo, funciones, modulos y errores) y examen.
- Semanas 3 a 5: Python para datos (numpy y pandas), miniproyecto y examen.

Bloque 2 - MongoDB (semanas 6 a 8)
- CRUD, modelado, consultas, indices, agregaciones y PyMongo, miniproyecto y examen.

Bloque 3 - AWS (semanas 9 a 12)
- Fundamentos, IAM, S3, EC2, RDS, DynamoDB, Lambda, Athena y Glue, miniproyecto y examen.

Cierre (semana 13)
- Proyecto integrador (Python + Mongo + AWS) y repaso global.

El seguimiento semana a semana esta en Notion (workspace IABD Prep 2026).

## Estructura del repo

```
00-python/        Bloque de Python (base y datos)
  01-sintaxis-basica/
  02-estructuras/
  03-comprehensions/
  04-control-de-flujo/
  05-unpacking/
  06-funciones/
  07-modulos-y-errores/
  08-numpy/
  09-pandas/
01-mongodb/       Bloque de MongoDB
  01-intro-crud-modelado/
  02-consultas-indices-agregaciones/
  03-pymongo/
02-aws/           Bloque de AWS
  01-fundamentos-iam-s3-ec2/
  02-rds-dynamodb-lambda/
  03-athena-glue/
proyectos/        Miniproyectos de cada bloque y proyecto integrador
  01-datos-pandas/
  02-mongodb/
  03-aws/
  04-integrador/
```

Cada unidad tiene su propio apuntes.md con la teoria y su ejercicios.py con la practica. La unidad de pandas usa notebooks (.ipynb) en lugar de .py.

## Convenciones

- Apuntes: un apuntes.md por unidad, dentro de la carpeta de esa unidad. Es lo primero que se crea al empezar cada unidad, antes de los ejercicios.
- Codigo: cada unidad resuelve sus ejercicios en ejercicios.py. Solo la unidad de pandas usa notebooks.
- Commits: Conventional Commits. Primero un commit docs: con el apuntes.md al empezar la unidad, y al terminar otro commit feat: con los ejercicios.
- Sin caracteres decorativos ni emojis en apuntes ni en codigo. Solo comentarios normales.

## Entorno

- Windows, Python 3.14, VS Code.
- Entorno virtual en .venv. Se activa en cmd con .venv\Scripts\activate.bat.
- Paquetes base: numpy, pandas, matplotlib, ipykernel.
