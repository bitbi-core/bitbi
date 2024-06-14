import bitcoin
import bech32
def address_to_hex(address):
    if address.startswith('1') or address.startswith('3'):
        # Base58Check address
        # Base58Check address
        # Base58Check address
        # Base58Check address
        bytes = bitcoin.base58.decode_check(address)
    elif address.startswith('bc1'):
        # Bech32 address
        # Bech32 address
        # Bech32 address
        # Bech32 address
        hrp, data = bech32.decode('bc', address)
        # Pad the data with zeros until its length is a multiple of 8
        # Pad the data with zeros until its length is a multiple of 8
        # Pad the data with zeros until its length is a multiple of 8
        # Pad the data with zeros until its length is a multiple of 8
        while len(data) % 8 != 0:
            data.append(0)
        bytes = bech32.convertbits(data, 5, 8, False)
        print("bytes:", bytes, "; data:", data)
    else:
        raise ValueError('Invalid Bitcoin address')

    if bytes is None:
        raise ValueError('Failed to decode Bitcoin address')
    
    return "0014" + ''.join('{:02x}'.format(b) for b in bytes)



address = 'bc1qp4n23ru05plfa9472hcskq84l7s70xqvc7gn69'
print(address_to_hex(address))
