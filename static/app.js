async function actualizarEstado() {
    try {

        const respuesta = await fetch("/estado");

        const datos = await respuesta.json();


        document.getElementById("equipo").textContent = datos.equipo;

        document.getElementById("sistema").textContent = datos.sistema_operativo;

        document.getElementById("cpu").textContent = datos.cpu + "%";

        document.getElementById("ram").textContent = datos.ram + "%";

        document.getElementById("disco").textContent = datos.disco + "%";

        document.getElementById("barra-cpu").style.width = datos.cpu + "%";

        document.getElementById("barra-ram").style.width = datos.ram + "%";

        document.getElementById("barra-disco").style.width = datos.disco + "%";


        const estado = document.getElementById("estado");

        estado.textContent = datos.estado;

        if (datos.estado === "ALERTA") {

            estado.className = "estado alerta";

        } else {

            estado.className = "estado normal";
        }


        const lista = document.getElementById(
            "lista-problemas"
        );


        if (datos.problemas.length === 0) {

            lista.innerHTML =
                "<p>No se detectaron problemas</p>";

        } else {

            lista.innerHTML = "";

            datos.problemas.forEach(problema => {

                const p = document.createElement("p");

                p.textContent = "PELIGRO: " + problema;

                lista.appendChild(p);

            });
        }
	
	const listaProcesos = document.getElementById("lista-procesos");

	listaProcesos.innerHTML = "";
	
	datos.procesos.forEach(proceso => {
		const  p = document.createElement("p");

		p.textContent =
			`${proceso.nombre} | ` +
			`PID: ${proceso.pid} | ` +
			`CPU: ${proceso.cpu}% | ` +
			`RAM: ${proceso.ram}%`; 
		listaProcesos.appendChild(p);
	});

    } catch (error) {

        console.error(
            "Error al obtener el estado:",
            error
        );
    }
}


actualizarEstado();

setInterval(actualizarEstado, 5000);

const botonAnalizar = document.getElementById("btn-analizar");

const resultadoIA = document.getElementById("resultado-ia");

botonAnalizar.addEventListener(
	"click",
        async function () {
        	botonAnalizar.disabled = true;

        	botonAnalizar.textContent = "Analizando...";

 		resultadoIA.textContent = "AI Tech Doctor está analizando el servidor...";
		
		const sintoma = document.getElementById("sintoma").value.trim();

		if (!sintoma) {
			resultadoIA.textContent = "Describe primero el problema";
			botonAnalizar.disabled = false;
			botonAnalizar.textContent = "Analizar con IA";

			return
		}

                 try {
                 	const respuesta = await fetch(
				"/diagnosticar",
				{
					method: "POST",

					headers: {
						"Content-Type": "application/json"
					},

					body: JSON.stringify({
						sintoma: sintoma
					})
				}
			);

                 	const datos = await respuesta.json();

			let fuentesRAG = "\n\n------------------------";
			fuentesRAG += "\nFragmentos recuperados por RAG:\n"

			datos.fragmentos_rag.forEach(fragmento => {
				fuentesRAG += 
					`\n${fragmento.archivo} - ` +
					`Fragmento ${fragmento.fragmento}` +
					`(similitud: ${fragmento.similitud})`;
			});

           		resultadoIA.textContent = datos.diagnostico + fuentesRAG;	

                 } catch (error) {
                 	resultadoIA.textContent = "No fue posible realizar el diagnóstico.";

                 	console.error(error);

                 } finally {
                 	botonAnalizar.disabled = false;

                 	botonAnalizar.textContent = "Analizar con IA"      
           }
        }
);
