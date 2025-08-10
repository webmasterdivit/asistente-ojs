# OJS OpenAI Interfaz (TDD)

Proyecto fullstack que conecta Open Journal Systems (OJS) con OpenAI usando Python (FastAPI) para el backend y Vue.js para el frontend. Utiliza Docker para producción y Docker Compose para desarrollo. El desarrollo sigue la metodología TDD (Test Driven Development).

## Estructura
- **backend/**: API en Python (FastAPI) que conecta con OpenAI y OJS
- **frontend/**: Interfaz de usuario en Vue.js
- **backend/tests/**: Pruebas unitarias para el backend
- **frontend/tests/**: Pruebas unitarias para el frontend

## Desarrollo local
1. Instala Docker y Docker Compose
2. Ejecuta:
   ```bash
   docker-compose up --build
   ```
3. Accede a la interfaz en [http://localhost:8080](http://localhost:8080)

## TDD y pruebas
- Las pruebas unitarias están en la carpeta `backend/tests` y `frontend/tests`.
- Para ejecutar los tests del backend:
   ```bash
   docker-compose run backend pytest
   ```
- Para ejecutar los tests del frontend (requiere configuración de Jest o similar):
   ```bash
   docker-compose run frontend npm run test
   ```

## Variables de entorno
- `OPENAI_API_KEY`: tu clave de OpenAI
- `OJS_API_URL`: URL del API de OJS

## Producción
Construye y ejecuta los contenedores individualmente usando los Dockerfile de cada servicio.

---

Este proyecto es un punto de partida. Personaliza la lógica de conexión a OJS y el manejo de respuestas de OpenAI según tus necesidades.
