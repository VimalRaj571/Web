import requests

def main():
	res = requests.get("http://data.fixer.io/api/latest?access_key=1432a3ced99547e70f479a1c677097f0&?base=USD&symbols=INR")
	if res.status_code != 200:
		raise Exception("Error At API endpoint")

	data = res.json()
	print(data)

if __name__ == "__main__":
	main()