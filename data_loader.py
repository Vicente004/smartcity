import requests
import json
import random
from datetime import datetime, timedelta

ORION_URL = "http://localhost:1026/v2/entities"
FIWARE_SERVICE = "smartcity"
HEADERS = {
    "Content-Type": "application/json",
    "Fiware-Service": FIWARE_SERVICE
}
NUM_UPDATES = 400
DIAS_SIMULACION = 60 
FECHA_INICIO = datetime.now() - timedelta(days=DIAS_SIMULACION) 

INTERVALO_SEGUNDOS = (DIAS_SIMULACION * 24 * 60 * 60) / NUM_UPDATES

ENTIDADES = [
    {
        "id": "SensorTemp1",
        "atributos": {
            "temperatura": {
                "valor_inicial": 28.0,
                "rango_fluctuacion": 2.0, 
                "tipo": "String"
            }
        }
    },
    {
        "id": "SensorCO2-1",
        "atributos": {
            "co2": {
                "valor_inicial": 412.3,
                "rango_fluctuacion": 15.0, 
                "tipo": "String"
            }
        }
    },
    {
        "id": "SensorAgua1",
        "atributos": {
            "ph": {
                "valor_inicial": 7.2,
                "rango_fluctuacion": 0.5, 
                "tipo": "String"
            },
            "cloro": {
                "valor_inicial": 0.8,
                "rango_fluctuacion": 0.1, 
                "tipo": "String"
            }
        }
    }
]

def enviar_actualizacion(entity_id, payload):
    """Envía la petición PATCH para actualizar la entidad."""
    url = f"{ORION_URL}/{entity_id}/attrs"
    try:
        response = requests.patch(url, headers=HEADERS, data=json.dumps(payload))

        if response.status_code == 204:
            print(f"  Entidad {entity_id} actualizada. Payload: {payload}")
        else:
            print(f"   Entidad {entity_id}. Código: {response.status_code}, Respuesta: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"  No se pudo conectar con Orion para {entity_id}: {e}")

print(f"Iniciando simulación de {NUM_UPDATES} actualizaciones por atributo a lo largo de {DIAS_SIMULACION} días.")
print(f"Intervalo de tiempo simulado entre actualizaciones: {round(INTERVALO_SEGUNDOS / 3600, 2)} horas.")


for i in range(1, NUM_UPDATES + 1):

    fecha_simulada = FECHA_INICIO + timedelta(seconds=i * INTERVALO_SEGUNDOS)
    fecha_str = fecha_simulada.isoformat(timespec='seconds')
    
    print(f"\n--- Actualización {i}/{NUM_UPDATES} - Fecha Simulada: {fecha_str} ---")

    for entidad in ENTIDADES:
        entity_id = entidad["id"]

        update_payload = {}
        
        for attr_name, attr_data in entidad["atributos"].items():

            fluctuacion = random.uniform(-attr_data["rango_fluctuacion"], attr_data["rango_fluctuacion"])
            nuevo_valor_float = attr_data["valor_inicial"] + fluctuacion
            
            nuevo_valor_str = f"{nuevo_valor_float:.2f}" 
            update_payload[attr_name] = {
                "value": nuevo_valor_str,
                "type": attr_data["tipo"],
                "metadata": {
                    "timestamp_sensor": {
                        "value": fecha_str,
                        "type": "DateTime"
                    }
                }
            }

        enviar_actualizacion(entity_id, update_payload)

print("\n--- Simulación de carga de datos finalizada. ---")