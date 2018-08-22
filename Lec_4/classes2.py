class Flight:

	def __init__(self,origin,destination,duration):
		self.origin = origin
		self.destination = destination
		self.duration = duration

	def print_info(self):
		print("Flight origin is {origin}".format(origin=self.origin))
		print("Flight origin is {destination}".format(destination=self.destination))
		print("Flight origin is {duration}".format(duration=self.duration))

def main():
	
	f1 = Flight(origin="New York",destination="Paris",duration=540)
	# f1 = Flight("New York","Paris",540) valid which we know the parameter order
	f1.print_info()


	f2 = Flight(origin="Tokyo",destination="Shanghai",duration=185)
	f2.print_info()

if __name__ == "__main__":
	main()