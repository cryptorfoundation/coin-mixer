from decimal import Decimal
from unittest.mock import Mock, patch, call
from transaction_queue import TransactionQueue
import time


class TestTransactionQueue:

    def test_start_builds_correct_transfers(self):
        target_addresses = ["add1", "add2"]
        mock_coin_api = Mock()
        delay_rate = 0
        test_processor = TransactionQueue(target_addresses, delay_rate, mock_coin_api, "fromAddress")
        test_processor.start("175")
        calls = [call('fromAddress', 'add1', Decimal('87.5')), call('fromAddress', 'add2', Decimal('87.5'))]
        mock_coin_api.transfer_coins_to_new_address.assert_has_calls(calls)

    def test_start_transfers_with_delays_between_transactions(self):
        target_addresses = ["add1", "add2"]
        mock_coin_api = Mock()
        delay_rate = 20
        test_processor = TransactionQueue(target_addresses, delay_rate, mock_coin_api, "fromAddress")
        with patch.object(time, "sleep", return_value=None) as mock_sleep:
            test_processor.start("175")
            mock_sleep.assert_called_with(20)
