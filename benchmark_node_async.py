import json
import time
import os
import dotenv
import asyncio
import aiohttp

dotenv.load_dotenv()
RPC_URL = os.environ.get("RPC_URL")
headers = {
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip",
}


async def fetch_data(tx: dict, session: aiohttp.ClientSession):
    data = json.dumps(tx)
    async with session.post(RPC_URL, headers=headers, data=data) as response:
        if response.status == 200:
            result_json = await response.json()
            return result_json
        else:
            if response.status == 429:
                print("Rate limit exceeded, exiting")
                exit()
            else:
                print(f"Error {response.status} for tx {tx['id']}")
            return None


async def main():
    print("RUNNING DIRECT ARCHIVE NODE REQUESTS OVER ASYNC HTTP")

    with open("node_requests.json", "r") as f:
        txs = json.load(f)
    print(f"Loaded {len(txs)} transactions")

    start_overall = time.time()
    async with aiohttp.ClientSession() as client:
        tasks = [fetch_data(tx, client) for tx in txs]
        responses = await asyncio.gather(*tasks)
    print(f"Async HTTP archive node: {round(time.time()-start_overall,2)} seconds\n")



if __name__ == "__main__":
    asyncio.run(main())
