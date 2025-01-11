first_names = ['Olga', 'Blanka', 'Remigiusz', 'Katarzyna', 'Kacper']
last_names = ['Tokarczuk', 'Lipińska', 'Mróz', 'Bonda']

# metoda Zip służy do łączenia elementów pomiędzy dwoma tablicami/listam, tworząc pomiędzy tymi dowma elementami tuplę/krotkę.

print(list(zip(first_names, last_names)))

# first_name, last_name = ('Olga', 'Tokarczuk')

# print(first_name)
# print(last_name)

for first_name, last_name in zip(first_names, last_names):
    print(first_name, last_name)

# Zbiory w Pythonie nie są iterowane

