# messing with dictionaries {} defined by squirly brackets
# Catherine Leddy

car = { "make": "ford", "price": 123, "owner": {"firstname": "Kate", "age" : 35}}
print(type(car))
print(car)

car['model']= 'focus'
print (car)
#make = car['make']
#notmake = car.get('makeit')
#print (type(notmake))
#print(make)

print (car["owner"]['age'])