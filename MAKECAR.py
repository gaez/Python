#make = ['Acura', 'Honda', 'Bentley', 'Mazda', 'Suburu']
#model = ['TL', 'TL-S', 'Integra', 'Accord', 'Civic', 'Prelude', 'Mulsanne', 'Flying Spur' ]


#make = acura, Mazda
#model = if acura then tl, tls, Integra

#if mazda then mx6, miata, mazdaspeed





# make of car

#acura_make = 'TL', 'TL-S', 'Integra'
#honda_make = 'Civic', 'Accord', 'Prelude'
#mazda_make = 'Mx-6', 'Miata', 'Mazdaspeed'
#suburu_make = 'Impreza', 'WRX', 'WRX STi'


#make = ['Acura', 'Honda', 'Mazda', 'Suburu']

make = input("Choose a make of car: Acura, Honda, Mazda, Suburu:\n  ")

if make == 'Acura':
    print('TL, TL-S, or Integra?')
elif make == 'Honda':
    print('Civic, Accord, or Prelude?')
elif make == 'Mazda':
    print('Mx-6, Miata, or Mazdaspeed?')
elif make == 'Suburu':
    print('Impreza, WRX, or WRX STi?')

model = input('How select a model:')

#model = input()

if model == 'TL':
    print(" Acura TL")
elif model == 'TL-S':
    print(" Acurua TL-S")
elif model == 'Integra':
    print(" Acura Integra")
elif model == 'Civic':
    print(" Honda Civic")
elif model == 'Accord':
    print(" Honda Accord")
elif model == 'Prelude':
    print(' Honda Prelude')
elif model == 'Mx-6':
    print(' Mazda Mx-6')
elif model == 'Miata':
    print(' Mazda Miata')
elif model == 'Mazdaspeed':
    print(' Mazda Mazdaspeed')
elif model == 'Impreza':
    print(' Suburu Impreza')
elif model == 'WRX':
    print(' Suburu WRX')
elif model == 'WRX STi':
    print(' Suburu WRX STi')

#print('Input year desired:')

year = input('Input year desired: ')

#print("You picked a %s -whatever the car was-" % year)

print("You picked a" " " +year+ " " +make+ " " +model)

if model == 'Mazdaspeed':
    print('You must have a huge dick! 8====D')
elif model != 'Mazdaspeed':
    print('Have a good day...........\n')

import time
print(".")
time.sleep(.2)
print(".")
time.sleep(.2)
print(".")
time.sleep(.2)
print(".")
time.sleep(.2)
print(".")
time.sleep(.2)
print(".")
time.sleep(.2)
print(".")
time.sleep(.2)
print(".")
time.sleep(.2)
print(".")
time.sleep(.2)
print(".")
time.sleep(.2)


print("Wait... What's another go?\nAnd this time you can enter whatever car you desire.\n")
make2 = input('What make vehicle do you want?\n')
model2 = input('Great! Now what trim type are you looking for?\n')
print("Oh! golly Gee, the" " " +make2+ " " +model2+ " " "??" "!! You animal!")
year2 = input('And the year for that?\n')
print("For your second car you've pick a" " " +year2+ " " +make2+ " " +model2+"!")

