places = ['Albania', 'Switzerland' ,'France', 'Spain', 'Italy', 'England', 'Cyprus', 'Turkey', 'Germany', 'Poland', 'Neterlands' ]
print (places)
message = 'Last country which i visited was ' + places[7] + '!'
print (message)
places[2] = 'Egypt'
print(places)
places.append ('Luxembourg')
print(places)
del places[7]
last_country=places.pop()
print (last_country)
places.sort()
print (places)
places.sort(reverse=True)
print (places)
number_country=len(places)
print (number_country)
