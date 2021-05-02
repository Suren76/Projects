import json

sensor_get_data = json.load(open("../Projects/DigiCode_Weather/sensor_data.json"))

print(sensor_get_data, type(sensor_get_data))

for i in range(len(sensor_get_data['date'])):
        print(i)
        print(sensor_get_data['temp'][i],sensor_get_data['humidity'][i], sensor_get_data['date'][i])