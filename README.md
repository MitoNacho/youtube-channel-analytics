
# 📺 YouTube Channel Analytics

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![YouTube API](https://img.shields.io/badge/YouTube-Data_API-red)

Aplicación web desarrollada con **FastAPI** que permite analizar canales de YouTube, comparar estadísticas entre creadores y poner a prueba tus conocimientos con un juego interactivo basado en suscriptores reales obtenidos desde la API oficial de YouTube.

<p align="center">

<img src="docs/images/home.png" alt="YouTube Analytics Home" width="900"/>

</p>

---

# 🚀 Funcionalidades

## 🔍 Análisis de canales

Busca cualquier canal de YouTube y obtén de forma inmediata:

* Avatar del canal
* Número de suscriptores
* Visualizaciones totales
* Número de vídeos publicados
* Últimos vídeos publicados

<p align="center">

<img src="docs/images/channel.png" alt="Channel Analytics" width="900"/>

</p>

---

## 🎬 Vídeos recientes

Visualización de los vídeos más recientes del canal seleccionado.

Incluye:

* Miniaturas de los vídeos
* Título
* Fecha relativa de publicación (Days Ago)
* Enlace directo a YouTube
* Diseño responsive

---

## ⚔️ Comparador de canales

Compara dos canales de YouTube de forma visual y sencilla.

Métricas disponibles:

* Suscriptores
* Visualizaciones
* Número de vídeos

Diseñado para ofrecer una experiencia clara, responsive y orientada al análisis.

<p align="center">

<img src="docs/images/compare.png" alt="Compare Channels" width="900"/>

</p>

---

## 🎮 Guess The Biggest Channel

Nuevo modo de juego interactivo.

El sistema selecciona aleatoriamente dos canales de una misma categoría:

* 🟢 Mid Channels
* 🔵 Big Channels
* 🔴 Mega Channels

El jugador deberá adivinar cuál de los dos tiene más suscriptores.

Características:

* Selección aleatoria de canales
* Categorías equilibradas
* Sistema de racha (streak)
* Verificación automática usando datos reales de YouTube
* Reinicio automático al fallar

Ideal para descubrir creadores y poner a prueba tus conocimientos sobre YouTube.

<p align="center">

<img src="docs/images/game.png" alt="Guess The Biggest Channel" width="900"/>

</p>

---

# 🛠️ Tecnologías utilizadas

## Backend

* FastAPI
* Python
* Requests
* Jinja2
* Python Dotenv

## Frontend

* HTML5
* Bootstrap 5

## APIs Externas

* YouTube Data API v3

---

# 🏗️ Arquitectura del proyecto

```text
youtube-channel-analytics/
│
├── app/
│
├── data/
│   └── channels.py
│
├── routers/
│   ├── channels.py
│   ├── compare.py
│   └── game.py
│
├── services/
│   ├── youtube_service.py
│   └── game_service.py
│
├── templates/
│   ├── home.html
│   ├── channel.html
│   ├── compare.html
│   └── game.html
│
├── utils/
│   ├── formatters.py
│   └── date_formatter.py
│
├── static/
│
├── main.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Instalación

Clona el repositorio:

```bash
git clone https://github.com/MitoNacho/youtube-channel-analytics.git

cd youtube-channel-analytics
```

Crear entorno virtual:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# 🔑 Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
YOUTUBE_API_KEY=tu_api_key
```

La clave puede obtenerse desde Google Cloud habilitando:

```text
YouTube Data API v3
```

---

# ▶️ Ejecución local

```bash
uvicorn app.main:app --reload
```

Acceder desde:

```text
http://127.0.0.1:8000
```

---

# 🎯 Objetivos del proyecto

Este proyecto ha sido desarrollado para profundizar en:

* Consumo de APIs externas
* Arquitectura backend con FastAPI
* Organización modular del código
* Desarrollo frontend con Bootstrap
* Gestión de variables de entorno
* Integración con servicios de terceros
* Diseño de lógica de juego basada en datos reales
* Buenas prácticas de desarrollo web

---

# 💡 Aspectos destacados

* Arquitectura organizada por capas
* Integración con la API oficial de YouTube
* Interfaz responsive
* Comparador visual de canales
* Sistema de juego interactivo
* Formateo automático de métricas
* Formateo relativo de fechas
* Uso de datos reales en tiempo real
* Despliegue en producción

---

# 🌐 Enlaces

### 🚀 Aplicación desplegada

https://youtube-channel-analytics.onrender.com

### 💼 Portfolio

https://mitonacho.github.io/dev/

### 🐙 GitHub

https://github.com/MitoNacho

---

# 👨‍💻 Autor

**Nacho Naves**


