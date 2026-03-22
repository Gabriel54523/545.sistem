# 📦 Sistema de Inventario para Negocio

Un sistema web completo para gestionar inventarios, productos, clientes, proveedores, ventas y compras. Desarrollado con **Flask** y **SQLite/PostgreSQL**.

## 🚀 Inicio Rápido

### Desarrollo Local (Windows/Linux)

```bash
# 1. Crear entorno virtual
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/Mac

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar aplicación
python run.py

# 4. Acceder a http://localhost:5000
```

## 📚 Documentación

- **[Guía de Inicio Rápido](docs/QUICKSTART.md)** - Instalación en 15 minutos
- **[Guía de Producción](docs/DEPLOYMENT.md)** - Desplegar en servidor Linux con Docker
- **[Seguridad](docs/SECURITY.md)** - Mejores prácticas de seguridad
- **[Documentación Técnica](docs/README.md)** - Documentación detallada del proyecto

## ✨ Características Principales

- ✅ **Gestión de Productos** - Crear, editar, eliminar con stock automático
- ✅ **Control de Inventario** - Seguimiento en tiempo real
- ✅ **Gestión de Clientes** - Registro y mantenimiento
- ✅ **Gestión de Proveedores** - Control de compras
- ✅ **Módulo de Ventas** - Facturas y transacciones
- ✅ **Módulo de Compras** - Requisiciones a proveedores
- ✅ **Alertas de Stock** - Notificaciones automáticas
- ✅ **Reportes** - Análisis e informes avanzados
- ✅ **Interfaz Responsiva** - Diseño moderno y amigable

## 🛠️ Stack Técnico

| Componente | Tecnología |
|-----------|-----------|
| **Backend** | Flask 3.0.0 |
| **Base de Datos** | SQLite (dev) / PostgreSQL (prod) |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Autenticación** | Flask-Login |
| **ORM** | SQLAlchemy |

## 📁 Estructura del Proyecto

```
sistema-inventario/
├── app/                          # Aplicación Flask
│   ├── __init__.py
│   ├── models.py                 # Modelos de base de datos
│   ├── routes.py                 # Rutas y API endpoints
│   ├── static/                   # Archivos estáticos
│   │   ├── css/
│   │   └── js/
│   └── templates/                # Templates HTML
│
├── docs/                         # 📚 Documentación
│   ├── README.md
│   ├── QUICKSTART.md
│   ├── DEPLOYMENT.md
│   └── SECURITY.md
│
├── deploy/                       # 🐳 Infraestructura
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── nginx-config.conf
│   ├── inventario.service
│   └── wsgi.py
│
├── config.py                     # Configuración de app
├── run.py                        # Entrada principal
├── requirements.txt              # Dependencias (desarrollo)
├── requirements-prod.txt         # Dependencias (producción)
└── .env.example                  # Variables de entorno
```

## ⚙️ Configuración

### Variables de Entorno

```bash
cp .env.example .env
```

**Producción:**
```env
FLASK_ENV=production
SECRET_KEY=<generar-clave-segura>
DB_PASSWORD=<contraseña-fuerte>
```

## 🐳 Despliegue con Docker

Ver [Guía de Producción](docs/DEPLOYMENT.md) para instalación completa.

```bash
docker-compose up -d
```

## 📞 Soporte

- Revisa la documentación en `/docs`
- Verifica logs: `docker-compose logs -f`
- Troubleshooting en [DEPLOYMENT.md](docs/DEPLOYMENT.md)

## 📄 Licencia

Uso interno - Más detalles en documentación.

---

✨ **Última actualización:** 2026-03-17
