from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from  ia import generar_diagnostico
from pydantic import BaseModel

import psutil
import platform

app = FastAPI(title =  "AI Tech Doctor API", description = "API para monitorear el estado de una maquina virtual", version = "1.0")

class SolicitudDiagnostico(BaseModel):
	sintoma: str

#Archivos HTML 
templates = Jinja2Templates(directory = "templates")

#CSS y Javascript
app.mount("/static", StaticFiles(directory = "static"), name = "static")

def obtener_datos_sistema():
	cpu = psutil.cpu_percent(interval=1)
	ram = psutil.virtual_memory()
	disco = psutil.disk_usage("/")
	
	#Obtener procesos y medir su uso de cpu 
	procesos = []

	for proceso in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
		try: 
			proceso.cpu_percent(None)
		except (psutil.NoSuchProcess, psutil.AccessDenied):
			pass
	#Esperamos un momento para poder calcular el consumo de cpu
	import time
	time.sleep(1)

	for proceso in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
		try:
			procesos.append({
				"pid": proceso.info["pid"],
				"nombre": proceso.info["name"],
				"cpu": proceso.cpu_percent(None),
				"ram": round(proceso.info["memory_percent"], 2)
			})
		except (psutil.NoSuchProcess, psutil.AccessDenied):
			pass

	#Ordenar por mayor consumo de cpu
	procesos = sorted(
		procesos,
		key = lambda p: p["cpu"],
		reverse = True
	)

	#Solo conservar los 5 primeros
	procesos = procesos[:5]

	problemas = []

	if cpu >= 80:
		problemas.append("Uso elevado de CPU")
	if ram.percent >= 80:
		problemas.append("Uso elevado de memoria RAM")
	if disco.percent >= 85:
		problemas.append("Poco espacio disponible en disco")

	estado = "ALERTA" if problemas else "NORMAL"

	return {
      		"equipo": platform.node(),
        	"sistema_operativo": platform.system(),
        	"cpu": cpu,
        	"ram": ram.percent,
        	"disco": disco.percent,
        	"estado": estado,
        	"problemas": problemas,
		"procesos": procesos
    	}

@app.get("/")
def inicio(request: Request):
	return templates.TemplateResponse(request = request, name = "index.html")

@app.get("/estado")
def obtener_estado():
	return obtener_datos_sistema()

@app.post("/diagnosticar")
def diagnosticar(solicitud: SolicitudDiagnostico):
	datos = obtener_datos_sistema()
	resultado = generar_diagnostico(datos, solicitud.sintoma)
	
	return {
		"sintoma": solicitud.sintoma,
		"datos": datos,
		"diagnostico": resultado["diagnostico"],
		"fragmentos_rag": resultado["fragmentos_rag"]
	}
