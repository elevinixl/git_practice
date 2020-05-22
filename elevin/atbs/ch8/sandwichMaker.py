import pyinputplus as pyin

menu = {'wheat':2,'white':2,'sourdough':2,'chicken':3,
        'turkey':2,'ham':2,'cheddar':1,'Swiss':1,'mozzarella':.5,
        "mayo":.25,'mustard':.25,'lettuce':.25,'tomato':25}

sandwich = []

print('What bread do you want?')
sandwich.append(pyin.inputMenu(['wheat','white','sourdough'], numbered=True))

print('What is your choice of protein?')
sandwich.append(pyin.inputMenu(['chicken','turkey','ham'],numbered=True))

cheese = pyin.inputYesNo('Do you want cheese?\n')
if cheese == 'yes':
    print('What type of cheese would you like?')
    sandwich.append(pyin.inputMenu(['cheddar','Swiss','mozzarella'],numbered=True))

if pyin.inputYesNo('Do you want mayo?\n') == 'yes':
    sandwich.append('mayo')
if pyin.inputYesNo('Do you want mustard?\n') == 'yes':
    sandwich.append('mustard')
if pyin.inputYesNo('Do you want lettuce?\n') == 'yes':
    sandwich.append('lettuce')
if pyin.inputYesNo('Do you want tomato?\n') == 'yes':
    sandwich.append('tomato')

quantity = pyin.inputInt('How many sandwiches do you want?\n', min=1)
price = 0
for item in sandwich:
    price += menu[item]
price *= quantity

print('You ordered %s sandwich(es) with the following ingrideints:'%str(quantity))
print(','.join(sandwich))
print('The total price is $%s.'%(round(price, 2)))