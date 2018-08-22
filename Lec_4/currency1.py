import requests

def main():			   #http://data.fixer.io/api/latest?access_key=1432a3ced99547e70f479a1c677097f0&symbols=INR&base=USD
	res = requests.get("http://data.fixer.io/api/latest?access_key=1432a3ced99547e70f479a1c677097f0&?base=USD&symbols=INR")
	if res.status_code != 200:
		raise Exception("Error in API End Point")
	
	data = res.json()
	rate = data["rates"]["INR"]
	print("1 USD is equal to {val}".format(val=rate))

if __name__ == '__main__':
	main()