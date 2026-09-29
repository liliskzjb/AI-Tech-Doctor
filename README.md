# AI Tech Doctor

AI Tech Doctor es un asistente inteligente diseñado para monitorear el estado de un servidor y generar diagnósticos técnicos mediante inteligencia artificial.

El sistema obtiene métricas reales del equipo, como el uso de CPU, memoria RAM y almacenamiento. A partir de estas métricas, los procesos en ejecución y el problema reportado por el usuario, AI Tech Doctor utiliza un sistema RAG (Retrieval-Augmented Generation) y un modelo de inteligencia artificial para generar un diagnóstico y recomendaciones.

## Objetivo

Desarrollar un asistente inteligente capaz de detectar posibles problemas de rendimiento en un servidor y proporcionar diagnósticos técnicos utilizando métricas reales del sistema, recuperación de información mediante RAG e inteligencia artificial generativa.

## Funcionalidades

- Monitoreo del uso de CPU.
- Monitoreo del uso de memoria RAM.
- Monitoreo del almacenamiento.
- Detección de estados normales y de alerta.
- Identificación de procesos con mayor consumo de recursos.
- Registro del problema observado por el usuario.
- Recuperación de documentación técnica mediante RAG.
- Generación de diagnósticos mediante inteligencia artificial.
- Visualización de métricas desde una interfaz web.
- Visualización de los fragmentos recuperados por RAG.

## Funcionamiento general

AI Tech Doctor sigue el siguiente flujo:

1. `psutil` obtiene las métricas reales del servidor.
2. El sistema analiza CPU, RAM, disco y procesos.
3. El usuario describe el problema observado.
4. El módulo RAG transforma la consulta en embeddings.
5. Se buscan los fragmentos más relacionados dentro de la base de conocimiento.
6. Las métricas, los procesos, el problema reportado y el contexto recuperado se envían al modelo de IA.
7. La IA genera un diagnóstico y recomendaciones.
8. El resultado se presenta en la interfaz web.

```text
Usuario
   │
   ▼
Interfaz Web
   │
   ▼
FastAPI
   │
   ├──► Métricas del servidor (psutil)
   │
   ├──► Procesos del sistema
   │
   ▼
RAG
   │
   ├──► cpu.txt
   ├──► ram.txt
   └──► disco.txt
   │
   ▼
Modelo de IA mediante Groq
   │
   ▼
Diagnóstico y recomendaciones
```

## Tecnologías utilizadas

- **Python:** lenguaje principal utilizado para desarrollar la aplicación.
- **FastAPI:** framework utilizado para crear la API y comunicar los diferentes componentes del sistema.
- **Uvicorn:** servidor utilizado para ejecutar la aplicación FastAPI.
- **psutil:** biblioteca utilizada para obtener métricas reales de CPU, memoria RAM, disco y procesos del servidor.
- **Groq:** plataforma utilizada para acceder al modelo de inteligencia artificial encargado de generar los diagnósticos.
- **Sentence Transformers:** utilizado para generar embeddings de la documentación técnica y las consultas.
- **Scikit-learn:** utilizado para calcular la similitud entre la consulta y los fragmentos de documentación.
- **RAG (Retrieval-Augmented Generation):** técnica utilizada para recuperar información técnica relevante antes de generar el diagnóstico.
- **HTML:** estructura de la interfaz web.
- **CSS:** diseño visual de la interfaz.
- **JavaScript:** actualización de métricas y comunicación de la interfaz con la API.
- **Ubuntu Server:** sistema operativo utilizado para ejecutar AI Tech Doctor.
- **Hyper-V:** plataforma de virtualización utilizada para alojar el servidor Ubuntu durante el desarrollo y las pruebas.

## Estructura del proyecto

```text
ai-tech-doctor/
├── api.py
├── ia.py
├── monitor.py
├── rag.py
├── prueba_ia.py
├── prueba_rag.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── conocimiento/
│   ├── cpu.txt
│   ├── ram.txt
│   └── disco.txt
│
├── static/
│   ├── app.js
│   └── styles.css
│
└── templates/
    └── index.html
```

### Archivos principales

- `api.py`: contiene la API desarrollada con FastAPI y los endpoints utilizados por la aplicación.
- `monitor.py`: contiene funciones relacionadas con el monitoreo de los recursos del servidor.
- `ia.py`: realiza la comunicación con el modelo de inteligencia artificial y genera el diagnóstico.
- `rag.py`: implementa la recuperación de información mediante RAG.
- `prueba_ia.py`: permite realizar pruebas individuales de la integración con el modelo de IA.
- `prueba_rag.py`: permite comprobar el funcionamiento del sistema de recuperación de información.
- `conocimiento/`: contiene la documentación técnica utilizada por el sistema RAG.
- `templates/index.html`: contiene la estructura de la interfaz web.
- `static/styles.css`: contiene los estilos de la interfaz.
- `static/app.js`: contiene la lógica del lado del cliente y la comunicación con la API.
- `requirements.txt`: contiene las principales dependencias necesarias para ejecutar el proyecto.
- `.env.example`: muestra la variable de entorno necesaria para configurar la API Key.
- `.gitignore`: evita que archivos privados o innecesarios sean incluidos en el repositorio.

## Requisitos

Para ejecutar el proyecto se requiere:

- Python 3.
- pip.
- Soporte para entornos virtuales de Python.
- Ubuntu Server o un sistema compatible.
- Conexión a Internet.
- Una API Key de Groq.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/liliskzjb/AI-Tech-Doctor.git
cd ai-tech-doctor
```

> La URL será sustituida por la dirección definitiva del repositorio de GitHub.

### 2. Crear un entorno virtual

```bash
python3 -m venv venv
```

### 3. Activar el entorno virtual

```bash
source venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Configuración de la API Key

AI Tech Doctor utiliza una API Key de Groq para acceder al modelo de inteligencia artificial.

Por motivos de seguridad, la clave real no se encuentra almacenada en el repositorio.

El proyecto incluye el archivo:

```text
.env.example
```

Para crear el archivo de configuración se puede utilizar:

```bash
cp .env.example .env
```

Posteriormente se debe editar `.env` y sustituir el valor de ejemplo por una API Key válida:

```text
GROQ_API_KEY=tu_api_key_de_groq
```

El archivo `.env` se encuentra incluido en `.gitignore`, por lo que las credenciales privadas no se publican en el repositorio.

## jecución de AI Tech Doctor

Una vez instalado el proyecto y configurada la API Key, se debe activar el entorno virtual:

```bash
source venv/bin/activate
```

Posteriormente se inicia el servidor:

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

Una vez iniciado, la interfaz puede abrirse desde un navegador utilizando la dirección IP del servidor y el puerto `8000`.

Ejemplo:

```text
http://IP_DEL_SERVIDOR:8000
```

Si el navegador se encuentra dentro del mismo servidor también se puede utilizar:

```text
http://localhost:8000
```

FastAPI también proporciona documentación interactiva de la API mediante:

```text
http://IP_DEL_SERVIDOR:8000/docs
```

## Monitoreo del servidor

AI Tech Doctor utiliza `psutil` para obtener información real del sistema operativo.

Entre las métricas monitoreadas se encuentran:

- Porcentaje de uso de CPU.
- Porcentaje de uso de memoria RAM.
- Porcentaje de utilización del disco.
- Procesos que consumen recursos.
- Estado general del servidor.
- Problemas detectados.

La interfaz actualiza periódicamente estas métricas para mostrar el estado actual del servidor.

Cuando una métrica supera el umbral configurado, AI Tech Doctor puede cambiar el estado del sistema de `NORMAL` a `ALERTA` e indicar el recurso relacionado con el problema.

## Sistema RAG

AI Tech Doctor utiliza **Retrieval-Augmented Generation (RAG)** para proporcionar al modelo de inteligencia artificial información técnica relacionada con el problema detectado.

La base de conocimiento está organizada en:

```text
conocimiento/
├── cpu.txt
├── ram.txt
└── disco.txt
```

Estos documentos contienen información relacionada con problemas de CPU, memoria RAM y almacenamiento.

### Funcionamiento del RAG

1. Los documentos de la base de conocimiento son cargados por el sistema.
2. El contenido se divide en fragmentos.
3. Los fragmentos se transforman en embeddings mediante Sentence Transformers.
4. El usuario describe el problema observado.
5. La consulta se complementa con las métricas y procesos actuales del servidor.
6. La consulta también se transforma en un embedding.
7. Se calcula la similitud entre la consulta y los fragmentos disponibles.
8. Se seleccionan los fragmentos con mayor similitud.
9. Estos fragmentos se proporcionan como contexto al modelo de inteligencia artificial.
10. El modelo genera el diagnóstico tomando en cuenta el problema reportado, las métricas reales y la documentación recuperada.

De esta manera, el diagnóstico no depende únicamente de la información general del modelo, sino que también utiliza la documentación técnica almacenada en el proyecto.

## Generación del diagnóstico

Para generar un diagnóstico, AI Tech Doctor combina diferentes fuentes de información:

```text
Problema reportado por el usuario
             +
Métricas reales del servidor
             +
Procesos en ejecución
             +
Fragmentos recuperados mediante RAG
             ↓
     Modelo de inteligencia artificial
             ↓
      Diagnóstico técnico
```

El modelo puede proporcionar información sobre el problema detectado, posibles causas y recomendaciones relacionadas con el estado actual del servidor.

## Pruebas realizadas

Durante el desarrollo se realizaron pruebas controladas para comprobar el funcionamiento de los principales componentes de AI Tech Doctor.

### Prueba de CPU elevada

Se generó una carga elevada de CPU en el servidor.

Durante la prueba se comprobó que:

- El porcentaje de CPU aumentó.
- AI Tech Doctor detectó el estado de alerta.
- Se identificó el uso elevado de CPU.
- Los procesos relacionados con la carga aparecieron entre los procesos monitoreados.
- RAG recuperó información relacionada con CPU.
- La inteligencia artificial generó un diagnóstico tomando en cuenta las métricas y el problema reportado.

### Prueba de memoria RAM elevada

Se realizó una prueba controlada de consumo de memoria RAM.

Debido al uso de memoria dinámica en Hyper-V, durante la validación se utilizó temporalmente un umbral de prueba para comprobar el funcionamiento de la detección. Una vez finalizada la prueba, el umbral se restauró a su valor normal.

Se comprobó que:

- El consumo de memoria aumentó.
- AI Tech Doctor cambió al estado de alerta.
- Se detectó el uso elevado de memoria RAM.
- RAG recuperó información relacionada con memoria.
- La IA generó un diagnóstico relacionado con el problema reportado y las métricas observadas.

### Prueba de uso elevado de disco

Se realizó una prueba controlada creando temporalmente consumo adicional de almacenamiento.

Para evitar llenar innecesariamente el disco del servidor, durante la validación se utilizó temporalmente un umbral de prueba. Después de comprobar el funcionamiento, el archivo utilizado para la prueba fue eliminado y el umbral se restauró a su valor normal.

Durante esta prueba se comprobó que:

- El porcentaje de utilización del disco aumentó.
- AI Tech Doctor detectó el estado de alerta.
- RAG recuperó documentación relacionada con almacenamiento.
- La inteligencia artificial generó un diagnóstico relacionado con el problema.

Las pruebas permitieron validar el flujo principal del proyecto:

```text
Problema del usuario
        +
Métricas reales
        +
Procesos
        ↓
Detección de problemas
        ↓
Recuperación mediante RAG
        ↓
Modelo de IA
        ↓
Diagnóstico y recomendaciones
```

## Seguridad

La API Key utilizada para acceder a Groq no se encuentra escrita directamente en el código fuente.

La credencial se almacena mediante una variable de entorno dentro de:

```text
.env
```

Este archivo está excluido del repositorio mediante:

```text
.gitignore
```

El repositorio solamente incluye `.env.example`, que permite conocer la configuración necesaria sin exponer credenciales privadas.

Además, el entorno virtual `venv/` y los archivos `__pycache__/` también están excluidos del repositorio.

## Estado del proyecto

AI Tech Doctor se encuentra actualmente como un **prototipo funcional**.

Se encuentran implementados y probados:

- Monitoreo de CPU.
- Monitoreo de memoria RAM.
- Monitoreo de almacenamiento.
- Monitoreo de procesos.
- Detección de estados normales y de alerta.
- Interfaz web.
- Registro del problema observado por el usuario.
- Integración con inteligencia artificial mediante Groq.
- Base de conocimiento técnica.
- Recuperación de información mediante RAG.
- Generación de embeddings.
- Selección de fragmentos mediante similitud.
- Generación de diagnósticos utilizando síntomas, métricas, procesos y contexto recuperado.
- Pruebas controladas de CPU, RAM y disco.

## onsideraciones

AI Tech Doctor es un prototipo académico orientado al diagnóstico asistido de problemas de rendimiento.

Los diagnósticos generados por inteligencia artificial deben considerarse como apoyo técnico y no como sustituto de una revisión especializada del servidor.

El comportamiento del sistema también puede variar dependiendo de los recursos disponibles, el sistema operativo y la configuración del entorno donde sea ejecutado.

## Autor

Proyecto desarrollado como parte de un curso de Inteligencia Artificial.
