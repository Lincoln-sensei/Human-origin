from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from pathlib import Path

PRIVATE_KEY_FILE = Path(".keys/private.key")

def sign(payload: bytes) -> bytes:
    private_key = Ed25519PrivateKey.from_private_bytes(PRIVATE_KEY_FILE.read_bytes())
    return private_key.sign(payload)
