TAREA 1

{
	'id': "SensorTemp1",
	'tipo': "SensorTemperatura",
	},
	"atributos": {
		"temperatura": "28",
		"unidad": "Grados Centígrados"
}
{
	'id': "SensorCO2-1",
	'tipo': "SensorCO2",
	},
	"atributos": {
		"co2": "412.3",
		"unidad": "ppm"
}
{
	'id': "SensorAgua1",
	'tipo': "SensorCalidadAgua",
	},
	"atributos": {
		"ph": "7.2",
		"cloro": "0.8",
		unidad": "mgL"
}

TAREA 2

Creación Entidad 1

curl -X POST "http://localhost:1026/v2/entities" -H "Content-Type: application/json" -H "Fiware-Service: smartcity" -d "{ \"id\": \"SensorTemp1\", \"type\": \"SensorTemperatura\", \"temperatura\": { \"value\": \"28\", \"type\": \"String\" }, \"unidad\": { \"value\": \"Grados Centígrados\", \"type\": \"String\" } }"

Creación Entidad 2

curl -X POST "http://localhost:1026/v2/entities" -H "Content-Type: application/json" -H "Fiware-Service: smartcity" -d "{ \"id\": \"SensorCO2-1\", \"type\": \"SensorCO2\", \"co2\": { \"value\": \"412.3\", \"type\": \"String\" }, \"unidad\": { \"value\": \"ppm\", \"type\": \"String\" } }"

Creación Entidad 3

curl -X POST "http://localhost:1026/v2/entities" -H "Content-Type: application/json" -H "Fiware-Service: smartcity" -d "{ \"id\": \"SensorAgua1\", \"type\": \"SensorCalidadAgua\", \"ph\": { \"value\": \"7.2\", \"type\": \"String\" }, \"cloro\": { \"value\": \"0.8\", \"type\": \"String\" }, \"unidad\": { \"value\": \"mgL\", \"type\": \"String\" } }"

Creación de la suscripción

curl -X POST "http://localhost:1026/v2/subscriptions" --header "Content-Type: application/json" --header "Fiware-Service: smartcity" -d "{ \"description\": \"QL Subscription\", \"subject\": { \"entities\": [ { \"idPattern\": \".*\" } ], \"condition\": { \"attrs\": [] } }, \"notification\": { \"http\": { \"url\": \"http://quatum-leap:8668/v2/notify\" }, \"attrs\": [] } }"

Entidades en Mongo

<img width="1919" height="1002" alt="image" src="https://github.com/user-attachments/assets/7e854785-bfda-4c15-9a88-10f133d1f2a4" />

