from flask import Flask, request, jsonify
from DataBase import Admin, Company, Location, Sensor, SensorData, db
from init import create_app
import time
app= create_app()
#inicio
@app.route('/')
def init():
    return "Bienvenido, para más informacion sobre rutas, entrar a https://github.com/"

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data= request.get_json()
        username= data['username']
        password= data['password']
        admin = Admin.query.filter_by(Username=username, Password=password).first()
        if admin:
            return jsonify({'message': 'Welcome'})
    return jsonify({'message': 'Error'})

##compañia

@app.route('/api/addCompany', methods=['POST'])
def addCompany():
    data = request.get_json()
    company_name = data['company_name']
    company_api_key = data['company_api_key']
    user = data['username']
    password = data['password']

    admin = Admin.query.filter_by(Username=user, Password=password).first()
    
    if admin:
        company = Company.query.filter_by(company_name=company_name).first()
        if company:
            return jsonify({
                'message': 'Nueva compañia agragada con exito'
            })
        else:   
            # console log
            print(company_name, company_api_key)
            company = Company(company_name=company_name, company_api_key=company_api_key)

            db.session.add(company)
            db.session.commit()
            return jsonify({
                'message': 'Nueva compañia agragada con exito',
            })

@app.route('/api/addLocation', methods=['POST'])
def addLocation():
    data = request.get_json()
    company_id = data['company_id']
    location_name = data['location_name']
    location_country= data['location_country']
    location_city = data['location_city']
    location_meta = data['location_meta']
    user = data['user']
    password = data['password']
    
    admin = Admin.query.filter_by(Username=user, Password=password).first()
    
    if admin:
        location = Location.query.filter_by(location_name=location_name).first()
        if location:
            return jsonify({
                'message': 'Nueva locacion agregada con exito'
            })
        else:   
            # console log
            print(company_id, location_name, location_country, location_city, location_meta)
            location = Location(company_id=company_id, location_name=location_name, location_country=location_country, location_city=location_city, location_meta=location_meta)
            location.save()
            return jsonify({
                'message': 'Nueva locacion agregada con exito',
            })

@app.route('/api/getLocation/<company_api_key>/<location_id>', methods=['GET'])
def getLocation(company_api_key, location_id):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        location = Location.query.filter_by(ID=location_id).first()
        print(location)
        if location:
    
            print(company_api_key, location_id)
            return jsonify({
                'location': location.to_json()
            })
    return jsonify({
        'message': 'Error'
    })
        
@app.route('/api/getLocations/<company_api_key>', methods=['GET'])
def getLocations(company_api_key):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        locations = Location.query.filter_by(company_id=company.ID).all()
        return jsonify({
            'locations': [location.to_json() for location in locations]
        })
    return jsonify({
        'message': 'Error'
    })

@app.route('/api/updateLocation', methods=['PUT'])
def updateLocation():
    data = request.get_json()
    location_id = data['location_id']
    company_api_key = data['company_api_key']
    location_name = data['location_name']
    location_country = data['location_country']
    location_city = data['location_city']
    location_meta = data['location_meta']

    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        location = Location.query.filter_by(ID=location_id).first()
        if location:
            location.location_name = location_name
            location.location_country = location_country
            location.location_city = location_city
            location.location_meta = location_meta
            db.session.commit()
            return jsonify({
                'message': 'Locacion cambiada con exito'
            })
        else:
            return jsonify({
                'message': 'Error'
            })
    return jsonify({
        'message': 'Error'
    })
        
@app.route('/api/deleteLocation', methods=['DELETE'])
def deleteLocation():
    data = request.get_json()
    location_id = data['location_id']
    company_api_key = data['company_api_key']

    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        location = Location.query.filter_by(ID=location_id).first()
        if location:
            db.session.delete(location)
            db.session.commit()
            return jsonify({
                'message': 'Locacion borrada con exito'
            })
        else:
            return jsonify({
                'message': 'Error'
            })
    return jsonify({
        'message': 'Error'
    })        
        
        
##Sensores        

@app.route('/api/addSensor', methods=['POST'])
def addSensor():
    data = request.get_json()
    location_id = data['location_id']
    sensor_name = data['sensor_name']
    sensor_category = data['sensor_category']
    sensor_meta = data['sensor_meta']
    sensor_api_key = data['sensor_api_key']
    user = data['user']
    password = data['password']
    
    admin = Admin.query.filter_by(Username=user, Password=password).first()    
    
    if admin: 
        print(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
        sensor = Sensor(location_id=location_id, sensor_name=sensor_name, sensor_category=sensor_category, sensor_meta=sensor_meta, sensor_api_key=sensor_api_key)
        sensor.save()
        return jsonify({
            'message': 'Sensor creado con exito',
        })
    return jsonify({
        'message': 'Error'
    })

@app.route('/api/getSensor/<company_api_key>/<sensor_id>', methods=['GET'])
def getSensor(company_api_key, sensor_id):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        sensor = Sensor.query.filter_by(sensor_id=sensor_id).first()
        return jsonify({
            'sensor': sensor.to_json()
        })
    return jsonify({
        'message': 'Error'
    })

@app.route('/api/getSensors/<company_api_key>/<location_id>', methods=['GET'])
def getSensors(company_api_key, location_id):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        sensors = Sensor.query.filter_by(location_id=location_id).all()
        return jsonify({
            'sensors': [sensor.to_json() for sensor in sensors]
        })
    return jsonify({
        'message': 'Error'
    })

@app.route('/api/updateSensor', methods=['PUT'])
def updateSensor():
    data = request.get_json()
    sensor_id = data['sensor_id']
    company_api_key = data['company_api_key']
    sensor_name = data['sensor_name']
    sensor_category = data['sensor_category']
    sensor_meta = data['sensor_meta']
    sensor_api_key = data['sensor_api_key']

    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        sensor = Sensor.query.filter_by(sensor_id=sensor_id).first()
        if sensor:
            sensor.sensor_name = sensor_name
            sensor.sensor_category = sensor_category
            sensor.sensor_meta = sensor_meta
            sensor.sensor_api_key = sensor_api_key
            db.session.commit()
            return jsonify({
                'message': 'Sensor cambiado con exito'
            })
        else:
            return jsonify({
                'message': 'Error'
            })
    return jsonify({
        'message': 'Error'
    })

@app.route('/api/deleteSensor', methods=['DELETE'])
def deleteSensor():
    data = request.get_json()
    sensor_id = data['sensor_id']
    company_api_key = data['company_api_key']

    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        sensor = Sensor.query.filter_by(sensor_id=sensor_id).first()
        if sensor:
            db.session.delete(sensor)
            db.session.commit()
            return jsonify({
                'message': 'Sensor borrado con exito'
            })
    return jsonify({
        'message': 'Error'
    })

##Sensor Data

@app.route('/api/sensorData', methods=['POST'])
def sensorData():
    data = request.get_json()
    sensor_api_key = data['sensor_api_key']
    temperatura = data['temperatura']

    sensor = Sensor.query.filter_by(sensor_api_key=sensor_api_key).first()
    if sensor:
        date =time.time()
        date = int(date)
        sensor_data = SensorData(sensor_id = sensor.sensor_id, temperatura = temperatura, date=date)
        sensor_data.save()
        return jsonify({
            'message': 'Informacion del sensor agregada con exito'
        })
    return jsonify({
        'message': 'Error'
    })

@app.route('/api/getSensorData/<company_api_key>/from/<time1>/to/<time2>/<sensor_id>/', methods=['GET'])
def getSensorData(company_api_key, time1, time2, sensor_id):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        data=[]
        for sensor in sensor_id.split(','):
            sensor = Sensor.query.filter_by(sensor_id=sensor).first()
            if sensor:
                sensordata = SensorData.query.filter_by(sensor_id = sensor.sensor_id).all()
                for i in sensordata:
                    if i.date >= int(time1) and i.date <= int(time2):
                        data.append(i.to_json())
        return jsonify({
            'data': data
        })
    return jsonify({
        'message': 'Error'
    })

@app.route('/api/updateSensorData', methods=['PUT'])
def updateSensorData():
    data = request.get_json()
    sensor_api_key = data['sensor_api_key']
    sensor_data = data['sensor_data']
    sensor_data_id = data['sensor_data_id']

    sensor = Sensor.query.filter_by(sensor_api_key=sensor_api_key).first()
    if sensor:
        sensordata = SensorData.query.filter_by(sensor_data_id=sensor_data_id).first()
        if sensordata:
            sensordata.data = sensor_data
            db.session.commit()
            return jsonify({
                'message': 'Informacion del sensor cambiada con exito'
            })
    return jsonify({
        'message': 'Error'
    })

@app.route('/api/deleteSensorData', methods = ['DELETE'])
def deleteSensorData():
    data = request.get_json()
    sensor_api_key = data['sensor_api_key']
    sensor_data_id = data['sensor_data_id']

    sensor = Sensor.query.filter_by(sensor_api_key=sensor_api_key).first()
    if sensor:
        sensordata = SensorData.query.filter_by(sensor_data_id=sensor_data_id).first()
        if sensordata:
            db.session.delete(sensordata)
            db.session.commit()
            return jsonify({
                'message': 'informacion del sensor borrada con exito'
            })
    return jsonify({
        'message': 'Error'
    })

app.run()