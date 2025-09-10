#!/usr/bin/env python3
"""
Script personalizado para ejecutar tests que permite commits cuando no hay tests.
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Ejecutar tests si existen, sino permitir el commit."""
    tests_dir = Path("tests")

    # Verificar si existe el directorio de tests
    if not tests_dir.exists():
        print("✅ No hay directorio de tests - permitiendo commit")
        return 0

    # Buscar archivos de test
    test_files = list(tests_dir.glob("test_*.py")) + list(tests_dir.glob("*_test.py"))

    if not test_files:
        print("✅ No hay archivos de test encontrados - permitiendo commit")
        return 0

    print(f"🧪 Encontrados {len(test_files)} archivo(s) de test - ejecutando...")

    # Ejecutar pytest
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests/", "--tb=short", "-v"],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print("✅ Todos los tests pasaron")
            return 0
        else:
            print("❌ Algunos tests fallaron:")
            print(result.stdout)
            print(result.stderr)
            return result.returncode

    except Exception as e:
        print(f"❌ Error ejecutando tests: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
