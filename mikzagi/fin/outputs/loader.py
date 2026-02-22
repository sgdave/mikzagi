import pandas as pd
from pathlib import Path
import json


def load_accounts(path: Path) -> dict:
    """
    Load baseline account balances.
    Returns a normalized dict keyed by account_id.
    """
    df = pd.read_csv(path)

    required = {
        "account_id",
        "account_type",
        "currency",
        "balance",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    accounts = {}
    for _, row in df.iterrows():
        accounts[row["account_id"]] = {
            "type": row["account_type"],
            "currency": row["currency"],
            "balance": float(row["balance"]),
            "owner": row.get("owner", None),
            "notes": row.get("notes", None),
        }

    return accounts

if __name__ == "__main__":
    accounts = load_accounts(Path("fin/inputs/now.csv"))
    print(json.dumps(accounts, indent=4))
