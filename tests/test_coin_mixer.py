import random
from mock import Mock, patch

from address_details import AddressDetails
from coin_mixer import CoinMixer


class TestCoinMixer:

    def test_mixer_creates_deposit_address_with_random_int(self):
        processor_mock = Mock()
        coin_api_mock = Mock()
        test_coin_mixer = CoinMixer(coin_api_mock, processor_mock)
        coin_api_mock.transfer_coins_to.return_value = None
        with patch.object(random, "randint", return_value=2):
            coin_api_mock.get_address_details.return_value = AddressDetails("testAddress", 51,
                                                                            ["testTransaction", "testTransaction"])
            test_coin_mixer.start()
            coin_api_mock.get_address_details.assert_called_with("deposit_address2")

    def test_mixer_detects_new_deposit_when_balance_increases_on_deposit_account(self):
        processor_mock = Mock()
        coin_api_mock = Mock()
        test_coin_mixer = CoinMixer(coin_api_mock, processor_mock)
        coin_api_mock.transfer_coins_to.return_value = None
        with patch.object(random, "randint", return_value=2):
            coin_api_mock.get_address_details.return_value = AddressDetails("testAddress", 51,
                                                                            ["testTransaction", "testTransaction"])
            test_coin_mixer.start()
            coin_api_mock.get_address_details.assert_called_with("deposit_address2")

    def test_mixer_sends_transfer_details_to_processor(self):
        processor_mock = Mock()
        coin_api_mock = Mock()
        test_coin_mixer = CoinMixer(coin_api_mock, processor_mock)
        coin_api_mock.transfer_coins_to.return_value = None
        coin_api_mock.get_address_details.return_value = AddressDetails("testAddress", 51,
                                                                        ["testTransaction", "testTransaction"])
        test_coin_mixer.start()
        processor_mock.start.assert_called_with('1')
