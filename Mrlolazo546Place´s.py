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
|          enfermedades          |
|        A continuación:         |
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
        "síntomas": "1.Tos crónica\n2.producción de esputo\n3.dificultad para respirar\n4.sibilancias\n5.fatiga",
        "diagnóstico": "1.Pruebas de función pulmonar (espirometría)\n2.radiografías de tórax\n3.análisis de gases en sangre arterial",
        "tratamiento": "1.Dejar de fumar\n2.broncodilatadores\n3.corticosteroides inhalados\n4.terapia de oxígeno\n5.rehabilitación pulmonar",
        "material de apoyo": "https://www.who.int/news-room/fact-sheets/detail/chronic-obstructive-pulmonary-disease-(copd)"

    },
     "asma": {
        "nombre": "Asma",
        "causa": "Inflamación y estrechamiento de las vías respiratorias, desencadenada por factores como alérgenos, infecciones respiratorias, ejercicio o estrés",
        "síntomas": "1.Dificultad para respirar\n2.sibilancias\n3.opresión en el pecho\n4.tos, especialmente por la noche o temprano en la mañana",
        "diagnóstico": "1.Pruebas de función pulmonar (espirometría)\n2.pruebas de alergia\n3.medición del óxido nítrico exhalado",
        "tratamiento": "1.Inhaladores (broncodilatadores y corticosteroides),\n2.medicamentos de control a largo plazo\n3.evitar desencadenantes\n4.planes de acción para el asma",
        "material de apoyo": "https://www.who.int/news-room/fact-sheets/detail/asthma"

    },
     "hepatitis": {
        "nombre": "Hepatitis",
        "causa": "Infección viral (hepatitis A, B, C, D, E), consumo excesivo de alcohol, toxinas, enfermedades autoinmunes",
        "síntomas": "1.Fatiga\n2.náuseas\n3.vómitos\n4.dolor abdominal\n5.ictericia (piel y ojos amarillos)\n6.orina oscura",
        "diagnóstico": "1.Pruebas de sangre para detectar la presencia del virus\n2.ecografía del hígado\n3.biopsia hepática",
        "tratamiento": "1.Antivirales\n2.interferón\n3.cambios en el estilo de vida\n4.evitar el consumo de alcohol\n5.en casos graves\n6.trasplante de hígado",
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/hepatitis"

    },
     "obesidad": {
        "nombre": "Obesidad",
        "causa": "Desequilibrio entre la ingesta calórica y el gasto energético, factores genéticos, estilo de vida sedentario, mala alimentación",
        "síntomas": "1.Exceso de grasa corporal\n2.dificultad para realizar actividades físicas\n3.problemas respiratorios\n4.fatiga",
        "diagnóstico": "1.Índice de masa corporal (IMC)\n2.medición del perímetro abdominal\n3.análisis de composición corporal",
        "tratamiento": "1.Dieta equilibrada\n2.ejercicio regular\n3.cambios en el estilo de vida\n4.en algunos casos, medicamentos o cirugía bariátrica",
        "material de apoyo": "https://www.who.int/topics/obesity/es/"

    },
     "dengue": {
      "nombre": "Dengue",
        "causa": "Virus del dengue, transmitido por mosquitos infectados (Aedes aegypti)",
        "síntomas": "1.Fiebre alta\n2.dolor de cabeza\n3.Dolor detrás de los ojos, dolor muscular y articular\n4.náuseas\n5.vómitos\n6.erupciones cutáneas",
        "diagnóstico": "1.Pruebas de sangre para detectar la presencia del virus\n2.frotis de sangre\n3.pruebas rápidas de diagnóstico",
        "tratamiento": "1.Medicamentos para aliviar el dolor (acetaminofén)\n2.hospitalización en casos graves\n3.hidratación y reposo",
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/dengue-and-severe-dengue"
    },
     "anemia": {
        "nombre": "Anemia",
        "causa": "Deficiencia de hierro, deficiencia de vitamina B12, pérdida de sangre, enfermedades crónicas",
        "síntomas": "1.Fatiga\n2.debilidad\n3.piel pálida\n4.dificultad para respirar\n5.mareos\n6.dolores de cabeza",
        "diagnóstico": "1.Análisis de sangre (hemograma completo)\n2.niveles de hierro ferritina y vitamina B12",
        "tratamiento": "1.Suplementos de hierro\n2.vitamina B12\n3.cambio en la dieta\n4.tratamiento de la causa subyacente",
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/anaemia"

    }, "malaria": {
        "nombre": "Malaria",
        "causa": "Plasmodium (parásitos), transmitidos por mosquitos Anopheles infectados",
        "síntomas": "1.Fiebre\n2.escalofríos\n3.sudoración\n4.dolor de cabeza\n5.náuseas\n6.vómitos\n7.diarrea\n8.anemia",
        "diagnóstico": "1.Pruebas de sangre para detectar la presencia de parásitos\n2.frotis de sangre\n3.pruebas rápidas de diagnóstico",
        "tratamiento": "1.Medicamentos antimaláricos como la cloroquina\n2.artemisinina\n3.seguimiento médico para complicaciones",
        "material de apoyo": "https://www.who.int/es/news-room/fact-sheets/detail/malaria"

    }, "sida": {
        "nombre": "VIH/SIDA",
        "causa": "Virus de la inmunodeficiencia humana (VIH)",
        "síntomas": "1.Fiebre\n2.fatiga\n3.inflamación de los ganglios linfáticos\n4.pérdida de peso\n5.infecciones oportunistas",
        "diagnóstico": "1.Pruebas de detección de anticuerpos del VIH\n2.pruebas de carga viral\n3.pruebas de CD4",
        "tratamiento": "1.Terapia antirretroviral (TAR\n2.medicamentos para infecciones oportunistas\n3.seguimiento médico regular",
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

#### PARA COLOCAR:
    # IDENTIFICACIÓN AMPLIA DE POBLACIONES, POR EJEMPLO LA DIABETES ES MÁS PROPENSA EN MAYORES DE 45 AÑOS

    # PREVENCIÓN DE ENFERMEDADES EN POBLACIÓN CON MAYOR RIESGO DE TRANSMISIÓN
    