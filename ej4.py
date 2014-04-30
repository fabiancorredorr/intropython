cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# concatena la variable cars en medio de dos strings por medio del uso de la coma
print "Hay", cars, "carros disponibles."

# concatena la variable drivers en medio de dos strings por medio del uso de la coma
print "Hay solo", drivers, "conductores disponibles."

# concatena la variable cars_not_driven en medio de dos strings por medio del uso de la coma
print "Habran", cars_not_driven, "carros vacios hoy."

# concatena la variable carpool_capacity en medio de dos strings por medio del uso de la coma
print "Podemos transportar", carpool_capacity, "personas hoy."

# concatena la variable passengers en medio de dos strings por medio del uso de la coma
print "Tenemos", passengers, "pasageros hoy ."

#cocatena la variable average_passengers_per_car en medio de dos strings por medio de el uso de la coma.
print "Llevamos cerca de ", average_passengers_per_car, "en cada carro."
