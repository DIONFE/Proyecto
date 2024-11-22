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
        "Nombre": "Diabetes",
        "Causa": "Insuficiencia de insulina o resistencia a la insulina",
        "Síntomas": "Sed excesiva, micción frecuente, hambre extrema, pérdida de peso",
        "Diagnóstico": "Pruebas de glucosa en sangre, A1C",
        "Tratamiento": "Insulina, medicamentos, dieta, ejercicio",
        "link": "holacrdsadsadwdack"
        
        },
    "hipertension": {
        "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés",
        "link": "como vas"
    },
    "leucemia": {
         "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés",
        "link": "como vas"
    },
     "leucemia": {
         "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés",
        "link": "como vas"
    },
     "leucemia": {
         "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés",
        "link": "como vas"
    },
     "leucemia": {
         "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés",
        "link": "como vas"
    },
     "leucemia": {
         "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés",
        "link": "como vas"
    },
     "leucemia": {
         "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés",
        "link": "como vas"
    }, "leucemia": {
         "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés",
        "link": "como vas"
    }, "leucemia": {
         "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés",
        "link": "como vas"
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