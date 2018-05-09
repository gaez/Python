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

print('How select a model:')

model = input()

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

#year = int(input('Input year desired: '))
#year = int(year) + 1
year = int(input('Input year desired: ')) + 1

print("You picked a " + str(year) + " " + make + " " + model)
