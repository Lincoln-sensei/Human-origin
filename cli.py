import sys
from identity import generate_identity
from record import create_record, serialize
from sign import sign
from verify import verify
from pathlib import Path

PUBLIC_KEY_FILE = Path(".keys/public.key")

def main():
    cmd = sys.argv[1]

    if cmd == "init":
        generate_identity()
        print("identity_created")

    elif cmd == "sign":
        content = sys.argv[2].encode()
        entropy = sys.argv[3]
        pubkey = PUBLIC_KEY_FILE.read_bytes().hex()

        record = create_record(content, entropy, pubkey)
        payload = serialize(record)
        signature = sign(payload)

        print(payload.decode())
        print(signature.hex())

    elif cmd == "verify":
        payload = bytes.fromhex(sys.argv[2])
        signature = bytes.fromhex(sys.argv[3])
        pubkey = PUBLIC_KEY_FILE.read_bytes()

        print(verify(payload, signature, pubkey))

    else:
        raise RuntimeError("unknown_command")

if __name__ == "__main__":
    main()
