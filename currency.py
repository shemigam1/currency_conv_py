import requests

API_KEY = "fca_live_yOatVQDrQYUSoSk6AlZmdFGVZkrK3Qm9Yx27pGX9"
ENDPOINT = "https://api.freecurrencyapi.com/v1/latest?apikey={}".format(API_KEY)

CURRENCIES = ["USD", "CAD", "EUR", "GBP"]

def convert(base):
    currencies = ",".join(CURRENCIES)
    url = f"{ENDPOINT}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        # print(data)
        return data["data"]
    except Exception as e:
        print("Invalid Currency")
        return None
    

while True:
    print("Available currencies", *CURRENCIES)
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break
    amount = input("enter the amount you want to convert: ")
    amount = float(amount)
    data = convert(base)
    if not data:
        continue
    # del data(base)
    for ticker, value in data.items():
        value = float(value * amount)
        print("{}, {:.4f}".format(ticker, value))