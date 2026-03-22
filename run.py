"""
Script para ejecutar la aplicación en desarrollo
Para producción: usar wsgi.py con Gunicorn
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

from app import create_app, db

# Crear aplicación con configuración por defecto (development)
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    print("\n" + "="*50)
    print("Sistema de Inventario - Modo Desarrollo")
    print("="*50)
    print("\nServidor en: http://localhost:5000")
    print("NOTA: Para produccion usar: gunicorn wsgi:app\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
