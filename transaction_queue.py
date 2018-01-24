from decimal import Decimal
import unittest.mock
import time


class TransactionQueue:

    def __init__(self, target_addresses, delay_rate, coin_api, from_address):
        self.from_address = from_address
        self._delay_rate = delay_rate
        self.coin_api = coin_api
        self.target_addresses = target_addresses

    def start(self, total_transfer_amount):
        transfers = self.build_transactions(total_transfer_amount, self.target_addresses)
        for transfer in transfers:
            address_index_one = 0
            address_index_two = 1
            self.coin_api.transfer_coins_to_new_address(self.from_address, transfer[address_index_one], transfer[address_index_two])
            time.sleep(self._delay_rate)
        print("Check your new addresses, all transfers have been sent")

    @staticmethod
    def build_transactions(total_transfer_amount, target_addresses):
        trans_actions = []
        transfer_amount = Decimal(total_transfer_amount) / Decimal(len(target_addresses))
        for address in target_addresses:
            transfer = (address, transfer_amount)
            trans_actions.append(transfer)
        return trans_actions
