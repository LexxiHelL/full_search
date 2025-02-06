import sys
from geocode import get_coord, get_ll_span
from viewmap import view_map


def main():
    toponym_to_find = ' '.join(sys.argv[1:])

    if toponym_to_find:
        lat, lon = get_coord(toponym_to_find)
        ll_spn = f'll={lat},{lon}&spn=0.005,0.005'
        view_map(ll_spn, 'map')

        ll, spn = get_ll_span(toponym_to_find)
        ll_spn = f'll={ll}&spn={spn}'
        view_map(ll_spn, 'map')

        poit_param = f'pt={ll}'
        view_map(ll_spn, 'map', add_params=poit_param)
    else:
        print('No param')


if __name__ == '__main__':
    main()
