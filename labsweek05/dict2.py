# messing with dictionaries
# Catheirne Leddy

car = {"make": "fiat", "model": "punto", "price" : 10000, "tags":["pre-owned", "best buy", "dealer"] }
# four attributes to the car make,model,price and tags (tags is an array and inside the array there are strings)

#print (car)

#print out loop for certain keys: they keys are the four attributes on the car. for key in care it will print out
# make, model, price and tags
#for key in car :
#    print (key)
# in order to print out the keys and the values the code would be written as 
#for key in car:
#print (key, "have a value", car[key])

# another way to print out the values is # because thisis an array of tuples you can iterate through it like in a for loop
print (car.items())  
for pair in car.items() :
    print(pair)
    print (type(pair))
# beacuse this code gives you tuples you can do the unpacking of it 

print (car.items())
for key, value in car.items():
    print (key, "have a value", value)



