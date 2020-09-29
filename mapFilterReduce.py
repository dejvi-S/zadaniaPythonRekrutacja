nazwiska = ['jan kot', 18, 'ANNA KRÓL', 'jÓzef BYK',
['nie', 'wasza','sprawa'], 'ROBERT wąŻ']
filtered = list(filter(lambda x: type(x) is str ,nazwiska))
print(filtered)

nazwiska = list(map(lambda s: s.capitalize(), filtered))

print(nazwiska)