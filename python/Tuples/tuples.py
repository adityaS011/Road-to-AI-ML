# Tuples are immutable unlike lists i.e. unchangeable

car = ('tata','audi', 'bmw')

#get length
print(len(car))

print(car)

more_car = ('mercedez','Ferrari')
print(more_car)

cars = car + more_car
print(cars)

#accessing tuple elements using indexing  
print(cars[0])    

#getting each value of tuple in varible when length is know
(car1, car2) = more_car
print(car1)
print(car2)

print(type(car1))
print(type(more_car))