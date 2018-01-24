from coin_mixer import CoinMixer
from job_coin_api import JobCoinApi
from parser import Parser
import sys

from transaction_queue import TransactionQueue


def main():
    target_addresses = Parser.get_accounts(sys.argv)
    api = JobCoinApi()
    processor_rate = 20

    j_coin_processor = TransactionQueue(target_addresses, processor_rate, api, "MixerPoolAddress")
    j_coin_mixer = CoinMixer(api, j_coin_processor)
    j_coin_mixer.start()


if __name__ == '__main__': main()
