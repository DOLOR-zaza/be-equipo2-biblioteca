# be-equipo2-biblioteca
# 📌 Sistema de Reservaciones de Consultorio Médico

## 👥 Integrantes del equipo
- Jesús Emmanuel Hernández Bibiano  
- Martín Cossio Delgado  
- Bladimir Mejía Hernández  
- Aarón Esteban Téllez Zamudio  

## 🎯 Descripción del proyecto
Este proyecto consiste en el desarrollo de una **API para la gestión de citas en un consultorio médico**.  
El sistema permitirá administrar pacientes, doctores y sus reservaciones de manera eficiente.  

### Funcionalidades principales:
- **CRUD de pacientes:** nombre, edad, contacto, historial médico básico.  
- **CRUD de doctores:** especialidad y horarios de atención.  
- **Sistema de reservaciones:** los pacientes pueden agendar citas con doctores en horarios disponibles.  
- **Validación de choques de horarios:** evita que se crucen citas.  
- **Consulta de citas futuras y pasadas:** mediante endpoints específicos.  
- **Base de datos en SQLite3:** almacenamiento con relaciones entre pacientes, doctores y reservaciones.  

# Consultorio Médico API

API REST en Flask con SQLAlchemy y migraciones, desarrollada bajo el patrón Application Factory.

---

## Instalación

```bash
git clone https://github.com/DOLOR-zaza/be-equipo2-consultorio
cd be-equipo2-consultorio
pip install -r requirements.txt

---
