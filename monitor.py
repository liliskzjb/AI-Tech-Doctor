import psutil 
import platform 

#Informacion del sistema 
sistema = platform.system()
nombre_equipo = platform.node()

#Uso de recursos 
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()
disco = psutil.disk_usage("/")

print("\n========== AI TECH DOCTOR ==========\n")

print(f"Equipo: {nombre_equipo}")
print(f"Sistema operativo: {sistema}")

print("\n----- RECURSOS -----")
print(f"CPU: {cpu}%")
print(f"RAM: {ram.percent}%")
print(f"Disco: {disco.percent}%")

print("\n----- ESTADO DEL SISTEMA -----")

problemas = []

if cpu >= 80: 
	problemas.append("Uso elevado de CPU")
if ram.percent >= 80:
	problemas.append("Uso elevado de memoria RAM")
if disco.percent >= 85:
	problemas.append("Poco espacio disponible en disco")
if problemas:
	print("Estado: ALERTA")
	
	for problema in problemas:
		print(f"- {problema}")
else:
	print("Estado: NORMAL")

print("\n----- PROCESOS -----")

procesos = []

for proceso in psutil.process_iter(["pid", "name", "memory_percent"]):
	try:
		procesos.append(proceso.info)
	except (psutil.NoSuchProcess, psutil.AccessDenied):
		pass

procesos =  sorted(procesos, key = lambda proceso: proceso["memory_percent"], reverse = True)

for proceso in procesos[:5]:
	print(f"PID: {proceso['pid']} |" f"{proceso['name']} |" f"RAM: {proceso['memory_percent']:.2f}%")

print("\n====================")
