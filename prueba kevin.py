from tabulate import tabulate

print(
    """
+================================+
|   ¡Bienvenido al software de   |
|   predicción de enfermedades   |
|       del grupo número 5!      |
|    Aquí consultarás ciertas    |
|    enfermedades de interés     |
+================================+
"""
)

# Diccionario de enfermedades
enfermedades = {
    # No transmisibles
    "diabetes": {
        "tipo": "no transmisible",
        "nombre": "Diabetes",
        "causa": "Insuficiencia de insulina o resistencia a la insulina en el cuerpo",
        "síntomas": "Sed excesiva, micción frecuente, hambre extrema, pérdida de peso inexplicada, fatiga",
        "diagnóstico": "Pruebas de glucosa en sangre, prueba de A1C, pruebas de tolerancia a la glucosa",
        "tratamiento": "Insulina, medicamentos orales, dieta saludable, ejercicio regular, monitoreo constante de los niveles de glucosa",
        "factores de riesgo": ["Obesidad", "Sedentarismo", "Dieta alta en azúcares", "Antecedentes familiares"],
    },
    "hipertension": {
        "tipo": "no transmisible",
        "nombre": "Hipertensión",
        "causa": "Genética, dieta alta en sodio, obesidad, sedentarismo, consumo excesivo de alcohol, estrés",
        "síntomas": "Generalmente asintomática en etapas tempranas, dolor de cabeza, dificultad para respirar, mareos, visión borrosa, palpitaciones",
        "diagnóstico": "Medición de la presión arterial en múltiples ocasiones, monitoreo de la presión arterial en casa, pruebas de laboratorio y ecocardiogramas para detectar daño en órganos",
        "tratamiento": "Modificaciones en el estilo de vida (dieta baja en sodio, ejercicio regular), medicamentos antihipertensivos, manejo del estrés, reducción del consumo de alcohol y tabaco",
        "factores de riesgo": ["Estrés crónico", "Consumo excesivo de sal", "Obesidad", "Sedentarismo", "Antecedentes familiares"],
    },
    "asma": {
        "tipo": "no transmisible",
        "nombre": "Asma",
        "causa": "Inflamación y estrechamiento de las vías respiratorias, desencadenada por factores como alérgenos, infecciones respiratorias, ejercicio o estrés",
        "síntomas": "Dificultad para respirar, sibilancias, opresión en el pecho, tos, especialmente por la noche o temprano en la mañana",
        "diagnóstico": "Pruebas de función pulmonar (espirometría), pruebas de alergia, medición del óxido nítrico exhalado",
        "tratamiento": "Inhaladores (broncodilatadores y corticosteroides), medicamentos de control a largo plazo, evitar desencadenantes, planes de acción para el asma",
        "factores de riesgo": ["Antecedentes familiares", "Exposición a alérgenos", "Infecciones respiratorias recurrentes", "Tabaquismo pasivo"],
    },
    "obesidad": {
        "tipo": "no transmisible",
        "nombre": "Obesidad",
        "causa": "Desequilibrio entre la ingesta calórica y el gasto energético, factores genéticos, estilo de vida sedentario, mala alimentación",
        "síntomas": "Exceso de grasa corporal, dificultad para realizar actividades físicas, problemas respiratorios, fatiga",
        "diagnóstico": "Índice de masa corporal (IMC), medición del perímetro abdominal, análisis de composición corporal",
        "tratamiento": "Dieta equilibrada, ejercicio regular, cambios en el estilo de vida, en algunos casos, medicamentos o cirugía bariátrica",
        "factores de riesgo": ["Dieta alta en calorías", "Sedentarismo", "Genética", "Estrés"],
    },
    # Transmisibles
    "dengue": {
        "tipo": "transmisible",
        "nombre": "Dengue",
        "causa": "Virus del dengue, transmitido por mosquitos infectados (Aedes aegypti)",
        "síntomas": "Fiebre alta, dolor de cabeza, dolor detrás de los ojos, dolor muscular y articular, náuseas, vómitos, erupciones cutáneas",
        "diagnóstico": "Pruebas de sangre para detectar el virus, frotis de sangre, pruebas rápidas de diagnóstico",
        "tratamiento": "Medicamentos para aliviar el dolor (acetaminofén), hospitalización en casos graves, hidratación y reposo",
        "factores de riesgo": ["Mosquitos en la zona", "Clima tropical", "Poca protección contra picaduras", "Viviendas sin mosquiteros"],
    },
}

# Función para mostrar información de una enfermedad
def mostrar_informacion(enfermedad):
    if enfermedad in enfermedades:
        datos = [[clave.capitalize(), valor] for clave, valor in enfermedades[enfermedad].items() if clave not in ["factores de riesgo", "tipo"]]
        print(tabulate(datos, headers=["Campo", "Descripción"], tablefmt="grid"))
    else:
        print(f"'{enfermedad}' no es válido. Por favor, verifica la lista de enfermedades disponibles.")

# Función para calcular la probabilidad de adquirir una enfermedad
def calcular_probabilidad(enfermedad):
    if enfermedad not in enfermedades:
        print("Enfermedad no encontrada.")
        return
    
    print("\nPara calcular la probabilidad, responde las siguientes preguntas:")
    factores = enfermedades[enfermedad]["factores de riesgo"]
    respuestas_positivas = 0

    for factor in factores:
        while True:
            respuesta = input(f"¿Tienes este factor de riesgo? ({factor}) (sí/no): ").strip().lower()
            if respuesta in ["sí", "no"]:
                if respuesta == "sí":
                    respuestas_positivas += 1
                break
            else:
                print("Por favor, responde con 'sí' o 'no'.")

    probabilidad = (respuestas_positivas / len(factores)) * 100
    print(f"\nLa probabilidad estimada de desarrollar {enfermedades[enfermedad]['nombre']} es del {probabilidad:.2f}%.")

# Función para listar enfermedades de una categoría y dar opciones
def listar_y_seleccionar(tipo):
    enfermedades_filtradas = [enf for enf, datos in enfermedades.items() if datos["tipo"] == tipo]
    if not enfermedades_filtradas:
        print("No hay enfermedades disponibles en esta categoría.")
        return
    print("\nSelecciona una enfermedad de la lista:")
    for i, enf in enumerate(enfermedades_filtradas, start=1):
        print(f"{i}. {enf.capitalize()}")
    try:
        seleccion = int(input("Elige el número correspondiente: ")) - 1
        if 0 <= seleccion < len(enfermedades_filtradas):
            enfermedad_seleccionada = enfermedades_filtradas[seleccion]
            mostrar_informacion(enfermedad_seleccionada)
            print("\n¿Te gustaría calcular la probabilidad de adquirir esta enfermedad?")
            calcular = input("(sí/no): ").strip().lower()
            if calcular == "sí":
                calcular_probabilidad(enfermedad_seleccionada)
        else:
            print("Número fuera de rango. Intenta de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")

# Menú principal
while True:
    print("\nOpciones:")
    print("1. Ver enfermedades no transmisibles")
    print("2. Ver enfermedades transmisibles")
    print("3. Salir del programa")
    
    try:
        opcion = int(input("Elige una opción (1, 2 o 3): "))
        if opcion == 1:
            listar_y_seleccionar("no transmisible")
        elif opcion == 2:
            listar_y_seleccionar("transmisible")
        elif opcion == 3:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige entre 1, 2 y 3.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")
