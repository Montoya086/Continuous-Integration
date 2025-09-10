#!/bin/bash

# Script para configurar el proyecto de Continuous Integration

echo "🚀 Configurando proyecto de Continuous Integration para Python..."

# Verificar que Python esté instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado. Por favor instala Python 3.9 o superior."
    exit 1
fi

# Crear entorno virtual si no existe
if [ ! -d "env" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv env
else
    echo "✅ Entorno virtual ya existe"
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source env/bin/activate

# Actualizar pip
echo "⬆️ Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias
echo "📚 Instalando dependencias..."
pip install -r requirements.txt

# Instalar pre-commit
echo "🔗 Instalando pre-commit hooks..."
pre-commit install

# Ejecutar tests para verificar que todo funciona
echo "🧪 Ejecutando tests..."
python scripts/run_tests.py

# Ejecutar linting
echo "🔍 Ejecutando verificaciones de código..."
make lint

echo ""
echo "✅ ¡Configuración completada!"
echo ""
echo "📋 Comandos útiles:"
echo "  make test          - Ejecutar tests"
echo "  make test-cov      - Tests con cobertura"
echo "  make lint          - Verificar código"
echo "  make format        - Formatear código"
echo "  make ci            - Pipeline completo"
echo "  make help          - Ver todos los comandos"
echo ""
echo "🔗 Para configurar pre-commit hooks:"
echo "  pre-commit install"
echo ""
echo "🚀 Para ejecutar el pipeline completo:"
echo "  make ci"
