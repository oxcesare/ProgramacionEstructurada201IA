# =================================================================
# TEMA 4.4: FUNCIONES EXTERNAS
# =================================================================

# -----------------------------------------------------------------
# 4.4.1 DEFINIDOS EN BIBLIOTECAS (Módulos Estándar)
# -----------------------------------------------------------------
# Importamos 'random' para generar datos y 'datetime' para el tiempo.
import random
from datetime import datetime

# -----------------------------------------------------------------
# 4.4.2 DEFINIDAS POR EL USUARIO (Simulación de Módulo Externo)
# -----------------------------------------------------------------
# En un proyecto real, estas funciones estarían en otro archivo .py
# Aquí las agrupamos para demostrar la "Modularidad".

class ModuloPersonaje:
    """Simulación de un archivo externo llamado 'personaje_utils.py'"""
    
    @staticmethod
    def calcular_ataque(fuerza, arma_bonus):
        """Calcula el daño basado en atributos."""
        return fuerza + arma_bonus

    @staticmethod
    def obtener_fecha_registro():
        """Usa otra función externa (datetime) dentro de nuestra función."""
        return datetime.now().strftime("%Y-%m-%d %H:%M")

# -----------------------------------------------------------------
# SCRIPT PRINCIPAL
# -----------------------------------------------------------------

def main():
    print("--- SISTEMA DE GESTIÓN DE HÉROES ---")
    
    # 1. Uso de Funciones de Biblioteca Estándar (4.4.1)
    # No escribimos la lógica del azar, solo la usamos.
    fuerza_base = random.randint(10, 20)
    suerte_critica = round(random.uniform(1.1, 1.5), 2)
    
    # 2. Uso de Funciones Definidas por el Usuario (4.4.2)
    # Llamamos a la lógica que nosotros organizamos "fuera" del flujo principal.
    fecha = ModuloPersonaje.obtener_fecha_registro()
    daño_total = ModuloPersonaje.calcular_ataque(fuerza_base, 5)
    
    # 3. Resultado Final
    print(f"Registro realizado el: {fecha}")
    print(f"Fuerza base (generada por random): {fuerza_base}")
    print(f"Daño calculado (función de usuario): {daño_total}")
    print(f"Multiplicador crítico: {suerte_critica}x")
    
    # Explicación del concepto:
    print("\n[EXPLICACIÓN]")
    print("- 'random' y 'datetime' son 4.4.1 (Vienen con Python).")
    print("- 'ModuloPersonaje' representa el 4.4.2 (Lo creaste tú para dar orden).")

if __name__ == "__main__":
    main()