def square(x):
	return x*x

def main():
	for i in range(10):
		print('i {} this square is {}'.format(i,square(i)))

if __name__ == "__main__":
	main()