import openai
import os

def obtener_respuesta(prompt, model, temperature=0.7, max_tokens=150):

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )

    respuesta = response['choices'][0]['text'].strip()
    print(respuesta)
    return respuesta


api_key = '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'

if not api_key:
    raise ValueError("La clave de API de OpenAI no está configurada. Configúrala como una variable de entorno.")

openai.api_key = api_key


prompt = ""

model = "text-davinci-003"


while True:
    
    pregunta = input("Haz una pregunta: ")


    if pregunta.lower() == 'salir':
        break

    prompt += " " + pregunta


    obtener_respuesta(prompt, model)
