#hola cómo estás
from tabulate import tabulate
print(
"""
+================================+
|   ¡Bienvenido al software de   |
|   predicción de enfermedades   |
|       del grupo número 5!      |
|    Aquí consultarás ciertas    |
|    enfermedades de interés     |
|    A continuación, ingresa:    |
+================================+
""")

enfermedades = {
    "diabetes": {
        "nombre": "Diabetes",
        "causa": "Insuficiencia de insulina o resistencia a la insulina en el cuerpo",
        "síntomas": "Sed excesiva, micción frecuente, hambre extrema, pérdida de peso inexplicada, fatiga",
        "diagnóstico": "Pruebas de glucosa en sangre, prueba de A1C, pruebas de tolerancia a la glucosa",
        "tratamiento": "Insulina, medicamentos orales, dieta saludable, ejercicio regular, monitoreo constante de los niveles de glucosa",
        "link": "https://www.who.int/news-room/fact-sheets/detail/diabetes"

        
        },
    "hipertension": {
        "nombre": "Hipertensión",
        "causa": "Genética, dieta alta en sodio, obesidad, sedentarismo, consumo excesivo de alcohol, estrés",
        "síntomas": "Generalmente asintomática en etapas tempranas, dolor de cabeza, dificultad para respirar, mareos, visión borrosa, palpitaciones",
        "diagnóstico": "Medición de la presión arterial en múltiples ocasiones, monitoreo de la presión arterial en casa, pruebas de laboratorio y ecocardiogramas para detectar daño en órganos",
        "tratamiento": "Modificaciones en el estilo de vida (dieta baja en sodio, ejercicio regular), medicamentos antihipertensivos, manejo del estrés, reducción del consumo de alcohol y tabaco",
        "link": "https://www.who.int/news-room/fact-sheets/detail/hypertension"


    },
    "enfermedad pulmonal": {
        "nombre": "Enfermedad Pulmonar Obstructiva Crónica (EPOC)",
        "causa": "Principalmente causada por el tabaquismo, también exposición a contaminantes, polvo y productos químicos",
        "síntomas": "Tos crónica, producción de esputo, dificultad para respirar, sibilancias, fatiga",
        "diagnóstico": "Pruebas de función pulmonar (espirometría), radiografías de tórax, análisis de gases en sangre arterial",
        "tratamiento": "Dejar de fumar, broncodilatadores, corticosteroides inhalados, terapia de oxígeno, rehabilitación pulmonar",
        "link": "https://www.who.int/news-room/fact-sheets/detail/chronic-obstructive-pulmonary-disease-(copd)"

    },
     "asma": {
        "nombre": "Asma",
        "causa": "Inflamación y estrechamiento de las vías respiratorias, desencadenada por factores como alérgenos, infecciones respiratorias, ejercicio o estrés",
        "síntomas": "Dificultad para respirar, sibilancias, opresión en el pecho, tos, especialmente por la noche o temprano en la mañana",
        "diagnóstico": "Pruebas de función pulmonar (espirometría), pruebas de alergia, medición del óxido nítrico exhalado",
        "tratamiento": "Inhaladores (broncodilatadores y corticosteroides), medicamentos de control a largo plazo, evitar desencadenantes, planes de acción para el asma",
        "link": "https://www.who.int/news-room/fact-sheets/detail/asthma"

    },
     "hepatitis": {
        "nombre": "Hepatitis",
        "causa": "Infección viral (hepatitis A, B, C, D, E), consumo excesivo de alcohol, toxinas, enfermedades autoinmunes",
        "síntomas": "Fatiga, náuseas, vómitos, dolor abdominal, ictericia (piel y ojos amarillos), orina oscura",
        "diagnóstico": "Pruebas de sangre para detectar la presencia del virus, ecografía del hígado, biopsia hepática",
        "tratamiento": "Antivirales, interferón, cambios en el estilo de vida, evitar el consumo de alcohol, en casos graves, trasplante de hígado",
        "link": "https://www.who.int/es/news-room/fact-sheets/detail/hepatitis"

    },
     "obesidad": {
        "nombre": "Obesidad",
        "causa": "Desequilibrio entre la ingesta calórica y el gasto energético, factores genéticos, estilo de vida sedentario, mala alimentación",
        "síntomas": "Exceso de grasa corporal, dificultad para realizar actividades físicas, problemas respiratorios, fatiga",
        "diagnóstico": "Índice de masa corporal (IMC), medición del perímetro abdominal, análisis de composición corporal",
        "tratamiento": "Dieta equilibrada, ejercicio regular, cambios en el estilo de vida, en algunos casos, medicamentos o cirugía bariátrica",
        "link": "https://www.who.int/topics/obesity/es/"

    },
     "dengue": {
      "nombre": "Dengue",
        "causa": "Virus del dengue, transmitido por mosquitos infectados (Aedes aegypti)",
        "síntomas": "Fiebre alta, dolor de cabeza, dolor detrás de los ojos, dolor muscular y articular, náuseas, vómitos, erupciones cutáneas",
        "diagnóstico": "Pruebas de sangre para detectar la presencia del virus, frotis de sangre, pruebas rápidas de diagnóstico",
        "tratamiento": "Medicamentos para aliviar el dolor (acetaminofén), hospitalización en casos graves, hidratación y reposo",
        "link": "https://www.who.int/es/news-room/fact-sheets/detail/dengue-and-severe-dengue"
    },
     "Anemia": {
        "nombre": "Anemia",
        "causa": "Deficiencia de hierro, deficiencia de vitamina B12, pérdida de sangre, enfermedades crónicas",
        "síntomas": "Fatiga, debilidad, piel pálida, dificultad para respirar, mareos, dolores de cabeza",
        "diagnóstico": "Análisis de sangre (hemograma completo), niveles de hierro, ferritina y vitamina B12",
        "tratamiento": "Suplementos de hierro, vitamina B12, cambio en la dieta, tratamiento de la causa subyacente",
        "link": "https://www.who.int/es/news-room/fact-sheets/detail/anaemia"

    }, "Malaria": {
        "nombre": "Malaria",
        "causa": "Plasmodium (parásitos), transmitidos por mosquitos Anopheles infectados",
        "síntomas": "Fiebre, escalofríos, sudoración, dolor de cabeza, náuseas, vómitos, diarrea, anemia",
        "diagnóstico": "Pruebas de sangre para detectar la presencia de parásitos, frotis de sangre, pruebas rápidas de diagnóstico",
        "tratamiento": "Medicamentos antimaláricos como la cloroquina, artemisinina, seguimiento médico para complicaciones",
        "link": "https://www.who.int/es/news-room/fact-sheets/detail/malaria"

    }, "sida": {
        "nombre": "VIH/SIDA",
        "causa": "Virus de la inmunodeficiencia humana (VIH)",
        "síntomas": "Fiebre, fatiga, inflamación de los ganglios linfáticos, pérdida de peso, infecciones oportunistas",
        "diagnóstico": "Pruebas de detección de anticuerpos del VIH, pruebas de carga viral, pruebas de CD4",
        "tratamiento": "Terapia antirretroviral (TAR), medicamentos para infecciones oportunistas, seguimiento médico regular",
        "link": "https://www.who.int/es/news-room/fact-sheets/detail/hiv-aids"

    }
}

# Función para mostrar la información en una tabla

def mostrar_informacion(enfermedad):
    if enfermedad in enfermedades:
        data = [[key, value] for key, value in enfermedades[enfermedad].items()]
        print(tabulate(data, headers=["Campo", "Descripción"], tablefmt="grid"))
    else:
        print("Enfermedad no encontrada. Por favor, elige entre: diabetes, hipertension, leucemia.")
contador=0
while contador != 1:
   tipo_de_enfermedad = int(input("Elige el tipo de enfermedad (1 o 2): "))

   if tipo_de_enfermedad == 1:
      enfermedad_elegida = input("Elige una enfermedad (diabetes, hipertension, leucemia): ").lower()
      mostrar_informacion(enfermedad_elegida)
      contador = int(input("Si desea terminar el programa digite 1: "))
   elif tipo_de_enfermedad == 2:
      enfermedad_elegida = input("Elige una enfermedad (diabetes, hipertension, leucemia): ").lower()
      mostrar_informacion(enfermedad_elegida)
      contador = int(input("Si desea terminar el programa digite 1: "))
   else:
      print("Digito un dato erroneo")
      contador = int(input("Si desea terminar el programa digite 1: "))

print("Descanse")