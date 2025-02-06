import requests


def get_coord(address):  # координаты объекта на карте
    server_address = 'http://geocode-maps.yandex.ru/1.x/?'
    api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
    geocoder_request = f'{server_address}apikey={api_key}&geocode={address}&format=json'

    response = requests.get(geocoder_request)
    if response:
        response_json = response.json()
        toponym = response_json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        coord = toponym['Point']['pos']
        print(coord)
        x, y = coord.split(' ')
        return float(x), float(y)


def get_ll_span(address):  # отмасштабированная карта
    server_address = 'http://geocode-maps.yandex.ru/1.x/?'
    api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
    geocoder_request = f'{server_address}apikey={api_key}&geocode={address}&format=json'

    response = requests.get(geocoder_request)
    if response:
        response_json = response.json()
        toponym = response_json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    if not toponym:
        return (None, None)

    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    ll = ",".join([toponym_longitude, toponym_lattitude])

    envelope = toponym["boundedBy"]["Envelope"]

    l, b = envelope["lowerCorner"].split(" ")
    r, t = envelope["upperCorner"].split(" ")

    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0

    span = f"{dx},{dy}"

    return ll, span
