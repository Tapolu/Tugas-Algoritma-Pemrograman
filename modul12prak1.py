import pandas as pd

data = {
    "Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", "Rusia", "Meksiko", "Nigeria", "Jerman", "Aljazair", "Inggris"],
    "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brazilia", "Moskow", "Meksiko City", "Abuja", "Berlin", "Aljazair", "London"],
    "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia", "Amerika", "Afrika", "Eropa", "Afrika", "Eropa"],
    "Luas": [1905, 377, 3287, 9597, 9834, 8515, 17098, 1964, 923, 357, 2381, 242],
    "Populasi": [264, 143, 1252, 1357, 329, 210, 146, 126, 200, 83, 43, 66]
}

df = pd.DataFrame(data)

print("Berikut Data Framenya:")
print(df.set_index(['Negara', 'Ibu Kota', 'Benua']))

grouped_stats = df.groupby(['Benua']).agg({'Luas': ['mean', 'std'], 'Populasi': ['mean', 'std']}).round(2)

print("\nBerikut Data Mean:")
print(grouped_stats['Luas']['mean'].rename('Luas Mean').to_frame().join(grouped_stats['Populasi']['mean'].rename('Populasi Mean')))

print("\nBerikut Data Standard Deviation:")
print(grouped_stats['Luas']['std'].rename('Luas Std').to_frame().join(grouped_stats['Populasi']['std'].rename('Populasi Std')))
