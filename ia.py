import os
from dotenv import load_dotenv
from groq import Groq
from rag import buscar_contexto

load_dotenv()
client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def generar_diagnostico(datos, sintoma):
	procesos_texto = ""

	for proceso in datos["procesos"]:
		procesos_texto += (
			f'- PID {proceso["pid"]}: '
			f'{proceso["nombre"]} | '
			f'CPU: {proceso["cpu"]}% | '
			f'RAM: {proceso["ram"]}%\n'
		)
	
	consulta_rag = f"""
	Problema detectado por el usuario: 
	{sintoma}
	Estado del servidor Linux

	CPU: {datos["cpu"]}%
	RAM: {datos["ram"]}%
	Disco: {datos["disco"]}%
	Problemas detectados: {datos["problemas"]}

	Procesos:
	{procesos_texto}
	"""
	
	fragmentos_rag = buscar_contexto(consulta_rag, cantidad = 3)

	contexto_texto = ""

	for fragmento in fragmentos_rag:
		contexto_texto += (
			f'\nFuente: {fragmento["archivo"]}'
			f'- Fragmento {fragmento["fragmento"]}\n'
			f'{fragmento["contenido"]}\n' 
		)

	prompt = f"""
Analiza el estado de este servidor Linux

PROBLEMA DETECTADO POR EL USUARIO: 
{sintoma}
DATOS REALES DEL SERVIDOR:
Equipo: {datos["equipo"]}
Sistema operativo: {datos["sistema_operativo"]}
CPU: {datos["cpu"]}%
RAM: {datos["ram"]}%
Disco: {datos["disco"]}%
Estado: {datos["estado"]}
Problemas detectados: {datos["problemas"]}

Procesos con mayor consumo: 

{procesos_texto}

DOCUMENTACION TECNICA RECUPERADA MEDIANTE RAG:

{contexto_texto}

Genera un diagnostico tecnico breve. Utiliza exactamente esta estructura:

DIAGNOSTICO: 
Explica que situacion observas

POSIBLES CAUSAS:
Menciona las posibles causas

RECOMENDACIONES:
Indica que deberia revisar el administrador 

Utiliza la documentacion tecnica recuperada como contexto para elaborar tus recomendacion.
No inventes metricas que no aparecen en los datos.
NO afirmes que una causa esta confirmada si los datos solamente indican que es una posibilidad.
"""

	respuesta = client.chat.completions.create(
        	model = "openai/gpt-oss-20b",
        	messages = [
                	{
                        	"role": "system",
                        	"content":(
                                	"Eres AI Tech Doctor, un asistente especializado en"
                                	"diagnostico de sistemas Linux"
                        	)
                	},
                	{
                        	"role": "user",
                        	"content": prompt
                	}
        	]
	)
	return {
		"diagnostico": respuesta.choices[0].message.content,
		"fragmentos_rag": [
			{
				"archivo": fragmento["archivo"],
				"fragmento":fragmento["fragmento"],
				"similitud": round(
						fragmento["similitud"],
						3
				)
			}
			for fragmento in fragmentos_rag
		]
	}
