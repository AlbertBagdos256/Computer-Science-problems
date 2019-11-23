#----------------------------#
#Unbreakable_encryption
#Author:Albert Bagdasarov
#Date: 23:11:19
#----------------------------#
from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # generate length of random bytes
    tb: bytes = token_bytes(length)
    # change this bytes v bytes str and return it
    return int.from_bytes(tb, "big")
def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes,"big")
    encrypted: int = original_key ^ dummy #XOR
    return dummy,encrypted


def decrypt(keyl: int, key2: int) -> str:
    decrypted: int = keyl ^ key2 # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+ 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    result: str = decrypt(key1, key2)
    print(result)
