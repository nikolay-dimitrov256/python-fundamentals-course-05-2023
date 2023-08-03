countries = input().split(', ')
capitals = input().split(', ')

# capitals_dict = {countries[i]: capitals[i] for i in range(len(countries))}
capitals_dict = dict(zip(countries, capitals))

for country, capital in capitals_dict.items():
    print(f'{country} -> {capital}')
