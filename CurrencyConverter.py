import requests
import csv
# import re
# import regcheck

print("This app only accepts 3-letter currency codes. refer to the following website for a list of currency codes: ")
print("http://www.nationsonline.org/oneworld/currencies.htm")

currency_code_list = []

with open(r"C:\Users\Sean\PycharmProjects\CurrencyConverter\currency_code_list.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        for item in row:
            if item.isupper() and len(item) == 3:
                # w = re.sub(r"[\(\[][A-Za-z.| \t]+[\)\]]", "", item)   --> used regex in attempt to remove brackets from country names.
                # print (w)
                currency_code_list.append(item)

def baseinput():
    global base
    base = input("Convert from: ")
    if base not in currency_code_list:
        print("That was not a proper currency code. Try again.")
        baseinput()

def targetinput():
    global target
    target = input("Convert to: ")
    if target not in currency_code_list:
        print("That was not a proper currency code. Try again.")
        targetinput()

baseinput()
targetinput()
amount = float(input("Amount: "))

url = ('https://currency-api.appspot.com/api/%s/%s.json') % (base, target)
r = requests.get(url)

exRate = r.json()["rate"]
print("Current exchange rate = " + str(exRate))
print("Converted amount = " + str(round((amount * exRate), 3)) + " " + target)