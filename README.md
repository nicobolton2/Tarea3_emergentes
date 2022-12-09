# Arquitecturas Emergentes flask sqlite



`http://35.153.241.7:5000/`

Resumen de rutas:

`/` = ruita de inicio

`'/login', methods=['POST']`      ruta para entrar como administrador

`'/api/addCompany', methods=['POST']`

`'/api/addLocation', methods=['POST']`

`'/api/getLocation/<company_api_key>/<location_id>', methods=['GET']`

`'/api/getLocations/<company_api_key>', methods=['GET']`

`'/api/updateLocation', methods=['PUT']`

`'/api/deleteLocation', methods=['DELETE']`

`'/api/addSensor', methods=['POST']`

`'/api/getSensor/<company_api_key>/<sensor_id>', methods=['GET']`

`'/api/getSensors/<company_api_key>/<location_id>', methods=['GET']`

`'/api/updateSensor', methods=['PUT']`

`'/api/deleteSensor', methods=['DELETE']`

`'/api/sensorData', methods=['POST']`

`'/api/getSensorData/<company_api_key>/from/<time1>/to/<time2>/<sensor_id>/', methods=['GET']`

`'/api/updateSensorData', methods=['PUT']`

`'/api/deleteSensorData', methods=['DELETE']`




