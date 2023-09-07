import json
import time
import os
import requests
from tqdm import tqdm
import dotenv

dotenv.load_dotenv()
RPC_URL = os.environ.get("RPC_URL")


if __name__ == "__main__":
    print("RUNNING DIRECT ARCHIVE NODE REQUESTS OVER HTTP")

    with open("node_requests.json", "r") as f:
        txs = json.load(f)
    print(f"Loaded {len(txs)} transactions")

    session = requests.Session()
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
    }
    start_overall = time.time()
    for tx in tqdm(txs, total=len(txs)):
        session.post(
            RPC_URL,
            headers=headers,
            data=tx,
        )

    print(f"HTTP archive node: {round(time.time()-start_overall,2)} seconds\n")
