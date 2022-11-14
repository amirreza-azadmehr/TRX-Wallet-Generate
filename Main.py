from tronpy import Tron

client = Tron()

print('wallet :' , client.generate_address()['base58check_address'])
print('Private key :',client.generate_address()['private_key'])
