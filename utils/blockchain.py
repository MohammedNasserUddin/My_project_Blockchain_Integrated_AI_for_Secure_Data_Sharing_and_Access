import hashlib
import json
import os
from datetime import datetime

LEDGER_FILE = "ledger.json"


def calculate_hash(data):
    """Create SHA256 hash"""
    return hashlib.sha256(data.encode()).hexdigest()


def load_ledger():
    """Load existing ledger"""
    if not os.path.exists(LEDGER_FILE):
        return []

    with open(LEDGER_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


def save_ledger(ledger):
    """Save ledger to file"""
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f, indent=4)


def add_to_ledger(data):
    """Add new block to ledger"""
    ledger = load_ledger()

    previous_hash = ledger[-1]["hash"] if ledger else "0"

    block = {
        "timestamp": str(datetime.utcnow()),
        "data": data,
        "previous_hash": previous_hash,
    }

    block_string = json.dumps(block, sort_keys=True)
    block_hash = calculate_hash(block_string)

    block["hash"] = block_hash

    ledger.append(block)
    save_ledger(ledger)

    return block_hash