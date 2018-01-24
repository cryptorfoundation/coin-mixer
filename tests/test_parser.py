from unittest.mock import patch
import parser
import sys


class TestParser:

    def test_get_adresses(self):
        test_args = ["program.py", "testAddress1", "testAddress2", "testAddress3"]
        with patch.object(sys, 'argv', test_args):
            expected_addresses = ["testAddress1", "testAddress2", "testAddress3"]
            assert expected_addresses == parser.Parser.get_accounts(test_args)
