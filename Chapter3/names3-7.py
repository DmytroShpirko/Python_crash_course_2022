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