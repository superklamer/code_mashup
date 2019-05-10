import socketio, json, sys
from py4j.java_gateway import JavaGateway
from java_gateway import _JavaGateway

# https://github.com/miguelgrinberg/python-socketio/blob/master/examples/client/asyncio/latency_client.py

sio = socketio.Client()

def connect_gateway():
    gateway = _JavaGateway()
    gateway.entry_point.getMonDb().setMongoCollection("Weather", "Cities")
    return gateway

def get_weather():
    print('in get_weather')
    gateway = connect_gateway()
    weather_data = gateway.entry_point.getLastDocument()
    weather_data_json = gateway.entry_point.convertDocToJson(weather_data)
    #print(weather_data_json)
    return weather_data_json

def request_updated_weather(id):
    gateway = connect_gateway()
    gateway.entry_point.setId(id)
    weather_data = gateway.entry_point.getUpdatedWeather()
    weather_data_json = gateway.entry_point.convertDocToJson(weather_data)
    return weather_data_json


def update_indoor_data(data):
    #3print('data received from raspberry: ', data)
    if data:
        data_to_str = json.dumps(data)
        data_to_json = json.loads(data_to_str)
        indoor = data_to_json
        #print('json converted data: ', indoor)
        #print('indoor is now', indoor)
        on_new_indoor_data(indoor)


@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

@sio.on('weather_data')
def on_weather_data():
    print('in weather_data')
    weather = get_weather()
    sio.emit('weather', weather)

@sio.on('update_weather')
def on_update_weather():
    print('in update_weather')
    on_weather_data()

@sio.on('pull_new_weather')
def on_pull_new_weather(id):
    weather = request_updated_weather(id)
    sio.emit('weather', weather)

@sio.on('new_indoor_data')
def on_new_indoor_data(data):
    print('Indoor data-sending to node')
    print('data sending: ', data)
    sio.emit('update_indoor', data)

def start_server():
    sio.connect('http://localhost:3000')
    sio.wait()


if __name__ == '__main__':
    start_server()
    sys.stdout.flush()




