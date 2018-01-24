import requests
from address_details import AddressDetails


class JobCoinApi:
    URL_ADDRESS = 'http://jobcoin.gemini.com/tattle/api/addresses/'
    URL_CREATE = 'https://jobcoin.gemini.com/tattle/create'
    URL_TRANSACTIONS = 'http://jobcoin.gemini.com/tattle/api/transactions'

    def get_address_details(self, address):
        try:
            response = requests.get(self.URL_ADDRESS + address).json()
            return AddressDetails(address, response['balance'], response['transactions'])
        except requests.exceptions.ConnectionError as err:
            print("Error Connecting:", err)
        except requests.exceptions.Timeout as err:
            print("Timeout Error:", err)
        except requests.exceptions.RequestException as err:
            print(" Something Else", err)

    def create_new_address(self, address):
        try:
            params = {"address": address}
            requests.post(self.URL_CREATE, data=params)
        except requests.exceptions.HTTPError as err:
            print("Http Error:", err)
        except requests.exceptions.ConnectionError as err:
            print("Error Connecting:", err)
        except requests.exceptions.Timeout as err:
            print("Timeout Error:", err)
        except requests.exceptions.RequestException as err:
            print(" Something Else", err)

    def transfer_coins_to_new_address(self, from_address, to_address, amount):
        try:
            params = {"fromAddress": from_address, "toAddress": to_address, "amount": amount}
            r = requests.post(self.URL_TRANSACTIONS, data=params)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print("Http Error:", err)
        except requests.exceptions.ConnectionError as err:
            print("Error Connecting:", err)
        except requests.exceptions.Timeout as err:
            print("Timeout Error:", err)
        except requests.exceptions.RequestException as err:
            print(" Something Else", err)
