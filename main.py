from requests import get
from json import loads
from terminaltables import AsciiTable

url = 'https://danepubliczne.imgw.pl/api/data/synop'
response = get(url)


def cities():
    cities = [row['stacja'] for row in loads(response.text)]
    return cities


def main(city):
    rows = [
        ['Miasto', 'Data', 'Godzina', 'Temperatura', 'Opady', 'Cisnienie']
    ]
    for row in loads(response.text):
        if row['stacja'] == city:
            rows.append([
                row['stacja'], row['data_pomiaru'], row['godzina_pomiaru'], row['temperatura'], row['suma_opadu'], row['cisnienie']
            ])

    table = AsciiTable(rows)
    print(table.table)


if __name__ == "__main__":
    quit = 'Y'
    cities = {index: city for index, city in enumerate(cities())}
    while quit.upper() == 'Y':
        city = int(input(f'Choose city: {cities}'))
        main(cities[city])
        quit = input('Again? [Y]es [N]o\n')
