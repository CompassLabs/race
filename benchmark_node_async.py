import json
import time
import os
from tqdm import tqdm
import dotenv
import asyncio
import aiohttp

dotenv.load_dotenv()
RPC_URL = os.environ.get("RPC_URL")


async def main():
    print("RUNNING DIRECT ARCHIVE NODE REQUESTS OVER ASYNC HTTP")

    with open("node_requests.json", "r") as f:
        txs = json.load(f)
    print(f"Loaded {len(txs)} transactions")

    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
    }
    start_overall = time.time()
    async with aiohttp.ClientSession() as client:
        tasks = []
        for tx in tqdm(txs, total=len(txs)):
            tasks.append(
                asyncio.create_task(
                    client.post(
                        RPC_URL,
                        headers=headers,
                        data=tx,
                    )
                )
            )
        await asyncio.gather(*tasks)
    print(f"Async HTTP archive node: {round(time.time()-start_overall,2)} seconds\n")



if __name__ == "__main__":
    asyncio.run(main())
