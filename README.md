# Portafolio — Manuel Vilcazan Mendoza

Estudiante de Ingeniería en Ciberseguridad (4.º ciclo, SENATI). Juego CTFs y también construyo
plataformas, hardware y software que está en producción.

Es un sitio estático de un solo archivo (`index.html`) sin build step, así que Vercel lo despliega tal cual.

## Contenido

- **Ciberseguridad y comunidad:** [Shadowbyt3s](https://shadowbyt3s.vercel.app/) (plataforma de retos CTF), CTFs de Hack The Box en equipo, paths de TryHackMe, Hack the Andes Black Box #01 (49.20% de réplica exacta)
- **Hardware e IoT:** sistema biométrico con ESP32-S3 (N16R8) y AS608 con enclosure impreso en 3D, y red de intercomunicadores ESP32 entre oficina y taller
- **Software empresarial:** sistema de impresión y etiquetado para Godex GE305 y Zebra, con QR y códigos de barras
- **Web en producción:** [crispitex.pe](https://crispitex.pe/), [alsimtex.com](https://www.alsimtex.com/), [camitex-aqp.vercel.app](https://camitex-aqp.vercel.app/)

## Local

Abre `index.html` en el navegador.

## Actualizar contenido y CV

La base está en `i18n/es.json`; `scripts/build_translations.py` contiene las traducciones generales y `i18n/content-updates.json` los datos de contacto, disponibilidad, fechas y nuevos logros por idioma. Los JSON por idioma y `i18n/bundle.js` se regeneran con:

```bash
npm ci
npm run build:translations
npm run build:cv
```

El generador usa Playwright con Edge, Chrome o Chromium y la plantilla `cv-template.html`. Exporta los diez PDF a `cv/Manuel-Vilcazan-CV-<idioma>.pdf`, que es la ruta pública de descarga de este sitio. Las notas de evidencias se mantienen en `EVIDENCE.md`.
