from tabulate import tabulate

def autores():
    print(f"Código creado por:\nDaniel Canchon\nLuis Neira\nKevin Herrera\nDilan Hernández")

print(
    """
+================================+
|   ¡Bienvenido al software de   |
|   predicción de enfermedades   |
|       del grupo número 5!      |
|    Aquí consultarás ciertas    |
|          enfermedades          |
|        A continuación:         |
+================================+
"""
)

# Diccionario con todas las enfermedades y consejos de cuidado
enfermedades = {
    # Enfermedades metabólicas crónicas
    "diabetes": {
        "tipo": "metabólica crónica",
        "nombre": "Diabetes",
        "causa": "Insuficiencia de insulina o resistencia a la insulina en el cuerpo",
        "síntomas": "1. Sed excesiva \n2. Micción frecuente \n3. Hambre extrema \n4. Pérdida de peso inexplicable \n5. Fatiga",
        "diagnóstico": "1. Pruebas de glucosa en sangre \n2. Prueba de A1C \n3. Pruebas de tolerancia a la glucosa",
        "tratamiento": "1. Insulina \n2. Medicamentos orales \n3. Dieta saludable \n4. Ejercicio regular \n5. Monitoreo constante de los niveles de glucosa",
        "factores de riesgo": ["Obesidad", "Sedentarismo", "Dieta alta en azúcares", "Antecedentes familiares"],
        "población afectada": "Mayormente afecta a personas mayores de 45 años y con antecedentes familiares.",
        "material de apoyo": "para mas informacion validar este Link: https://www.who.int/es/news-room/fact-sheets/detail/diabetes",
        "consejos": [
            "Adopta una dieta equilibrada rica en vegetales, proteínas magras y fibra.",
            "Realiza actividad física regularmente para mantener niveles de glucosa estables.",
            "Monitorea tus niveles de azúcar en sangre según las recomendaciones médicas.",
        ],
    },
    "hipertension": {
        "tipo": "metabólica crónica",
        "nombre": "Hipertensión",
        "causa": "1. Genética \n2. Dieta alta en sodio \n3. Sobrepeso \n4. Sedentarismo \n5. Consumo excesivo de alcohol \n6. Estrés",
        "síntomas": "1. Generalmente asintomática en etapas tempranas \n2. Dolor de cabeza \n3. Dificultad para respirar \n4. Mareos \n5. Visión borrosa \n6. Palpitaciones",
        "diagnóstico": "1. Medición de la presión arterial en múltiples ocasiones \n2. Monitoreo de la presión arterial en casa \n3. Pruebas de laboratorio y electrocardiogramas para detectar daño en órganos",
        "tratamiento": "1. Modificaciones en el estilo de vida (dieta baja en sodio, ejercicio regular, etc.) \n2. Medicamentos antihipertensivos \n3. Manejo del estrés \n4. Reducción del consumo de alcohol y tabaco",
        "factores de riesgo": ["Estrés crónico", "Consumo excesivo de sal", "Obesidad", "Sedentarismo", "Antecedentes familiares"],
        "población afectada": "Personas mayores de 40 años, especialmente con estilos de vida sedentarios.",
                "material de apoyo": "para mas informacion validar este Link: https://www.paho.org/es/enlace/hipertension#:~:text=La%20hipertensión%20es%20definida%20como,para%20bajar%20la%20presión%20arterial.",
        "consejos": [
            "Reduce el consumo de sal en tus comidas.",
            "Haz ejercicio regularmente para mantener un peso saludable.",
            "Evita el consumo excesivo de alcohol y tabaco.",
        ],
    },
    "asma": {
        "tipo": "metabólica crónica",
        "nombre": "Asma",
        "causa": "Inflamación y estrechamiento de las vías respiratorias, desencadenada por factores como alérgenos, infecciones respiratorias, ejercicio o estrés",
        "síntomas": "1. Dificultad para respirar \n2. Sibilancias \n3. Opresión en el pecho \n4. Tos, especialmente por la noche o temprano en la mañana",
        "diagnóstico": "1. Pruebas de función pulmonar (espirometría) \n2. Pruebas de alergia \n3. Medición del óxido nítrico exhalado",
        "tratamiento": "1. Inhaladores (broncodilatadores y corticosteroides) \n2. Medicamentos de control a largo plazo \n3. Evitar desencadenantes \n4. Planes de acción para el asma",
        "factores de riesgo": ["Antecedentes familiares", "Exposición a alérgenos", "Infecciones respiratorias recurrentes", "Tabaquismo pasivo"],
        "población afectada": "Más común en niños y adultos jóvenes con antecedentes familiares o exposición a alérgenos.",
        "material de apoyo": "para mas informacion validar este Link: https://www.who.int/es/news-room/fact-sheets/detail/asthma",
        "consejos": [
            "Evita los desencadenantes conocidos como polvo, humo y alérgenos.",
            "Usa inhaladores según las indicaciones médicas.",
            "Mantén un plan de acción para el manejo de ataques de asma.",
        ],
    },
    # Enfermedades transmisibles
    "dengue": {
        "tipo": "transmisible",
        "nombre": "Dengue",
        "causa": "Virus del dengue, transmitido por mosquitos infectados (Aedes aegypti)",
        "síntomas": "1. Fiebre alta \n2. Dolor de cabeza \n3. Dolor detrás de los ojos, dolor muscular y articular \n4. Náuseas \n5. Vómitos \n6. Erupciones cutáneas",
        "diagnóstico": "1. Pruebas de sangre para detectar el virus \n2. Frotis de sangre \n3. Pruebas rápidas de diagnóstico",
        "tratamiento": "1. Medicamentos para aliviar el dolor (acetaminofén) \n2. Hospitalización en casos graves \n3. Hidratación y reposo",
        "factores de riesgo": ["Mosquitos en la zona", "Clima tropical", "Poca protección contra picaduras", "Viviendas sin mosquiteros"],
        "población afectada": "Más frecuente en niños y adultos jóvenes que viven en zonas tropicales y subtropicales.",
        "material de apoyo": "para mas informacion validar este Link: https://www.who.int/es/news-room/fact-sheets/detail/dengue-and-severe-dengue?gad_source=1&gclid=Cj0KCQiAuou6BhDhARIsAIfgrn5LF-asPwAetw7Zsx_xYBBZP8_lu0cj8a_iQ9DFLMqxdwaOisOVCAUaApTLEALw_wcB",
        "consejos": [
            "Usa mosquiteros y repelentes de insectos para prevenir picaduras.",
            "Elimina los recipientes con agua estancada para evitar la reproducción de mosquitos.",
            "Consulta a un médico si presentas síntomas como fiebre y dolor intenso.",
        ],
    },
    # Nuevas enfermedades añadidas
    "obesidad": {
        "tipo": "metabólica crónica",
        "nombre": "Obesidad",
        "causa": "Desequilibrio entre la ingesta calórica y el gasto energético, influenciado por factores genéticos, ambientales y psicológicos",
        "síntomas": "1. Aumento de peso significativo \n2. Dificultad para realizar actividades físicas \n3. Problemas de autoestima",
        "diagnóstico": "1. Índice de masa corporal (IMC) \n2. Evaluación médica general",
        "tratamiento": "1. Cambios en la dieta \n2. Ejercicio regular \n3. Terapia conductual \n4. Medicamentos en algunos casos \n5. Cirugía bariátrica en casos severos",
        "factores de riesgo": ["Genética", "Sedentarismo", "Dieta poco saludable", "Estrés"],
        "población afectada": "Afecta a personas de todas las edades, especialmente en países con alta disponibilidad de alimentos procesados.",
        "material de apoyo": "para mas informacion validar este Link: https://www.who.int/es/news-room/fact-sheets/detail/obesity-and-overweight",
        "consejos": [
            "Adopta una dieta equilibrada y controla las porciones.",
            "Realiza actividad física al menos 150 minutos a la semana.",
            "Busca apoyo psicológico si es necesario.",
        ],
    },
    "anemia": {
        "tipo": "metabólica crónica",
        "nombre": "Anemia",
        "causa": "Deficiencia de hierro, vitamina B12 o ácido fólico, pérdida de sangre o enfermedades crónicas",
        "síntomas": "1. Fatiga \n2. Debilidad \n3. Palidez \n4. Mareos",
        "diagnóstico": "1. Hemograma completo \n2. Pruebas de hierro y vitaminas",
        "tratamiento": "1. Suplementos de hierro o vitaminas \n2. Cambios en la dieta \n3. Tratamiento de la causa subyacente",
        "factores de riesgo": ["Dieta deficiente", "Menstruación abundante", "Embarazo", "Enfermedades crónicas"],
        "población afectada": "Más común en mujeres en edad fértil y personas con dietas inadecuadas.",
        "material de apoyo": "para mas informacion validar este Link: https://www.who.int/es/health-topics/anaemia#tab=tab_1",
        "consejos": [
            "Incluye alimentos ricos en hierro como carnes rojas, legumbres y vegetales de hoja verde .",
            "Consulta a un médico si presentas síntomas de anemia.",
            "Considera suplementos de hierro si es necesario, siempre bajo supervisión médica.",
        ],
    },
    "hepatitis": {
        "tipo": "transmisible",
        "nombre": "Hepatitis",
        "causa": "Inflamación del hígado, comúnmente causada por virus (hepatitis A, B, C), consumo excesivo de alcohol o toxinas",
        "síntomas": "1. Fatiga \n2. Ictericia (color amarillo en piel y ojos) \n3. Dolor abdominal \n4. Pérdida del apetito",
        "diagnóstico": "1. Análisis de sangre para detectar virus \n2. Ecografía del hígado",
        "tratamiento": "1. Antivirales para hepatitis B y C \n2. Cambios en el estilo de vida \n3. Vacunación para hepatitis A y B",
        "factores de riesgo": ["Consumo de drogas intravenosas", "Relaciones sexuales sin protección", "Viajes a áreas con alta incidencia de hepatitis"],
        "población afectada": "Afecta a personas de todas las edades, especialmente en áreas con poca atención médica.",
        "material de apoyo": "para mas informacion validar este Link: https://www.who.int/es/health-topics/hepatitis#tab=tab_1",
        "consejos": [
            "Vacúnate contra la hepatitis A y B si aún no lo has hecho.",
            "Evita el consumo de alcohol y drogas.",
            "Practica sexo seguro para reducir el riesgo de transmisión.",
        ],
    },
    "Covid-19": {
        "tipo": "transmisible",
        "nombre": "SARS-CoV-2",
        "causa": "Comúnmente por contacto directo hacia un infectado",
        "síntomas": "1. Tos seca \n2. Falta de aire \n3. Pérdida del sentido del gusto y/u olfato \n4. Dolores (corporales, de cabeza, etc.)",
        "diagnóstico": "1. Pruebas de reacción en cadena de la polimerasa \n2. Pruebas virales comunes",
        "tratamiento": "1. Mantenerse en cuarentena \n2. Alimentarse equilibradamente para evitar descompensaciones \n3. Vacunación para evitar complicaciones",
        "factores de riesgo": ["Contacto con directamente infectados", "Tocamiento de superficies al público (postes, baños, etc.)"],
        "población afectada": "Afecta a personas de todas las edades, pero se complica en personas con antecedentes de enfermedades crónicas.",
        "material de apoyo": "para mas informacion validar este Link: https://www.who.int/es/health-topics/coronavirus#tab=tab_1",
        "consejos": [
            "Vacúnate contra la Covid-19, se recomiendan las 3 dosis.",
            "Evita salir y exponerte a cualquier clima, puede afectar aún más a la respiración.",
            "Lávate las manos muy a menudo, evita tocarte la cara e intenta evadir al máximo tocar superficies expuestas a la gente."
        ],
},
    "Fiebre Tifoidea": {
        "tipo":"transmisible",
        "nombre": "Fiebre Tifoidea",
        "causa": "Infección por la bacteria Salmonella, consumo de agua o alimentos contaminados, poca higiene y usualmente deficiente.",
        "síntomas": "1. Fiebre alta\n2. Dolor (de cabeza y abdominal)\n3. Estreñimiento o diarrea\n4. Pérdida del apetito\n5. Manchas rojas en la piel",
        "diagnóstico": "1. Cultivo de sangre\n2. Pruebas serológicas\n3. Examen de heces",
        "tratamiento": "1. Antibióticos (recomendados son ciprofloxacina o ceftriaxona)\n2. Hidratación\n3. Reposo\n4. Supervisión médica",
        "factores de riesgo": ["Consumir comida infectada con heces","Poca higiene con los alimentos","Poca higiene personal (no lavarse las manos, tocarse la cara, etc.)"],
        "población afectada": "Afecta a cualquier población, pero sobre todo a aquellas poblaciones en vías de desarrollo o, en otras palabras, pobreza, como lo son países del África o ciudades alejadas de latinoamérica.", 
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/typhoid-fever",
        "consejos": [
            "Vacunarse contra la fiebre tifoidea es lo mejor que se puede hacer para prevenirla.",
            "Evita manejar alimentos con las manos sucias, siempre manipula CUALQUIER alimento con la correspondiente salubridad.",
            "Evita beber agua de cuerpos de agua extraños o donde el agua no se vea de un aspecto idóneo."
        ]
        },
}

# Función para mostrar información de una enfermedad
def mostrar_informacion(enfermedad):
    if enfermedad in enfermedades:
        datos = [[key.capitalize(), valor] for key, valor in enfermedades[enfermedad].items() if key not in ["factores de riesgo", "tipo", "consejos"]]
        print(tabulate(datos, headers=["Campo", "Descripción"], tablefmt="grid"))
    else:
        print(f"'{enfermedad}' no es válido. Por favor, verifica la lista de enfermedades disponibles.")

# Función para calcular la probabilidad de adquirir una enfermedad y mostrar consejos
def calcular_probabilidad(enfermedad):
    if enfermedad not in enfermedades:
        print("Enfermedad no encontrada.")
        return
    
    # Solicitar edad del usuario
    while True:
        try:
            edad = int(input("Por favor, ingresa tu edad: "))
            break
        except ValueError:
            print("Edad no válida. Por favor, ingresa un número entero.")
    
    print("\nPara calcular la probabilidad, responde las siguientes preguntas:")
    factores = enfermedades[enfermedad]["factores de riesgo"]
    respuestas_positivas = 0

    for factor in factores:
        while True:
            respuesta = input(f"¿Tienes este factor de riesgo? ({factor}) (sí/no): ").strip().lower()
            if respuesta in ["sí","si", "no"]:
                if respuesta == "sí" or respuesta=="si":
                    respuestas_positivas += 1
                break
            else:
                print("Por favor, responde con 'sí' o 'no'.")

    # Ajustar probabilidad por edad
    probabilidad_base = (respuestas_positivas / len(factores)) * 100
    if edad >= 45 and enfermedad in ["diabetes", "hipertension"]:
        probabilidad_base += 10  # Incremento del 10% si es mayor de 45 años para estas enfermedades
    elif edad < 15 and enfermedad in ["dengue"]:
        probabilidad_base += 10  # Incremento del 10% si es menor de 15 años para dengue

    probabilidad_final = min(probabilidad_base, 100)  # Limitar a 100%
    print(f"\nLa probabilidad estimada de desarrollar {enfermedades[enfermedad]['nombre']} es del {probabilidad_final:.2f}%.")
    print("\n Este porcentaje está basado en la información proporcionada. Recuerde que el resultado puede variar, dependiendo de muchos otros factores, sin embargo, si presenta alguno de los síntomas, acuda a su médico de cabecera para una evaluación adecuada.\n")
    print(f"Población más afectada:{enfermedades[enfermedad]['población afectada']}")

    # Mostrar consejos de cuidado
    print("\nConsejos de cuidado:")
    for consejo in enfermedades[enfermedad]["consejos"]:
        print(f"- {consejo}")

# Función para listar enfermedades de una categoría y mostrar opciones
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

            # Solicitar confirmación válida
            while True:
                print("\n¿Te gustaría calcular la probabilidad de adquirir esta enfermedad?")
                calcular = input("(sí/no): ").strip().lower()
                if calcular in ["sí", "si"]:
                    calcular_probabilidad(enfermedad_seleccionada)
                    break
                elif calcular == "no":
                    print("\nGracias por utilizar nuestro sistema de información de enfermedades.")
                    autores()
                    break
                else:
                    print("Entrada no válida. Por favor, responde con 'sí' o 'no'.")
        else:
            print("Número fuera de rango. Intenta de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")

# Menú principal
while True:
    print("\nOpciones:")
    print("1. Ver enfermedades metabólicas crónicas")
    print("2. Ver enfermedades transmisibles")
    print("3. Salir del programa")
    
    try:
        opcion = int(input("Elige una opción (1, 2 o 3): "))
        if opcion == 1:
            listar_y_seleccionar("metabólica crónica")
        elif opcion == 2:
            listar_y_seleccionar("transmisible")
        elif opcion == 3:
            print("Gracias por usar el programa. ¡Hasta luego!")
            autores()
            break
        else:
            print("Opción no válida. Por favor, elige entre 1, 2 y 3.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")