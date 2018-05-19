
#How many lists do I need?? How many could someone possibly want??
# Got it. instead of list for individual car builds. 
# Each attribute will have it's individual list and will be called 
# upon by using element ID's.

### Lists
yearList = []
makeList = []
modelList = []

### Calls for input from the user
year = input('What year car?:')
yearList.append(year)
make = input('What make car?:')
makeList.append(make)
model = input('What model car?:')
modelList.append(model)

print(yearList + makeList + modelList)

#print(yearList)
#print(makeList)
#print(modelList)

### Do they want to continue making car lists?
answer = print(input('Would you like to make another car?:\n'))
if answer == 'yes' or answer == 'y':
    print('Okay, Great.')
else: 
    print('Okay, thanks for you time.')

print(input('What year?:'))
yearList.append(year)
print(input('What make?:'))
makeList.append(make)
print(input('What model?:'))
modelList.append(model)

print(yearList)
print(makeList)
print(modelList)