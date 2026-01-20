import hashlib
import time
import json

def hash_content(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()

def create_record(content_bytes: bytes, entropy_hash: str, creator_pubkey_hex: str, parent=None):
    record = {
        "content_hash": hash_content(content_bytes),
        "entropy_hash": entropy_hash,
        "creator": creator_pubkey_hex,
        "parent": parent,
        "timestamp": int(time.time())
    }
    return record

def serialize(record: dict) -> bytes:
    return json.dumps(record, sort_keys=True).encode()
