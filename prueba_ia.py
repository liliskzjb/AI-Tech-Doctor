import os 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

respuesta = client.chat.completions.create(
	model = "openai/gpt-oss-20b",
	messages = [
		{	
			"role": "system",
			"content":(
				"Eres un asistente especializado en"
				"soporte tecnico de sistemas Linux"
			)
		},
		{
			"role": "user",
                        "content":(
                                "Un servidor Linux presenta un uso"
                                "de cpu del 95%. ¿Qué debería revisar?"
                        )
		}
	]
)

print(respuesta.choices[0].message.content)
