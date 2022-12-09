# Arquitecturas Emergentes flask sqlite

## Resumen de rutas:
##### Ruta principal
`http://35.153.241.7:5000/`

## Login
+ Ruta de login `username = admin`, `password = admin` por defecto (Metodo POST): `/login`      

## Compañia
+ Agregar compañia (Metodo POST): `/api/addCompany', methods=['POST']`

## Ubicación
+ Agregar locación (Metodo POST): `/api/addLocation`
+ Obtener ubicación (Metodo GET): `/api/getLocation/<company_api_key>/<location_id>`
+ Obtener ubicaciones (Metodo GET): `/api/getLocations/<company_api_key>`
+ Cambiar ubicación (Metodo PUT): `/api/updateLocation`
+ Borrar ubicación (Metodo DELETE): `/api/deleteLocation`

## Sensor
+ Agregar sensor (Metodo POST): `/api/addSensor`
+ Obtener Sensor (Metodo GET): `/api/getSensor/<company_api_key>/<sensor_id>`
+ Obtener sensores (Metodo GET): `/api/getSensors/<company_api_key>/<location_id>`
+ Cambiar sensor (Metodo PUT): `/api/updateSensor`
+ Borrar sensor (Metodo DELETE): `/api/deleteSensor`


## Datos del sensor
+ Datos del sensor (Metodo POST): `/api/sensorData`
+ Obtener datos del sensor (Metodo GET): `/api/getSensorData/<company_api_key>/from/<time1>/to/<time2>/<sensor_id>/`
+ Cambiar datos del sensor (Metodo PUT): `/api/updateSensorData`
+ Cambiar datos del sensor (Metodo DELETE): `/api/deleteSensorData`




