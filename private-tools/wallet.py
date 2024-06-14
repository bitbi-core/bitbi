from bitbirpc.authproxy import AuthServiceProxy, JSONRPCException
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException




# setup the connection to the Bitcoin Core node
# setup the connection to the Bitbi Core node
# setup the connection to the Bitcoin Core node
# setup the connection to the Bitcoin Core node
rpc_user = "jibuji"
rpc_user = "jibuji"
rpc_user = "jibuji"
rpc_user = "jibuji"
rpc_password = "jibujipwd"
rpc_password = "jibujipwd"
rpc_password = "jibujipwd"
rpc_password = "jibujipwd"
rpc_host = "127.0.0.1"
rpc_host = "127.0.0.1"
rpc_host = "127.0.0.1"
rpc_host = "127.0.0.1"
rpc_port = "9800"
rpc_port = "9800"
rpc_port = "9800"
rpc_port = "9800"
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")




# your descriptor
# your descriptor
# your descriptor
# your descriptor
descriptor = "wpkh(xprv9s21ZrQH143K4bx9mdfpdeJdJjY6nCQkChbMZVBikjt3iKKzezDRZP7Ef2h4Y6HrEmBKujL7dsiLyc3mrvfW43LioWyGi2bUwS6CqZgt3Gp/84h/0h/0h/0/*)#3cw0c2ke"
descriptor = "wpkh(xprv9s21ZrQH143K4bx9mdfpdeJdJjY6nCQkChbMZVBikjt3iKKzezDRZP7Ef2h4Y6HrEmBKujL7dsiLyc3mrvfW43LioWyGi2bUwS6CqZgt3Gp/84h/0h/0h/0/*)#3cw0c2ke"
descriptor = "wpkh(xprv9s21ZrQH143K4bx9mdfpdeJdJjY6nCQkChbMZVBikjt3iKKzezDRZP7Ef2h4Y6HrEmBKujL7dsiLyc3mrvfW43LioWyGi2bUwS6CqZgt3Gp/84h/0h/0h/0/*)#3cw0c2ke"
descriptor = "wpkh(xprv9s21ZrQH143K4bx9mdfpdeJdJjY6nCQkChbMZVBikjt3iKKzezDRZP7Ef2h4Y6HrEmBKujL7dsiLyc3mrvfW43LioWyGi2bUwS6CqZgt3Gp/84h/0h/0h/0/*)#3cw0c2ke"




# derive the first 1000 addresses
# derive the first 1000 addresses
# derive the first 1000 addresses
# derive the first 1000 addresses
addresses = rpc_connection.deriveaddresses(descriptor, [0, 1000])
addresses = rpc_connection.deriveaddresses(descriptor, [0, 1000])
addresses = rpc_connection.deriveaddresses(descriptor, [0, 1000])
addresses = rpc_connection.deriveaddresses(descriptor, [0, 1000])




# iterate over the addresses and check the balance
# iterate over the addresses and check the balance
# iterate over the addresses and check the balance
# iterate over the addresses and check the balance
for address in addresses:
for address in addresses:
for address in addresses:
for address in addresses:
    # get the address info
    # get the address info
    # get the address info
    # get the address info
    address_info = rpc_connection.getaddressinfo(address)
    address_info = rpc_connection.getaddressinfo(address)
    address_info = rpc_connection.getaddressinfo(address)
    address_info = rpc_connection.getaddressinfo(address)
    # print(address_info)
    # print(address_info)
    # print(address_info)
    # print(address_info)
    # check if the address has any transactions
    # check if the address has any transactions
    # check if the address has any transactions
    # check if the address has any transactions
    if address_info['ismine'] and address_info.get("txcount", 0) > 0:
    if address_info['ismine'] and address_info.get("txcount", 0) > 0:
    if address_info['ismine'] and address_info.get("txcount", 0) > 0:
    if address_info['ismine'] and address_info.get("txcount", 0) > 0:
        # get the total received by the address
        # get the total received by the address
        # get the total received by the address
        # get the total received by the address
        total_received = rpc_connection.getreceivedbyaddress(address)
        total_received = rpc_connection.getreceivedbyaddress(address)
        total_received = rpc_connection.getreceivedbyaddress(address)
        total_received = rpc_connection.getreceivedbyaddress(address)
        if total_received > 0:
        if total_received > 0:
        if total_received > 0:
        if total_received > 0:
            print(f"Address: {address}, Balance: {total_received}")            print(f"Address: {address}, Balance: {total_received}")            print(f"Address: {address}, Balance: {total_received}")            print(f"Address: {address}, Balance: {total_received}")