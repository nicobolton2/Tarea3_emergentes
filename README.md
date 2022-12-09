# Arquitecturas Emergentes flask sqlite

## Resumen de rutas:
##### Ruta principal
`http://35.153.241.7:5000/`

##### Ruita de inicio:
`/` 

##### Ruta de login `username = admin`, `password = admin` por defecto
`'/login', methods=['POST']`      

## Compañia
#### Agregar compañia 
`'/api/addCompany', methods=['POST']`

## Ubicación
#### Agregar locación
`'/api/addLocation', methods=['POST']`
#### Obtener ubicación
`'/api/getLocation/<company_api_key>/<location_id>', methods=['GET']`
#### Obtener ubicaciones
`'/api/getLocations/<company_api_key>', methods=['GET']`
#### Cambiar ubicación
`'/api/updateLocation', methods=['PUT']`
#### Borrar ubicación
`'/api/deleteLocation', methods=['DELETE']`

## Sensor
#### Agregar sensor
`'/api/addSensor', methods=['POST']`
#### Obtener Sensor
`'/api/getSensor/<company_api_key>/<sensor_id>', methods=['GET']`
#### Obtener sensores
`'/api/getSensors/<company_api_key>/<location_id>', methods=['GET']`
#### Cambiar sensor 
`'/api/updateSensor', methods=['PUT']`
#### Borrar sensor 
`'/api/deleteSensor', methods=['DELETE']`


## Datos del sensor
#### Datos del sensor
`'/api/sensorData', methods=['POST']`
#### obtener datos del sensor
`'/api/getSensorData/<company_api_key>/from/<time1>/to/<time2>/<sensor_id>/', methods=['GET']`
#### Cambiar datos del sensor
`'/api/updateSensorData', methods=['PUT']`
#### Cambiar datos del sensor
`'/api/deleteSensorData', methods=['DELETE']`




