dogs = [
{"name": "Bodri", "age": 9},
{"name": "Buksi", "age": 3},
{"name": "Burkus", "age": 11},
{"name": "Lolka", "age": 2},
{"name": "Killer", "age": 7},
{"name": "Alma", "age": 5},
{"name": "Korte", "age": 2},
{"name": "Morzsa", "age": 1},
]

def printer(dogs):
	for dog in dogs:
		print(dog["name"] + ", " + str(dog["age"]))

def is_in_order(this, that):
	return this["age"] < that["age"]	


print(is_in_order(dogs[1], dogs[0]))
# printer(dogs)		