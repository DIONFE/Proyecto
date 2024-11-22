#hola cómo estás
from tabulate import tabulate
def autores():
    print(f"Codigo creado por:\nDaniel Canchon \nLuis Neira\nKevin Herrera\nDilan Hernández")
print(
"""
+================================+
|   ¡Bienvenido al software de   |
|   predicción de enfermedades   |
|       del grupo número 5!      |
|    Aquí consultarás ciertas    |
|    enfermedades de interés     |
|    A continuación, revisa:     |
+================================+
""")

enfermedades = {
    "diabetes": {
        "nombre": "Diabetes",
        "causa": "Insuficiencia de insulina o resistencia a la insulina en el cuerpo",
        "síntomas": "1. Sed excesiva \n2. Micción frecuente \n3. Hambre extrema \n4. Pérdida de peso inexplicable, \n5. Fatiga",
        "diagnóstico": "1. Pruebas de glucosa en sangre \n2. Prueba de A1C \n3. Pruebas de tolerancia a la glucosa",
        "tratamiento": "1. Insulina \n2. Medicamentos orales \n3. Dieta saludable \n4. Ejercicio regular \n5. Monitoreo constante de los niveles de glucosa",
        "material de apoyo:": "https://www.who.int/news-room/fact-sheets/detail/diabetes"

        
        },
    "hipertension": {
        "nombre": "Hipertensión",
        "causa": "1. Genética \n2. Dieta alta en sodio \n3. Sobrepeso \n4. Sedentarismo \n5. Consumo excesivo de alcohol \n6. Estrés",
        "síntomas": "1. Generalmente asintomática en etapas tempranas \n2. Dolor de cabeza \n3. Dificultad para respirar \n4. Mareos, \n5. Visión borrosa \n6. Palpitaciones",
        "diagnóstico": "1. Medición de la presión arterial en múltiples ocasiones \n2. Monitoreo de la presión arterial en casa \n3. Pruebas de laboratorio y electrocardiogramas para detectar daño en órganos",
        "tratamiento": "1. Modificaciones en el estilo de vida (dieta baja en sodio, ejercicio regular, etc.) \n2. Medicamentos antihipertensivos \n3. Manejo del estrés \n4. Reducción del consumo de alcohol y tabaco",
        "material de apoyo": "https://www.who.int/news-room/fact-sheets/detail/hypertension"


    },
    "enfermedad pulmonar": {
        "nombre": "Enfermedad Pulmonar Obstructiva Crónica (EPOC)",
        "causa": "Principalmente causada por el tabaquismo, también exposición a contaminantes, polvo y productos químicos",
        "síntomas": "Tos crónica, producción de esputo, dificultad para respirar, sibilancias, fatiga",
        "diagnóstico": "Pruebas de función pulmonar (espirometría), radiografías de tórax, análisis de gases en sangre arterial",
        "tratamiento": "Dejar de fumar, broncodilatadores, corticosteroides inhalados, terapia de oxígeno, rehabilitación pulmonar",
        "material de apoyo": "https://www.who.int/news-room/fact-sheets/detail/chronic-obstructive-pulmonary-disease-(copd)"

    },
     "asma": {
        "nombre": "Asma",
        "causa": "Inflamación y estrechamiento de las vías respiratorias, desencadenada por factores como alérgenos, infecciones respiratorias, ejercicio o estrés",
        "síntomas": "Dificultad para respirar, sibilancias, opresión en el pecho, tos, especialmente por la noche o temprano en la mañana",
        "diagnóstico": "Pruebas de función pulmonar (espirometría), pruebas de alergia, medición del óxido nítrico exhalado",
        "tratamiento": "Inhaladores (broncodilatadores y corticosteroides), medicamentos de control a largo plazo, evitar desencadenantes, planes de acción para el asma",
        "material de apoyo": "https://www.who.int/news-room/fact-sheets/detail/asthma"

    },
     "hepatitis": {
        "nombre": "Hepatitis",
        "causa": "Infección viral (hepatitis A, B, C, D, E), consumo excesivo de alcohol, toxinas, enfermedades autoinmunes",
        "síntomas": "Fatiga, náuseas, vómitos, dolor abdominal, ictericia (piel y ojos amarillos), orina oscura",
        "diagnóstico": "Pruebas de sangre para detectar la presencia del virus, ecografía del hígado, biopsia hepática",
        "tratamiento": "Antivirales, interferón, cambios en el estilo de vida, evitar el consumo de alcohol, en casos graves, trasplante de hígado",
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/hepatitis"

    },
     "obesidad": {
        "nombre": "Obesidad",
        "causa": "Desequilibrio entre la ingesta calórica y el gasto energético, factores genéticos, estilo de vida sedentario, mala alimentación",
        "síntomas": "Exceso de grasa corporal, dificultad para realizar actividades físicas, problemas respiratorios, fatiga",
        "diagnóstico": "Índice de masa corporal (IMC), medición del perímetro abdominal, análisis de composición corporal",
        "tratamiento": "Dieta equilibrada, ejercicio regular, cambios en el estilo de vida, en algunos casos, medicamentos o cirugía bariátrica",
        "material de apoyo": "https://www.who.int/topics/obesity/es/"

    },
     "dengue": {
      "nombre": "Dengue",
        "causa": "Virus del dengue, transmitido por mosquitos infectados (Aedes aegypti)",
        "síntomas": "Fiebre alta, dolor de cabeza, dolor detrás de los ojos, dolor muscular y articular, náuseas, vómitos, erupciones cutáneas",
        "diagnóstico": "Pruebas de sangre para detectar la presencia del virus, frotis de sangre, pruebas rápidas de diagnóstico",
        "tratamiento": "Medicamentos para aliviar el dolor (acetaminofén), hospitalización en casos graves, hidratación y reposo",
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/dengue-and-severe-dengue"
    },
     "anemia": {
        "nombre": "Anemia",
        "causa": "Deficiencia de hierro, deficiencia de vitamina B12, pérdida de sangre, enfermedades crónicas",
        "síntomas": "Fatiga, debilidad, piel pálida, dificultad para respirar, mareos, dolores de cabeza",
        "diagnóstico": "Análisis de sangre (hemograma completo), niveles de hierro, ferritina y vitamina B12",
        "tratamiento": "Suplementos de hierro, vitamina B12, cambio en la dieta, tratamiento de la causa subyacente",
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/anaemia"

    }, "malaria": {
        "nombre": "Malaria",
        "causa": "Plasmodium (parásitos), transmitidos por mosquitos Anopheles infectados",
        "síntomas": "Fiebre, escalofríos, sudoración, dolor de cabeza, náuseas, vómitos, diarrea, anemia",
        "diagnóstico": "Pruebas de sangre para detectar la presencia de parásitos, frotis de sangre, pruebas rápidas de diagnóstico",
        "tratamiento": "Medicamentos antimaláricos como la cloroquina, artemisinina, seguimiento médico para complicaciones",
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/malaria"

    }, "sida": {
        "nombre": "VIH/SIDA",
        "causa": "Virus de la inmunodeficiencia humana (VIH)",
        "síntomas": "Fiebre, fatiga, inflamación de los ganglios linfáticos, pérdida de peso, infecciones oportunistas",
        "diagnóstico": "Pruebas de detección de anticuerpos del VIH, pruebas de carga viral, pruebas de CD4",
        "tratamiento": "Terapia antirretroviral (TAR), medicamentos para infecciones oportunistas, seguimiento médico regular",
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/hiv-aids"

    }
}

# Función para mostrar la información en una tabla

def mostrar_informacion(enfermedad):
    if enfermedad in enfermedades:
        data = [[key, value] for key, value in enfermedades[enfermedad].items()]
        print(tabulate(data, headers=["Campo", "Descripción"], tablefmt="grid"))
    else:
        print("Enfermedad no encontrada. Por favor, elige entre: Diabetes, hipertensión, enfermedad pulmonar, asma, hepatitis, obesidad, dengue, anemia, malaria, sida \n")
contador=0
while contador != 1:
   tipo_de_enfermedad = int(input("Elige el tipo de enfermedad:\n1. Enfermedades metabólicas crónicas  |  2. Enfermedades trasmisibles \n "))

   if tipo_de_enfermedad == 1:
      enfermedad_elegida = input("Digita la enfermedad con la cual desea acceder al repositorio: Diabetes, hipertensión, asma, obesidad, anemia \n").lower()
      mostrar_informacion(enfermedad_elegida)
      contador = int(input("Si desea terminar el programa digite 1, de otra manera digite cualquier otro número: "))
   elif tipo_de_enfermedad == 2:
      enfermedad_elegida = input("Digite la enfermedad con la cual desea acceder al repositorio: Enfermedad pulmonar, hepatitis, dengue, malaria, sida \n").lower()
      mostrar_informacion(enfermedad_elegida)
      contador = int(input("Si desea terminar el programa digite 1, de otra manera digite cualquier otro número: "))
   else:
      print("Ha digitado un dato erróneo")
      contador = int(input("Si desea terminar el programa digite 1, de otra manera digite cualquier otro número: "))
      autores()

print("¡Gracias por usar el programa!")
autores()