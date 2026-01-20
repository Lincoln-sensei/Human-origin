from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

def verify(payload: bytes, signature: bytes, public_key_bytes: bytes) -> bool:
    try:
        pub = Ed25519PublicKey.from_public_bytes(public_key_bytes)
        pub.verify(signature, payload)
        return True
    except Exception:
        return False
