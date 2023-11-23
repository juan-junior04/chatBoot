import openai
import os

def obtener_respuesta(prompt, model, temperature=0.7, max_tokens=150):
    # Hacer una solicitud a la API de OpenAI
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Imprimir la respuesta del modelo
    respuesta = response['choices'][0]['text'].strip()
    print(respuesta)
    return respuesta

# Accede a tu clave de API desde la variable de entorno
api_key = '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'

if not api_key:
    raise ValueError("La clave de API de OpenAI no está configurada. Configúrala como una variable de entorno.")

# Configura la clave de API
openai.api_key = api_key

# Inicializa el prompt
prompt = ""

# Modelo a utilizar
model = "text-davinci-003"

# Bucle para permitir preguntas continuas
while True:
    # Pregunta al usuario
    pregunta = input("Haz una pregunta: ")

    # Salir del bucle si el usuario ingresa 'salir'
    if pregunta.lower() == 'salir':
        break

    # Agrega la pregunta al prompt
    prompt += " " + pregunta

    # Obtiene y muestra la respuesta
    obtener_respuesta(prompt, model)
