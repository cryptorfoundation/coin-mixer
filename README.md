#Context
Coin Mixer Challenge
Despite some media reports, Bitcoin is not an anonymous protocol.
Instead, it's often referred to as a pseudonymous system.
All transactions to or from any Bitcoin address are publicly available, so Bitcoin's “anonymity” hinges on not knowing which addresses belong to which people.
But because Bitcoin addresses are so trivial to create (it’s essentially just a key pair), you can help ensure your anonymity by using a bunch of addresses instead of just one.



A Bitcoin mixer is one way to maintain your privacy on the Bitcoin network.  Here’s how one popular mixer works:

You provide  a list of new, unused addresses that you own to the mixer;
The mixer provides you with a new deposit address that it owns;
You transfer your bitcoins to that address;
The mixer will detect your transfer by watching or polling the P2P Bitcoin network;
The mixer will transfer your bitcoin from the deposit address into a big “house account” along with all the other bitcoin currently being mixed; and
Then, over some time the mixer will use the house account to dole out your bitcoin in smaller increments to the withdrawal addresses that you provided, possibly after deducting a fee.
There are a number of reasons to use a Bitcoin mixer. For instance, if your salary gets paid to the same Bitcoin address every two weeks, and if you buy your morning coffee using that address, it would be fairly easy for your barista to look up your previous transactions and figure out how much money you make. Using a mixer is one of the many ways to hide that transaction flow.


# Problem
  Please create a Jobcoin mixer, analogous to the Bitcoin mixer described above. You may collect a fee for your mixing service if you wish.


#Approach
  Simple commandline app that reads two new address arguments that the mixed coins will be moved to. The mixer creates a deposit account
  for the user to deposit coins to me mixed and then they are transferred to the larger pool with existing coins. Finally pushed to the
  new Addresses provided by the user.

#Security flaws
  Any user of this commandLine based mixer can be traced back to their IP. All requests sent to and from the JobCoin api
  is tied back to its IP. From a code standpoint, the application can connect via VPN to mask some traceability. Another approach is to update
  api calls to go through the tor network, to mask IPs etc. The stem module would be a great tool to incorporate into this project to do such.

  In additionally, the application does a 20 second delay between each transfer and split the amounts in half.
  In an ideal situation account transfer cadence and sizes would randomly vary.

  Ideally the user creates the new address anomalously and then uses the mixer. This helps to mask their relationship to the new addresses

##Requirments
 1. Python 3
 2. pytest version = '3.3.2'
 3. Mac OS X

## Setup

 1. To install Homebrew, open Terminal
  `$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

 2.`$ brew install python3`

 3. `pip install pytest`

## To Runt Tests
 1. Run tests:
   `$ python3 -m pytest  `

 ##  Run code
   1. python3 _main.py newAddress1 newAddress2

   2. You will then see
      `Please send required mixing coins to this Address: deposit_address2648`

   3. Send coins to the listed deposit address above




