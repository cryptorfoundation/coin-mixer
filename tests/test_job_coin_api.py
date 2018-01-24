from mock import patch, Mock
import requests

from address_details import AddressDetails
from job_coin_api import JobCoinApi


class TestJCoinApi:

    def test_sends_required_address_to_jcoin_api(self):
        test_api = JobCoinApi()
        address = "testAddress"
        expected_url = 'http://jobcoin.gemini.com/tattle/api/addresses/testAddress'
        expected_dict = {'balance': "50", "transactions": "test"}
        mock_response = Mock()
        mock_response.json.return_value = expected_dict
        with patch.object(requests, "get", return_value=mock_response):
            test_api.get_address_details(address)

            assert requests.get.called_with(expected_url)

    def test_returns_address_details_when_sucessfull_address_request(self):
        test_api = JobCoinApi()
        address = "testAddress"
        expected_dict = {'balance': "50", "transactions": {}}
        mock_response = Mock()
        mock_response.json.return_value = expected_dict
        expected_account_details = AddressDetails(address, "50", {})
        with patch.object(requests, "get", return_value=mock_response):
            assert expected_account_details == test_api.get_address_details(address)

    def test_sends_request_for_new_address_creation(self):
        test_api = JobCoinApi()
        address = "testAddress"
        expected_url = 'https://jobcoin.gemini.com/tattle/create'
        with patch.object(requests, "get", return_value={}):
            test_api.create_new_address(address)
            params = {"address": address}
            assert requests.get.called_with(expected_url, data=params)
