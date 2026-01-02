import requests
import csv 

with open('exchangerate.csv', 'a') as csvFile:
    with open('currencies.txt','r') as currencyFile:

        currencies = currencyFile.readlines()
        headers = ['Base Currency', 'Currency', 'Exchange Rate']
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(headers)
        for currency in currencies:
            baseCurrency = currency.strip().replace(',','')
            url = f"https://open.er-api.com/v6/latest/{baseCurrency}"


            response = requests.get(url)

            exchangeRates = response.json()



            for currencyName,exchangeRate in exchangeRates['rates'].items():
                csvWriter.writerow([baseCurrency,currencyName,exchangeRate])

