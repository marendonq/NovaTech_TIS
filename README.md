# NutriDash: Healthy Delivery & Meal Intelligence
NutriDash no es solo otra plataforma de delivery; es tu aliado integral para una alimentación consciente. Construida con Django, esta plataforma transforma el "takeout" tradicional en una experiencia nutricional personalizada, integrando seguimiento calórico y planificación de comidas en un solo ecosistema.

## Características Principales
+  Healthy Marketplace: Filtros avanzados por macros, alérgenos y tipos de dieta (Keto, Vegana, Paleo, etc.).
+   Real-Time Calorie Tracker: Calcula automáticamente el impacto nutricional de tu pedido y lo suma a tu diario diario.
+   AI Meal Planner: Sugerencias semanales basadas en tus objetivos de salud y presupuesto.
+    Portion Control: Opción para solicitar gramajes específicos en restaurantes asociados.
+    Eco-Delivery Tracking: Seguimiento en tiempo real de pedidos con una flota enfocada en eficiencia.
+    y muchas mas...

## Stack Tecnológico

+ Backend:	Django 5.0 + Django REST Framework
+ Database:	PostgreSQL + PosGIS (map data)
+ API Nutricional:	Open Food Facts (Licencia ODbL)
+ Task Queue:	Celery + Redis (para tracking y notificaciones)
+ Frontend:	Tailwind CSS + Alpine.js
+ Maps API:	OSM Platform (PostGIS + OSRM + MapLibre GL JS)

## Estructura del Proyecto
NutriDash sigue los principios SOLID y un patrón de Monolito Modular para asegurar una separación clara de responsabilidades:

+ ```apps.users```: Biometría, cálculo de TMB (Tasa Metabólica Basal) y gestión de perfiles.
+ ```apps.catalogue```: Menús de restaurantes, listas de ingredientes y datos de macronutrientes.
+ ```apps.logistics```: Geocodificación basada en OSM, cálculo de distancias y despacho de repartidores.
+ ```apps.tracker```: Registro de ingesta diaria y análisis histórico de salud.
+ ```apps.planner```: Motor algorítmico de sugerencias de comidas.

### Instalación y Configuración
Requisitos Previos:

+ Python 3.11+
+ PostgreSQL con extensión PostGIS
+ Redis (para Celery y Caché)

Clonar el repositorio:

  ```Bash
  git clone https://github.com/marendonq/NovaTech_TIS/
  cd nutridash
```
  Configurar el entorno virtual:

  ```Bash
  python -m venv venv
  source venv/bin/activate  # En Windows: venv\Scripts\activate
  pip install -r requirements.txt
  Variables de Entorno:
  Crea un archivo .env en la raíz y añade tus credenciales (DB, API Keys, Secret Key).
```
## Migraciones y Servidor:

  ```Bash
  python manage.py migrate
  python manage.py runserver
  Estructura del Proyecto (Estructura de Apps)
```
## Estándares de Calidad
Para mantener un código limpio y profesional, todas las contribuciones deben cumplir con:

+ Linting: Formateo mediante flake8 y black.
+ Verificación de Tipos: Análisis estático con mypy.
+ Pruebas: Cobertura mínima del 85% mediante pytest.
