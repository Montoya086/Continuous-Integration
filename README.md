# Continuous Integration Python Project

Este proyecto demuestra cómo configurar integración continua (CI) para Python usando GitHub Actions y pre-commit hooks.

## 🚀 Características

- **GitHub Actions**: Ejecuta tests automáticamente en cada push y pull request
- **Pre-commit hooks**: Ejecuta tests y verificaciones de código antes de cada commit
- **Múltiples versiones de Python**: Soporta Python 3.9, 3.10, 3.11, y 3.12
- **Cobertura de código**: Genera reportes de cobertura automáticamente
- **Linting y formateo**: Incluye Black, isort, y flake8 para mantener la calidad del código

## 📁 Estructura del Proyecto

```
.
├── .github/
│   └── workflows/
│       └── python-tests.yml    # GitHub Actions workflow
├── src/
│   ├── __init__.py
│   └── text_utils.py           # Módulo principal
├── tests/
│   ├── __init__.py
│   └── test_text_utils.py      # Tests unitarios
├── .pre-commit-config.yaml     # Configuración de pre-commit
├── requirements.txt            # Dependencias
├── setup.py                    # Configuración del paquete
├── pyproject.toml             # Configuración moderna del proyecto
├── pytest.ini                 # Configuración de pytest
├── .flake8                    # Configuración de flake8
├── Makefile                   # Comandos útiles
└── README.md
```

## 🛠️ Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Montoya086/Continuous-Integration
   cd continuous-integration-python
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instala el paquete en modo desarrollo:**
   ```bash
   pip install -e .
   ```

## 🧪 Ejecutar Tests

### Ejecutar todos los tests:
```bash
pytest
```

### Ejecutar tests con cobertura:
```bash
pytest --cov=src --cov-report=html
```

### Usar el Makefile:
```bash
make test          # Ejecutar tests
make test-cov      # Tests con cobertura
make ci            # Pipeline completo (lint + test)
```

## 🔧 Configuración de Pre-commit

Los pre-commit hooks ejecutan automáticamente tests y verificaciones antes de cada commit:

1. **Instalar pre-commit:**
   ```bash
   pip install pre-commit
   ```

2. **Instalar los hooks:**
   ```bash
   pre-commit install
   ```

3. **Ejecutar manualmente en todos los archivos:**
   ```bash
   pre-commit run --all-files
   ```

## 🚀 GitHub Actions

El workflow de GitHub Actions se ejecuta automáticamente en:
- Push a las ramas `main` y `develop`
- Pull requests hacia `main` y `develop`

### Lo que hace el workflow:
1. Configura Python (3.9, 3.10, 3.11, 3.12)
2. Instala dependencias
3. Ejecuta linting (flake8, black, isort)
4. Ejecuta tests con pytest
5. Genera reportes de cobertura
6. Sube cobertura a Codecov (opcional)

## 📊 Cobertura de Código

Los reportes de cobertura se generan automáticamente:
- **Terminal**: `pytest --cov=src --cov-report=term-missing`
- **HTML**: `pytest --cov=src --cov-report=html` (genera `htmlcov/index.html`)
- **XML**: `pytest --cov=src --cov-report=xml` (para CI/CD)

## 🎯 Comandos Útiles

```bash
# Formatear código
make format

# Ejecutar linting
make lint

# Limpiar archivos temporales
make clean

# Instalar pre-commit hooks
make pre-commit-install

# Ver todos los comandos disponibles
make help
```

## 🔍 Verificaciones de Calidad

### Black (Formateo de código)
```bash
black src tests
```

### isort (Ordenamiento de imports)
```bash
isort src tests
```

### flake8 (Linting)
```bash
flake8 src tests
```

## 📝 Configuración de Desarrollo

### VS Code
Si usas VS Code, puedes configurar el formateo automático:

1. Instala la extensión Python
2. Configura Black como formateador por defecto
3. Habilita el formateo al guardar

### PyCharm
1. Ve a Settings > Tools > External Tools
2. Configura Black e isort como herramientas externas
3. Configura pre-commit como herramienta externa

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Troubleshooting

### Error: "pre-commit: command not found"
```bash
pip install pre-commit
```

### Error: "pytest: command not found"
```bash
pip install pytest
```

### Tests fallan en GitHub Actions pero pasan localmente
- Verifica que estés usando las mismas versiones de Python
- Asegúrate de que todas las dependencias estén en `requirements.txt`
- Revisa los logs de GitHub Actions para más detalles

### Pre-commit hooks fallan
```bash
# Ejecutar manualmente para ver errores detallados
pre-commit run --all-files --verbose
```
