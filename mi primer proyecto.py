# =================================================================
# PROYECTO: SIMULADOR DE VIABILIDAD Y COSTOS PARA EMPRENDEDORES
# Autor: Mr. Campos
# Descripción: Herramienta interactiva para calcular costos,
#              márgenes de ganancia y diagnóstico de negocio.
# =================================================================

print("=== BIENVENIDO AL SIMULADOR DE VIABILIDAD COMERCIAL ===")
print("Este sistema analizará la rentabilidad de tu producto.\n")

# --- PARTE 1: RECOLECCIÓN DE DATOS (Variables e Inputs) ---
# Nota: Usamos float() para permitir números con decimales
producto = input("¿Cuál es el nombre del producto o negocio?: ")
costo_produccion = float(input("¿Cuánto cuesta producir una sola unidad? ($): "))
precio_venta = float(input("¿A qué precio lo vas a vender al público? ($): "))
ventas_estimadas = float(input("¿Cuántas unidades estimas vender al mes?: "))

# --- PARTE 2: CÁLCULOS MATEMÁTICOS ---
# Calculamos la ganancia limpia por cada unidad vendida
ganancia_por_unidad = precio_venta - costo_produccion

# Ingresos totales y costos totales mensuales
ingresos_totales = precio_venta * ventas_estimadas
costos_totales = costo_produccion * ventas_estimadas
ganancia_neta_mensual = ingresos_totales - costos_totales

# --- PARTE 3: LÓGICA DE NEGOCIO (Condicionales 'if', 'elif', 'else') ---
print("\n=================================================")
print(f"   ANÁLISIS DE VIABILIDAD PARA: {producto.upper()}   ")
print("=================================================")

# Verificamos si el precio de venta cubre los costos
if precio_venta <= costo_produccion:
    print("❌ ALERTA CRÍTICA: Estás perdiendo dinero.")
    print("El precio de venta es menor o igual al costo de fabricación.")
    print("Sugerencia: Incrementa el precio o reduce los costos de los insumos.")

elif ganancia_neta_mensual > 0 and ganancia_neta_mensual < 5000:
    print("⚠️ VIABILIDAD MODERADA: El negocio es rentable pero el margen es bajo.")
    print(f"Ganancia estimada por unidad: ${ganancia_por_unidad:.2f}")
    print(f"Proyección de ganancia neta mensual: ${ganancia_neta_mensual:.2f}")
    print("Sugerencia: Intenta aumentar el volumen de ventas para mejorar el ingreso.")

else:
    print("✅ ¡VIABILIDAD ALTA! El proyecto es altamente rentable.")
    print(f"Ganancia limpia por unidad: ${ganancia_por_unidad:.2f}")
    print(f"Proyección de ganancia neta mensual: ${ganancia_neta_mensual:.2f}")
    print("Sugerencia: El margen es sano. Es un buen momento para planificar la distribución.")

print("=================================================")
print("Fin del análisis. ¡Mucho éxito en tu emprendimiento!")








           