class Flight:

	counter = 1

	def __init__(self,origin,destination,duration):
		
		# Keep Track of id number
		self.id = Flight.counter
		Flight.counter += 1

		# Keep track of passenger
		self.passengers = []

		# Detail about flight
		self.origin = origin
		self.destination = destination
		self.duration = duration

	def print_info(self):
		print("Flight origin is {origin}".format(origin=self.origin))
		print("Flight destination is {destination}".format(destination=self.destination))
		print("Flight duration is {duration}".format(duration=self.duration))

		print('')

		print("Pasengers")

		for passenger in self.passengers:
			print("{name}".format(name=passenger.name))

	def delay(self,delay):
		self.duration += delay

	def add_passenger(self,p):  # self=flight object,p=Passenger object
		self.passengers.append(p)
		p.flight_id = self.id

class Passenger:

	def __init__(self,name):
		self.name = name

def main():
	f1 = Flight(origin="New York",destination="Paris",duration=540)
	# f1 = Flight("New York","Paris",540) valid which we know the parameter order

	alice = Passenger(name="Alice")
	bob = Passenger(name="bob")
	# First create the passenger obj
	# Send the object to the 
	# flight class method
	# create the passenger maped flight

	f1.add_passenger(alice)
	f1.add_passenger(bob)

	f1.print_info()

if __name__ == '__main__':
	main()