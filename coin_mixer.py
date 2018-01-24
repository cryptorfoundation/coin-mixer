import random
from decimal import Decimal

BASE_DEPOSIT_ADDRESS_NAME = "deposit_address"
DEFAULT_ACCOUNT_BALANCE = 50


class CoinMixer:

    def __init__(self, coin_api,processor):
        self._processor = processor
        self._coin_api = coin_api
        self._deposit_address = None
        self.transfer_amount = None
        self._deposit_account_details = None
        self._mixer_pool_address = "MixerPoolAddress"

    def start(self):
        self._create_new_mixer_pool_deposit_address()
        self._detect_new_deposit()
        self._send_funds_to_mixer_pool()
        self._process_funds()

    def _create_new_mixer_pool_deposit_address(self):
        self._deposit_address = BASE_DEPOSIT_ADDRESS_NAME + str(random.randint(1111, 9999))
        self._coin_api.create_new_address(self._deposit_address)
        print("Please send required mixing coins to this Address: " + self._deposit_address)

    def _detect_new_deposit(self):
        received_funds = False
        while received_funds is False:
            self._deposit_account_details = self._coin_api.get_address_details(self._deposit_address)
            if Decimal(self._deposit_account_details.balance) > DEFAULT_ACCOUNT_BALANCE:
                received_funds = True
                print("Funds Received")

    def _send_funds_to_mixer_pool(self):
        self.transfer_amount = str(Decimal(self._deposit_account_details.balance) - Decimal(50))
        self._coin_api.transfer_coins_to_new_address(self._deposit_address, self._mixer_pool_address, self.transfer_amount)

    def _process_funds(self):
        print("you funds are being processed")
        self._processor.start( self.transfer_amount)
