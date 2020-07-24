from requests import get
from json import loads
from terminaltables import AsciiTable


cities = ['Wrocław']


def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows = [
        ['Miasto', 'Data', 'Godzina', 'Temperatura', 'Opady', 'Cisnienie']
    ]
    for row in loads(response.text):
        if row['stacja'] in cities:
            rows.append([
                row['stacja'], row['data_pomiaru'], row['godzina_pomiaru'], row['temperatura'], row['suma_opadu'], row['cisnienie']
            ])

    table = AsciiTable(rows)
    print(table.table)


if __name__ == "__main__":
    main()
