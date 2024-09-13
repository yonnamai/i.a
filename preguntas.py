import streamlit as st
import pandas as pd
import os

# Título de la aplicación
st.title("Encuesta de Datos Personales")

# Preguntas
nombre = st.text_input("¿Cómo te llamas?")
edad = st.number_input("¿Cuál es tu edad?", min_value=0, max_value=120, step=1)
origen = st.text_input("¿De dónde eres?")

# Botón para guardar la información
if st.button("Guardar respuestas"):
    if nombre and edad and origen:
        # Crear un DataFrame con las respuestas
        data = pd.DataFrame({"Nombre": [nombre], "Edad": [edad], "Origen": [origen]})
        
        # Verificar si el archivo CSV ya existe
        if os.path.exists("respuestas.csv"):
            # Si existe, cargar el archivo y agregar las nuevas respuestas
            data_antigua = pd.read_csv("respuestas.csv")
            data = pd.concat([data_antigua, data], ignore_index=True)
        
        # Guardar las respuestas en un archivo CSV
        data.to_csv("respuestas.csv", index=False)
        st.success("Respuestas guardadas exitosamente.")
    else:
        st.error("Por favor, responde a todas las preguntas.")


import streamlit as st
import pandas as pd

# Título del cuestionario en Markdown
st.markdown("# Preguntas del cuestionario 1: *Las Ciencias de Datos*")
st.markdown("### *Programación*")

# Preguntas del cuestionario
pregunta1 = st.radio(
    "1. ¿Cuánto interés tienes en aprender a programar?",
    ("Mucho", "Algo", "Poco", "Ninguno")
)

pregunta2 = st.multiselect(
    "2. ¿Qué lenguajes de programación conoces o te gustaría aprender?",
    ("Python", "JavaScript", "Java", "Otro")
)

pregunta3 = st.radio(
    "3. ¿Has desarrollado algún proyecto de software o aplicación?",
    ("Sí, por mi cuenta", "Sí, en un curso o taller", "No, pero me gustaría", "No, y no me interesa")
)

# Botón para guardar respuestas
if st.button("Guardar"):
    # Crear un DataFrame con las respuestas
    respuestas = pd.DataFrame({
        'Pregunta 1': [pregunta1],
        'Pregunta 2': [', '.join(pregunta2)],  # Convertir la lista de selección múltiple en una cadena
        'Pregunta 3': [pregunta3]
    })
    
    # Guardar el DataFrame en un archivo CSV
    respuestas.to_csv('respuestas_cuestionario.csv', index=False)
    st.success("Respuestas guardadas en respuestas_cuestionario.csv")


import streamlit as st
import pandas as pd

# Estilos para el fondo con temática de anime
page_bg_img = '''
<style>
body {
background-image: url("https://i.imgur.com/YOUR_ANIME_IMAGE.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Título del cuestionario en Markdown
st.markdown("# Preguntas del cuestionario 2: *Tecnología, Análisis de Datos e Inteligencia Artificial*")

# Sección: Tecnología
st.markdown("### *Tecnología*")

pregunta4 = st.radio(
    "4. ¿Cuánto tiempo al día utilizas dispositivos tecnológicos (teléfono, computadora, tablet, etc.)?",
    ("Menos de 2 horas", "2-4 horas", "4-6 horas", "Más de 6 horas")
)

pregunta5 = st.radio(
    "5. ¿Qué tan cómodo te sientes utilizando nuevas tecnologías?",
    ("Muy cómodo", "Cómodo", "Poco cómodo", "Incómodo")
)

pregunta6 = st.selectbox(
    "6. ¿Qué dispositivo tecnológico consideras indispensable en tu día a día?",
    ("Teléfono", "Computadora", "Tablet", "Otro")
)

# Sección: Análisis de Datos
st.markdown("### *Análisis de Datos*")

pregunta7 = st.radio(
    "7. ¿Sabes qué es el análisis de datos?",
    ("Sí, lo conozco bien", "Sí, he oído hablar de ello", "No, pero me gustaría saber más", "No, y no me interesa")
)

pregunta8 = st.radio(
    "8. ¿Has utilizado alguna vez herramientas para analizar datos (como Excel, Google Sheets, Power BI)?",
    ("Sí, frecuentemente", "Sí, algunas veces", "No, pero me gustaría aprender", "No, y no me interesa")
)

pregunta9 = st.radio(
    "9. ¿Qué tan importante crees que es el análisis de datos en la toma de decisiones?",
    ("Muy importante", "Algo importante", "Poco importante", "No es importante")
)

# Sección: Inteligencia Artificial
st.markdown("### *Inteligencia Artificial*")

pregunta10 = st.radio(
    "10. ¿Qué tan familiarizado estás con el concepto de inteligencia artificial (IA)?",
    ("Muy familiarizado", "Algo familiarizado", "Poco familiarizado", "Nada familiarizado")
)

pregunta11 = st.radio(
    "11. ¿Crees que la inteligencia artificial será útil en tu futura carrera profesional?",
    ("Sí, definitivamente", "Probablemente", "No estoy seguro", "No, no lo creo")
)

pregunta12 = st.multiselect(
    "12. ¿Qué aplicaciones de inteligencia artificial te parecen más interesantes?",
    ("Asistentes virtuales (como Siri o Alexa)", 
     "Recomendaciones personalizadas (como Netflix o Spotify)", 
     "Automóviles autónomos", 
     "Chat, GPT", 
     "Otro")
)

# Botón para guardar respuestas
if st.button("Guardar respuestas"):
    # Crear un DataFrame con las respuestas
    respuestas = pd.DataFrame({
        'Pregunta 4': [pregunta4],
        'Pregunta 5': [pregunta5],
        'Pregunta 6': [pregunta6],
        'Pregunta 7': [pregunta7],
        'Pregunta 8': [pregunta8],
        'Pregunta 9': [pregunta9],
        'Pregunta 10': [pregunta10],
        'Pregunta 11': [pregunta11],
        'Pregunta 12': [', '.join(pregunta12)]  # Convertir la lista de selección múltiple en una cadena
    })
    
    # Guardar el DataFrame en un archivo CSV
    respuestas.to_csv('respuestas_tecnologia_datos_ia.csv', index=False)
    st.success("Respuestas guardadas en respuestas_tecnologia_datos_ia.csv")
