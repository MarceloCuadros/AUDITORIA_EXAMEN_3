
# AUDITORIA_EXAMEN_3

**Repositorio del examen de auditoría de sistemas – Unidad III**  
[Link al repositorio en GitHub](https://github.com/MarceloCuadros/AUDITORIA_EXAMEN_3)

---

## Informe de Auditoría

### 1. Datos Generales

- **Nombre del Sistema Auditdo:** Mesa de Ayuda con IA – Corporate EPIS Pilot  
- **Versión Auditada:** v1.0  
- **Fecha de Ejecución:** 19/11/2025  
- **Auditor:** Raúl Marcelo Cuadros Napa  
- **Alcance de la Auditoría:** Revisión completa del código fuente y funcionalidad del sistema de Mesa de Ayuda con IA, incluyendo backend, frontend y proxy.

---

### 2. Objetivo General

Auditar el sistema de Mesa de Ayuda con IA de Corporate EPIS Pilot para evaluar su correcto funcionamiento, seguridad, integridad de datos y cumplimiento de buenas prácticas de desarrollo de software.

---

### 3. Objetivos Específicos

1. Verificar que el sistema se levante y funcione correctamente al 100%, procesando consultas y creando tickets en la base de datos.  
2. Revisar la integridad y persistencia de los datos en SQLite, incluyendo la creación de tickets y almacenamiento de información relevante.  
3. Evaluar la correcta comunicación entre frontend, backend y proxy (Nginx), asegurando que todas las solicitudes y respuestas se manejen correctamente.  
4. Documentar evidencia del funcionamiento del sistema mediante capturas de pantalla, logs y pruebas de creación de tickets.

---

### 4. Metodología de Auditoría

- Clonar el repositorio del sistema de Mesa de Ayuda con IA.  
- Configurar el entorno de desarrollo usando Docker y Ollama (smollm:360m).  
- Levantar todos los servicios (`backend`, `frontend`, `proxy`) y comprobar que se comuniquen correctamente.  
- Ejecutar pruebas de creación de tickets y verificación en la base de datos (`tickets.db`).  
- Registrar evidencias en la carpeta `/evidencias/` incluyendo logs, pantallas y archivos relevantes.  

---

### 5. Resultados de la Auditoría

| Item | Descripción | Evidencia |
|------|------------|-----------|
| Sistema levantado | Backend, frontend y proxy funcionando correctamente | `<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/5dea8241-1bd0-477e-8e80-53dbf2611da0" />
` |
| Creación de ticket | Prueba de ticket creado vía endpoint `/ask` | <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a2747d88-b436-4e86-8696-9fe01f7dcdce" />
` |
| Logs y comunicación | Revisión de logs del backend y proxy | `<img width="743" height="413" alt="image" src="https://github.com/user-attachments/assets/22775f5a-dcb1-4e80-be13-a40477e5ab66" />
` |

---

### 6. Observaciones y Recomendaciones

- El sistema funciona correctamente con Docker, backend en FastAPI, frontend y proxy Nginx.  
- Se recomienda agregar fecha y hora de creación de tickets para mayor trazabilidad.  
- Se sugiere documentar endpoints y casos de uso para futuras auditorías.  
- Mantener la carpeta `/data` como volumen para persistencia de la base de datos en Docker.

---

### 7. Conclusión

El sistema auditado cumple con los objetivos de funcionamiento y persistencia de datos, asegurando la creación de tickets correctamente. La auditoría confirma que el sistema está operativo al 100% y listo para su uso.

---


