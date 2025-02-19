import requests


def find_businesss(ll, spn, request, locale="ru_RU"):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
    search_params = {
        "apikey": api_key,
        "text": request,
        "lang": locale,
        "ll": ll,
        "spn": spn,
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)

    json_response = response.json()
    organizations = json_response["features"]
    return organizations


def find_business(ll, spn, request, locale="ru_RU"):
    orgs = find_businesss(ll, spn, request, locale=locale)
    if len(orgs):
        return orgs[1]