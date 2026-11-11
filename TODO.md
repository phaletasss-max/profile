# Elementos Pendientes y Guía de Honestidad — Portafolio & CV

Este documento recopila todos los datos, evidencias y precisiones pendientes de confirmación para mantener la total honestidad y rigor técnico del portafolio y los currículums generados.

---

## 1. Fechas de Experiencia Laboral
- [ ] **Innovatech CMC E.I.R.L. (Prácticas pre-profesionales)**:
  - Estado actual: Marcado como concluido con `TODO: Fechas por confirmar`.
  - Acción requerida: Definir mes y año de inicio y término exactos (ejemplo: *Enero 2026 – Junio 2026*).
- [ ] **Proyectos Freelance & Clientes (Crispitex, AlSimTex, Camitex, Etiquetado, Intercomunicadores)**:
  - Estado actual: Agrupados bajo la sección de experiencia con `TODO: Fechas por confirmar`.
  - Acción requerida: Indicar rango de fechas o períodos de desarrollo y puesta en marcha para cada cliente.

---

## 2. Institución de Convalidación Universitaria
- [ ] **Convalidación a Ingeniería en Ciberseguridad (Egreso previsto: 2029)**:
  - Estado actual: Listado como meta académica con la etiqueta `"Institución por definir (Convalidación)"` y estatus `TODO`.
  - Acción requerida: Una vez formalizado el convenio o matrícula universitaria, actualizar el nombre de la universidad en `i18n/*.json` y en `cv-template.html`.

---

## 3. Certificado y Evento HBXAC
- [ ] **Nombre oficial del evento**:
  - En el certificado original (`photos/Certificate-HBXAC.png`) el evento figura textualmente como **kBxAc CTF 2026**, realizado el **10 de octubre de 2026**.
  - El certificado fue emitido a nombre de tu handle de competencia: **`unqval1f1ed`** (puesto 277).
  - Acción recomendada: Si la organización de kBxAc permite actualizar el nombre en el certificado para que figure *Manuel Vilcazan Mendoza*, solicitar la reemisión; de lo contrario, se conserva documentado con tu alias.

---

## 4. Imágenes y Certificados de Cisco Networking Academy
- [ ] **Cursos de Cisco Networking Academy**:
  - Se han registrado estrictamente como **Cursos** (nunca certificaciones CCNA), con las fechas correspondientes:
    - *Curso: CCNA: Introducción a las redes* — 18 feb 2026
    - *Curso: Conceptos básicos de hardware de computadora* — 19 feb 2026
    - *Curso: Introducción a la ciencia de datos* — 24 feb 2026
    - *Curso: Introducción al Internet de las Cosas* — 28 feb 2026
    - *Curso: Conceptos básicos de redes* — 28 mar 2026
    - *Curso: Conciencia digital* — 16 abr 2026
    - *Curso: Uso de computadoras y dispositivos móviles* — 23 abr 2026
    - *Curso: Introducción a la ciberseguridad* — 23 may 2026
    - *Insignias de módulo*: System Safeguards, Threat Analysis, Cybersecurity Administration.
  - Acción requerida: Subir las constancias/certificados en formato PNG o PDF a `photos/` cuando estén disponibles y agregar el enlace correspondiente si se desea mostrarlos en el lightbox.

---

## 5. Recaptura limpia de FireCal Global (NASA Space Apps 2026)
- [ ] **Captura de FireCal Global (`photos/sensor_calor.png`)**:
  - Estado actual: La captura actual muestra la ventana de comandos `cmd.exe` flotando sobre el mapa (exponiendo la ruta local `D:\nasa-space-apps-2026\...`) y la barra de tareas de Windows.
  - Acción requerida: Volver a iniciar el proyecto localmente y tomar una captura limpia en pantalla completa (modo F11 del navegador) para reemplazar `photos/sensor_calor.png`.
  - Comando tras reemplazar la imagen:
    ```bash
    python3 scripts/build_translations.py && npm run build:cv
    ```

---

## 6. Revisión Humana de Traducciones
- [ ] **Idiomas asistidos por IA**:
  - Los archivos `pt.json`, `fr.json`, `de.json`, `it.json`, `zh.json`, `ja.json`, `ko.json`, `ru.json` tienen `"_meta": { "machine_translated": true, "reviewed": false }`.
  - Todos los términos técnicos (*CTF, pwn, reversing, SSRF, SQLi, SENATI, Hack The Box, TryHackMe, PortSwigger, etc.*) se conservaron intactos en inglés o en su denominación técnica universal.
  - Acción recomendada: Cuando un hablante nativo revise un idioma, cambiar `"reviewed": true` en su respectivo JSON.
