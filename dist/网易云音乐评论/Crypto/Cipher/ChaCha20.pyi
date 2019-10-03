from typing import Union, overload

Buffer = Union[bytes, bytearray, memoryview]

def _HChaCha20(key: Buffer, nonce: Buffer) -> bytearray: ...

class ChaCha20Cipher:
    block_size: int
    nonce: bytes

    def __init__(self, key: Buffer, nonce: Buffer) -> None: ...
    @overload
    def encrypt(self, plaintext: Buffer) -> bytes: ...
    @overload
    def encrypt(self, plaintext: Buffer, output: Union[bytearray, memoryview]) -> None: ...
    @overload
    def decrypt(self, plaintext: Buffer) -> bytes: ...
    @overload
    def decrypt(self, plaintext: Buffer, output: Union[bytearray, memoryview]) -> None: ...
    def seek(self, position: int) -> None: ...

def new(__key: Buffer, nonce: Buffer = ...) -> ChaCha20Cipher: ...

block_size: int
key_size: int
