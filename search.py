import sys
from geocode import get_coord
from viewmap import view_map
from business import find_business
from distance import find_distance


def main():
    toponym_to_find = ' '.join(sys.argv[1:])

    lat, lon = get_coord(toponym_to_find)
    address_ll = f'{lat},{lon}'
    span = '0.005,0.005'
    organization = find_business(address_ll, span, 'аптека')
    point = organization['geometry']['coordinates']
    org_lat = float(point[0])
    org_lon = float(point[1])
    point_param = f'pt={org_lat},{org_lon},pm2gl'
    points_param = point_param + f'~{address_ll},pm2rdl'
    view_map(map_type="map", add_params=points_param)
    name = organization["properties"]["CompanyMetaData"]["name"]
    address = organization["properties"]["CompanyMetaData"]["address"]
    time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
    distance = round(find_distance((lon, lat), (org_lon, org_lat)))

    snippet = f"Название:\t{name}\nАдрес:\t{address}\nВремя работы:\t{time}\n" \
              f"Расстояние:\t{distance}м."
    print(snippet)


if __name__ == "__main__":
    main()
