import requests

def main():
	base = input("Enter First currency : ")
	symbols = input("Enter Second currency : ")
	payload={ '?base' : base,'symbols' : symbols }
	# http://data.fixer.io/api/latest?access_key=1432a3ced99547e70f479a1c677097f0&?base=USD&symbols=INR
	url = "http://data.fixer.io/api/latest?access_key=1432a3ced99547e70f479a1c677097f0"
	res = requests.get(url = url ,params=payload)
	if res.status_code != 200:
		raise Exception("Error At API Endpoint")
	
	data = res.json()
	value = data["rates"]["INR"]
	print("1 USD is roughly equal to {val}".format(val=value))

if __name__ == '__main__':
	main()