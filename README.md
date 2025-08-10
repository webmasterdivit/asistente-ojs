
# OJS OpenAI Interfaz (TDD)

## Propósito
Este proyecto fullstack conecta Open Journal Systems (OJS) con OpenAI, permitiendo automatizar tareas editoriales y enriquecer la experiencia de usuarios y editores. El backend está desarrollado en Python (FastAPI) y el frontend en Vue.js. El flujo de trabajo sigue TDD (Test Driven Development) y utiliza Docker para facilitar el despliegue y la portabilidad.

## Proceso de instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/webmasterdivit/asistente-ojs.git
   cd asistente-ojs
   ```
2. Asegúrate de tener Docker y Docker Compose instalados.
3. Copia y personaliza los archivos `.env` necesarios para backend y frontend si corresponde.
4. Levanta el entorno de desarrollo:
   ```bash
   docker-compose up --build
   ```
5. Accede a la interfaz en [http://localhost:8080](http://localhost:8080)

## Proceso de test
Las pruebas unitarias están en las carpetas `backend/tests` y `frontend/tests`.

- Para ejecutar los tests del backend:
  ```bash
  docker-compose run backend pytest
  ```
- Para ejecutar los tests del frontend (requiere configuración de Jest o similar):
  ```bash
  docker-compose run frontend npm run test
  ```

## Proceso de despliegue
El despliegue continuo está automatizado mediante GitHub Actions y Render:

1. Cada push a la rama `main` dispara un workflow que solicita a Render desplegar la última versión del proyecto.
2. Asegúrate de tener configurados los secrets `RENDER_SERVICE_ID` y `RENDER_API_KEY` en tu repositorio de GitHub.
3. Para despliegue manual o local en producción:
   - Construye y ejecuta los contenedores individualmente usando los Dockerfile de cada servicio.

## Variables de entorno
- `OPENAI_API_KEY`: tu clave de OpenAI
- `OJS_API_URL`: URL del API de OJS

---

Este proyecto es un punto de partida. Personaliza la lógica de conexión a OJS y el manejo de respuestas de OpenAI según tus necesidades.
