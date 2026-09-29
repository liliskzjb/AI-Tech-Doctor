import os

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


modelo_embeddings = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def cargar_documentos():
	documentos = []

	carpeta = "conocimiento"

	for archivo in os.listdir(carpeta):

        	if archivo.endswith(".txt"):
            		ruta = os.path.join(carpeta, archivo)

            		with open(
                		ruta,
                		"r",
                		encoding="utf-8"
            		) as f:
                		contenido = f.read()

                		documentos.append({
                    			"archivo": archivo,
                    			"contenido": contenido
                		})
	return documentos

def dividir_en_fragmentos(documentos):
	fragmentos = []

	for documento in documentos:
		parrafos = documento["contenido"].split("\n\n")

		for  numero, parrafo in enumerate(parrafos):
			parrafo = parrafo.strip()
			
			if parrafo:
				fragmentos.append({
					"archivo": documento["archivo"],
					"numero": numero + 1,
					"contenido": parrafo
				})
	
	return fragmentos

documentos = cargar_documentos()

fragmentos = dividir_en_fragmentos(documentos)

textos_fragmentos = [
    fragmento["contenido"]
    for fragmento in fragmentos
]

embeddings_fragmentos = modelo_embeddings.encode(
    textos_fragmentos
)

def buscar_contexto(consulta, cantidad = 3):
	embedding_consulta = modelo_embeddings.encode(
        	[consulta]
    	)

	similitudes = cosine_similarity(
		embedding_consulta,
		embeddings_fragmentos
	)[0]

	indices = similitudes.argsort()[::-1]

	resultados = []

	for indice in indices[:cantidad]:
		fragmento = fragmentos[indice]
    		
		resultados.append({
        	"archivo": fragmento["archivo"],
		"fragmento": fragmento["numero"],
        	"contenido": fragmento["contenido"],
        	"similitud": float(similitudes[indice])
    		})
	return resultados
