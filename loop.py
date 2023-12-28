# Pętla for w języku Python służy do iterowania po sekwencjach lub innych obiektach iterowalnych.

# Napisz program, który znajdzie wszystkie liczby dwucyfrowe podzielne przez 11.
import re
numbers = []

for num in range(1, 100):
    if num % 11 == 0:
        numbers.append(num)

print(', '.join(map(str, numbers)))

print('---')

# Napisz program, który znajdzie wszystkie liczby dwucyfrowe podzielne przez 11 oraz niepodzielne przez 3
number_check_two = []

for num in range(1, 100):
    if num % 11 == 0 and num % 3 != 0:
        number_check_two.append(num)

print(", ".join(map(str, number_check_two)))

print('---')

# Napisz program, który usunie liczby nieparzyste i zwróci pozostałe.
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
new_items = []

for ele in items:
    if ele % 2 == 0:
        new_items.append(ele)

print(new_items)

print('---')

# Napisz program, który usunie duplikaty z tej listy (kolejność musi zostać zachowana).
# Usuwanie duplikatów
items_duple = [1, 5, 3, 2, 2, 4, 2, 4]
new_item = []

for item in items_duple:
    if item not in new_item:
        new_item.append(item)

print(new_item)

print('---')

# Napisz program, który z podanego tekstu,
# wytnie dokładnie cztery pierwsze wyrazy.
# Przeprowadź standaryzację każdego wyrazu, tzn. zamień duże litery na małe. Wynik przedstaw w postaci listy
text = 'Python jest bardzo popularnym językiem programowania'
my_text_list = text.lower().split()[:4]

print(my_text_list)

print('---')

# Napisz program, który z podanej listy zwróci listę wartości powyżej ustalonego progu równego 0.5
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

probabilitiesHigh = [num for num in probabilities if num > 0.5]
print(probabilitiesHigh)

print('---')


# Napisz program, który przypisze klasę 0
# dla wartości mniejszych niż 0.5 oraz 1 dla wartości większych lub równych 0.5.
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

check_probabilities = [0 if num < 0.5 else 1 for num in probabilities]

print(check_probabilities)

print('---')

# Przekształcenie listy na słownik i zliczeń liczby wystąpień
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
item_set = dict(enumerate(items))

count_item_set = {}

for value in item_set.values():
    if value in count_item_set:
        count_item_set[value] += 1
    else:
        count_item_set[value] = 1

print(count_item_set)

print('---')

"""
Utwórz listę słów z podanego tekstu. Następnie dokonaj standaryzacji tekstu. Wykonaj poniższe kroki:
    zamień duże litery na małe
    usuń znaki interpunkcyjne
    wyodrębnij tylko wyrazy z długością powyżej 11 znaków
"""

text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""

text_list = text.split()
new_text_list = []

for text in text_list:
    text.lower()
    if len(text) > 11:
        new_text_list.append(text)

print(new_text_list)

print('---')

# Dokonaj iteracji po liście indexes oraz
# wydrukuj do konsoli tylko te indeksy, które zwierają w nazwie '20' lub '30'.
indexes = [
    'WIG',
    'WIG-banki',
    'WIG-budownictwo',
    'WIG-CEE',
    'WIG-chemia',
    'WIG-energia',
    'WIG-ESG',
    'WIG-górnictwo',
    'WIG-informatyka',
    'WIG-leki',
    'WIG-media',
    'WIG-motoryzacja',
    'WIG-nieruchomości',
    'WIG-odzież',
    'WIG-paliwa',
    'WIG-Poland',
    'WIG-spożywczy',
    'WIG-telekomunikacja',
    'WIG-Ukraine',
    'WIG.GAMES',
    'WIG.MS-BAS',
    'WIG.MS-FIN',
    'WIG.MS-PET',
    'WIG20',
    'WIG20dvp',
    'WIG20lev',
    'WIG20short',
    'WIG20TR',
    'WIG30',
    'WIG30TR',
    'WIGdiv',
    'WIGtech',
]

for inx in indexes:
    if '20' in inx or '30' in inx:
        print(inx)


print('---')

# Wydrukuj kody (tickery) tylko tych spółek,
# których cena zamknięcia jest większa niż 100.00 PLN.
gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

high_gaming = {}

for gam, value in gaming.items():
    if value > 100:
        high_gaming[gam] = value

for key in high_gaming.keys():
    print(key)

print('---')

# Sprawdź, czy każde imię jest poprawne (składa się tylko z liter).
# Jeżeli tak, wynik wydrukuj do konsoli w następującej postaci, np. Hello Jack!
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
number = r'\d'
only_name = []

for name in names:
    numer_find = re.findall(number, name)
    if numer_find:
        print(name)
    else:
        only_name.append(name)

for name in only_name:
    print(f"Hello {name}!")

print('---')

# obliczyć całkowity koszt wszystkich lotów podczas podróży klienta - miast z listy cities
cities = ['Paris', 'Rome', 'Barcelona', 'Berlin']

flight_prices = {
    'Paris': 350,
    'Rome': 450,
    'Barcelona': 300,
    'Amsterdam': 250,
    'Berlin': 400
}

your_cities = {}

for name in cities:
    if name in flight_prices:
        your_cities[name] = flight_prices[name]
    else:
        print(f"Ten usunąć {name}")

total_price = sum(your_cities.values())
print(f"Total cost of flights: $ {total_price}.")

print('---')

# Przporządkuj do danej osoby stopień wojskowy
soldiers = ['John', 'Mike', 'Sarah', 'Kim', 'Tom']

rankings = {
    'John': 'Captain',
    'Mike': 'Private',
    'Kim': 'Lieutenant',
    'Tom': 'Major'
}

soliders_rank = {}

for name in soldiers:
    if name not in rankings:
        soliders_rank[name] = 'no ranking'
    else:
        soliders_rank[name] = rankings[name]


for nameSolider in soliders_rank:
    if soliders_rank[nameSolider] == 'no ranking':
        print(f"{nameSolider} has {soliders_rank[nameSolider]}")
    else:
        print(f"{nameSolider} is a {soliders_rank[nameSolider]}")

print('---')
# Oblicz całkowitą energię wygenerowaną przez panel słoneczny w ciągu całego dnia
# biorąc pod uwagę fakt, że wartości mniejsze niż 0.5 nie są wliczane do wynik
energy_output = [
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0,
    0.9,
    0.8,
    0.7,
    0.6,
    0.5,
    0.4,
]

energySum = []

for energy in energy_output:
    if energy >= 0.5:
        energySum.append(energy)
sumEnergySum = sum(energySum)
formatedSumEnergySum = "{:.2f}".format(sumEnergySum)

print(f"Total energy generated: {formatedSumEnergySum}")

print('---')

# Oblicz całkowitą energię wygenerowaną przez instalację paneli słonecznych w ciągu całego dnia
energy_output = [
    [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4],
    [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5],
    [0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],
]

energyAll = [energy_output[0], energy_output[1], energy_output[2]]
sumEnergy = []

for energy in energyAll:
    sumEnergy.append(sum(energy))

print(f"Total energy generated: {sum(sumEnergy)}")

print('---')

# Oblicz sumę scored dla poszczególnego gracza
points = [
    {'player': 'Alice', 'scored': 5},
    {'player': 'Bob', 'scored': 7},
    {'player': 'Charlie', 'scored': 3},
    {'player': 'Alice', 'scored': 2},
    {'player': 'Bob', 'scored': 4},
    {'player': 'Charlie', 'scored': 6},
    {'player': 'Alice', 'scored': 3},
    {'player': 'Bob', 'scored': 8},
    {'player': 'Charlie', 'scored': 1},
]

aliceScore = 0
bobScore = 0
charlieScore = 0

for point in points:
    if point['player'] == 'Alice':
        aliceScore += point['scored']

    if point['player'] == 'Bob':
        bobScore += point['scored']
    
    if point['player'] == 'Charlie':
        charlieScore += point['scored']

print(f"Alice - {aliceScore} points.")
print(f"Bob - {bobScore} points.")
print(f"Charlie - {charlieScore} points.")

print('---')

#     oblicz liczbę lotów opóźnionych
#     średni czas opóźnienia lotu

flights = [
    {
        'flight_num': 'AA123',
        'origin': 'LAX',
        'destination': 'JFK',
        'delay_minutes': 12,
    },
    {
        'flight_num': 'BB456',
        'origin': 'ORD',
        'destination': 'LAX',
        'delay_minutes': 0,
    },
    {
        'flight_num': 'CC789',
        'origin': 'JFK',
        'destination': 'ORD',
        'delay_minutes': 32,
    },
    {
        'flight_num': 'AA321',
        'origin': 'LAX',
        'destination': 'ORD',
        'delay_minutes': 6,
    },
    {
        'flight_num': 'BB654',
        'origin': 'JFK',
        'destination': 'LAX',
        'delay_minutes': 18,
    },
    {
        'flight_num': 'CC987',
        'origin': 'ORD',
        'destination': 'JFK',
        'delay_minutes': 24,
    },
]

flights_count = []

for flight in flights:
    if flight['delay_minutes'] > 0:
        flights_count.append(flight)

total_minutes = sum(flight['delay_minutes'] for flight in flights_count)
avg_flight = "{:.2f}".format(total_minutes / len(flights_count))

print(f"Total number of delayed flights: {len(flights_count)}")

print(f"Average delay time: {avg_flight} minutes")

print('---')

# Oblicz wygenerowany dzienny przychód dla każdego sprzedanego produktu. 
sales = [
    {'product_id': 1, 'quantity': 3, 'price': 10.99},
    {'product_id': 2, 'quantity': 1, 'price': 34.99},
    {'product_id': 1, 'quantity': 2, 'price': 10.99},
    {'product_id': 3, 'quantity': 5, 'price': 5.99},
    {'product_id': 2, 'quantity': 2, 'price': 34.99},
    {'product_id': 1, 'quantity': 1, 'price': 10.99},
]


priceProductOne = 0
priceProductOneSecond = 0
priceProductOneThird = 0



priceProdutTwo = 0
priceProdutTwoSecond = 0
priceProductTwoThird = 0


priceProductThree = 0
priceProdutThreeSecond = 0
priceProductThreeThird = 0

# -- zliczenie ilości oraz ceny dla każdeo produktu ID
for sale in sales:
    if sale['product_id'] == 1 and sale['quantity'] == 1:
        priceProductOne += sale['price']
    if sale['product_id'] == 1 and sale['quantity'] == 2:
        priceProductOneSecond += sale['price']
    if sale['product_id'] == 1 and sale['quantity'] == 3:
        priceProductOneThird += sale['price']
    if sale['product_id'] == 2 and sale['quantity'] == 1:
        priceProdutTwo += sale['price']
    if sale['product_id'] == 2 and sale['quantity'] == 2:
        priceProdutTwoSecond += sale['price']
    if sale['product_id'] == 2 and sale['quantity'] == 3:
        priceProductTwoThird += sale['price']
    if sale['product_id'] == 3 and sale['quantity'] == 5:
        priceProductThree += sale['price']
 

print(f"Product 1 generated ${(1 * priceProductOne) + (2 * priceProductOneSecond) + (3 * priceProductOneThird)} in revenue")
print(f"Product 2 generated ${(1 * priceProdutTwo) + (2 * priceProdutTwoSecond) + (3 * priceProductTwoThird)} in revenue")
print(f"Product 3 generated ${'{:.2f}'.format(5 * priceProductThree)} in revenue")
                                                            
print('---')

cars = [
    {
        'model': 'Sedan',
        'parts': [
            'engine',
            'transmission',
            'chassis',
            'wheels',
        ],
        'cost': 20000,
    },
    {
        'model': 'SUV',
        'parts': [
            'engine',
            'transmission',
            'chassis',
            'wheels',
            'air conditioning',
            'infotainment system',
        ],
        'cost': 35000,
    },
    {
        'model': 'Hatchback',
        'parts': [
            'engine',
            'transmission',
            'chassis',
            'wheels',
            'air conditioning',
        ],
        'cost': 25000,
    },
    {
        'model': 'Pickup Truck',
        'parts': [
            'engine',
            'transmission',
            'chassis',
            'wheels',
            'towing package',
            'bed liner',
        ],
        'cost': 40000,
    },
]

modelCars = []

for model in cars:
    modelCars.append(model['model'])

