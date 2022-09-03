# CHAPTER 3

## Ex 3-1


~~~
names = ['Friend1', 'Friend2', 'Friend3']
print(names[0]) 
print(names[1]) 
print(names[2]) 

~~~
~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/names3-1.py
Friend1
Friend2
Friend3
~~~

## Ex 3-2

~~~
names = ['Friend1', 'Friend2', 'Friend3']
print ('Hello, ' + (names[0]) + '. Please, call me!')
print ('Hello, ' + (names[1]) + '. Please, call me!')
print ('Hello, ' + (names[2]) + '. Please, call me!')
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/names3-2.py
Hello, Friend1. Please, call me!
Hello, Friend2. Please, call me!
Hello, Friend3. Please, call me!
~~~

## Ex 3-3

~~~
cars = ['VAZ', 'Audi', 'Fiat', 'Ford']
message = "I would like to buy " + cars[3].title() + " soon."
print(message)
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/cars3-3.py
I would like to buy Ford soon.
~~~

## Ex 3-4

~~~
guests = ['DelPiero', 'Biden', 'putin']
print ("Welcome, " + (guests[0]) + " to dinner-party!")
print ("Welcome, " + (guests[1]) + " to dinner-party!")
print ("Welcome, " + (guests[2]) + " to hell-party!")
~~~

~~~
gk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/guests3-4.py
Welcome, DelPiero to dinner-party!
Welcome, Biden to dinner-party!
Welcome, putin to hell-party!
~~~

## Ex 3-5

~~~
guests = ['DelPiero', 'Biden', 'putin']
print ("Welcome, " + (guests[0]) + " to dinner-party!")
print ("Welcome, " + (guests[1]) + " to dinner-party!")
print ("Welcome, " + (guests[2]) + " to hell-party!")
guests[2] = 'patrushev'
print ("Welcome, " + (guests[0]) + " to dinner-party!")
print ("Welcome, " + (guests[1]) + " to dinner-party!")
print ("Welcome, " + (guests[2]) + " to hell-party!")
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/guests3-5.py
Welcome, DelPiero to dinner-party!
Welcome, Biden to dinner-party!
Welcome, putin to hell-party!
Welcome, DelPiero to dinner-party!
Welcome, Biden to dinner-party!
Welcome, patrushev to hell-party!
~~~

## Ex 3-6

~~~
guests = ['DelPiero', 'Biden', 'putin']
print ("Welcome, " + (guests[0]) + " to dinner-party!")
print ("Welcome, " + (guests[1]) + " to dinner-party!")
print ("Welcome, " + (guests[2]) + " to hell-party!")
guests[2] = 'patrushev'
print ("Welcome, " + (guests[0]) + " to dinner-party!")
print ("Welcome, " + (guests[1]) + " to dinner-party!")
print ("Welcome, " + (guests[2]) + " to hell-party!")
print ('Our party will be bigger!')
guests.insert(0, 'Zelenskiy')
guests.insert(2, 'Zaluzhnyy')
guests.append('Arestovych')
print ("Welcome, " + (guests[0]) + " to dinner-party!")
print ("Welcome, " + (guests[1]) + " to dinner-party!")
print ("Welcome, " + (guests[2]) + " to dinner-party!")
print ("Welcome, " + (guests[3]) + " to dinner-party!")
print ("Welcome, " + (guests[4]) + " to hell-party!")
~~~

~~~
gk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/guests3-6.py
Welcome, DelPiero to dinner-party!
Welcome, Biden to dinner-party!
Welcome, putin to hell-party!
Welcome, DelPiero to dinner-party!
Welcome, Biden to dinner-party!
Welcome, patrushev to hell-party!
Our party will be bigger!
Welcome, Zelenskiy to dinner-party!
Welcome, DelPiero to dinner-party!
Welcome, Zaluzhnyy to dinner-party!
Welcome, Biden to dinner-party!
Welcome, patrushev to hell-party!
~~~

## Ex 3-7

~~~
guests = ['DelPiero', 'Biden', 'putin']
print ("Welcome, " + (guests[0]) + " to dinner-party!")
print ("Welcome, " + (guests[1]) + " to dinner-party!")
print ("Welcome, " + (guests[2]) + " to hell-party!")
guests[2] = 'patrushev'
print ("Welcome, " + (guests[0]) + " to dinner-party!")
print ("Welcome, " + (guests[1]) + " to dinner-party!")
print ("Welcome, " + (guests[2]) + " to hell-party!")
print ('Our party will be bigger!')
guests.insert(0, 'Zelenskiy')
guests.insert(2, 'Zaluzhnyy')
guests.append('Arestovych')
print ("Welcome, " + (guests[0]) + " to dinner-party!")
print ("Welcome, " + (guests[1]) + " to dinner-party!")
print ("Welcome, " + (guests[2]) + " to dinner-party!")
print ("Welcome, " + (guests[3]) + " to dinner-party!")
print ("Welcome, " + (guests[4]) + " to hell-party!")
print ('SORRY, ONLY 2 GUESTS WAS INVATED TO PARTY')
first_cancelled=guests.pop(1)
print('Sorry, ' + first_cancelled.title() + ' but your invate has been cancelled')
second_cancelled=guests.pop(4)
print('Sorry, ' + second_cancelled.title() + ' but your invate has been cancelled')
third_cancelled=guests.pop(3)
print('Sorry, ' + third_cancelled.title() + ' but your invate has been cancelled')
fourth_cancelled=guests.pop(2)
print('Sorry, ' + fourth_cancelled.title() + ' but your invate has been cancelled')
print ("This message confirm, that your Mr. " + (guests[0]) + " invite to party is actually!")
print ("This message confirm, that your Mr. " + (guests[1]) + " invite to party is actually!")
del guests[:2]
print(guests)
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/names3-7.py
Welcome, DelPiero to dinner-party!
Welcome, Biden to dinner-party!
Welcome, putin to hell-party!
Welcome, DelPiero to dinner-party!
Welcome, Biden to dinner-party!
Welcome, patrushev to hell-party!
Our party will be bigger!
Welcome, Zelenskiy to dinner-party!
Welcome, DelPiero to dinner-party!
Welcome, Zaluzhnyy to dinner-party!
Welcome, Biden to dinner-party!
Welcome, patrushev to hell-party!
SORRY, ONLY 2 GUESTS WAS INVATED TO PARTY
['Zelenskiy', 'DelPiero', 'Zaluzhnyy', 'Biden', 'patrushev', 'Arestovych']
Sorry Delpiero but your invate has been cancelled
Sorry Arestovych but your invate has been cancelled
Sorry Patrushev but your invate has been cancelled
Sorry Biden but your invate has been cancelled
This message confirm, that your Mr. Zelenskiy invite to party is actually!
This message confirm, th
~~~

## Ex 3-8

~~~
countries = ['USA', 'Australia', 'Senegal', 'Brazil', 'Wales']
print(countries)
print (sorted (countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
print(countries.reverse)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print (countries)
countries.sort(reverse=True)
print (countries)
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/countries3-8.py
['USA', 'Australia', 'Senegal', 'Brazil', 'Wales']
['Australia', 'Brazil', 'Senegal', 'USA', 'Wales']
['USA', 'Australia', 'Senegal', 'Brazil', 'Wales']
['Wales', 'USA', 'Senegal', 'Brazil', 'Australia']
['USA', 'Australia', 'Senegal', 'Brazil', 'Wales']
<built-in method reverse of list object at 0x7f7d6dab7980>
['Wales', 'Brazil', 'Senegal', 'Australia', 'USA']
['USA', 'Australia', 'Senegal', 'Brazil', 'Wales']
['Australia', 'Brazil', 'Senegal', 'USA', 'Wales']
['Wales', 'USA', 'Senegal', 'Brazil', 'Australia']
~~~


## Ex 3-9

~~~
guests = ['DelPiero', 'Biden', 'putin']
number=len(guests)
print(number)
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/number3-9.py
3
~~~

## Ex 3-10

~~~
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

~~~

~~~gk-25:Python_Crash_Course_2022 tgk$ python3 Chapter3/review3-10.py
['Albania', 'Switzerland', 'France', 'Spain', 'Italy', 'England', 'Cyprus', 'Turkey', 'Germany', 'Poland', 'Neterlands']
Last country which i visited was Turkey!
['Albania', 'Switzerland', 'Egypt', 'Spain', 'Italy', 'England', 'Cyprus', 'Turkey', 'Germany', 'Poland', 'Neterlands']
['Albania', 'Switzerland', 'Egypt', 'Spain', 'Italy', 'England', 'Cyprus', 'Turkey', 'Germany', 'Poland', 'Neterlands', 'Luxembourg']
Luxembourg
['Albania', 'Cyprus', 'Egypt', 'England', 'Germany', 'Italy', 'Neterlands', 'Poland', 'Spain', 'Switzerland']
['Switzerland', 'Spain', 'Poland', 'Neterlands', 'Italy', 'Germany', 'England', 'Egypt', 'Cyprus', 'Albania']
10
~~~