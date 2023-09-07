import json
import subprocess
import time
import os

from web3 import AsyncWeb3, Web3, AsyncHTTPProvider
import dotenv
import asyncio
from eth_abi import decode, encode
from tqdm import tqdm

dotenv.load_dotenv()
RPC_URL = os.environ.get("RPC_URL")


def encode_args(fun_sig: str, fun_args: tuple) -> str:
    """Encode function arguments."""
    arg_types = fun_sig.split("(", 1)[1].rsplit(")", 1)[0]
    if arg_types == "":
        arg_types = []
    elif arg_types[0] != "(":
        arg_types = arg_types.split(",")
    elif arg_types[0] == "(":
        arg_types = [arg_types]
    encoded_data = encode(arg_types, fun_args)
    return (Web3.keccak(text=fun_sig)[:4] + encoded_data).hex()


def decode_response(res1: dict, return_types: tuple):
    """Decode function response."""
    decoded_response = list(decode(return_types, bytes.fromhex(res1["result"][2:])))
    for i, res in enumerate(decoded_response):
        if Web3.is_address(res):
            decoded_response[i] = Web3.to_checksum_address(res)
    if len(return_types) == 1:
        return decoded_response[0]
    else:
        return tuple(decoded_response)


def anvil_cmd(port: int) -> str:
    """Get the anvil command to fork the chain at the given block number."""
    return str(
        f"anvil --fork-url {RPC_URL} --fork-block-number 17151020 --hardfork shanghai --accounts 1 --balance 10000000000000000000 --chain-id 31337 --port {port} --base-fee 0 --disable-block-gas-limit --no-rate-limit --ipc /tmp/anvil_debug.ipc"
    )


async def main():
    cmd = anvil_cmd(8545)
    if not os.path.exists("logs"):
            os.mkdir("logs")
    proc = subprocess.Popen(
        cmd.split(" "), stdout=open(f"logs/console_out_port_{8545}.txt", "w")
    )
    web3 = AsyncWeb3(AsyncHTTPProvider("http://localhost:8545"))
    while not await web3.is_connected():
        pass
    await web3.provider.make_request("anvil_autoImpersonateAccount", [True])

    with open("requests.json", "r") as f:
        txs = json.load(f)
    print(f"Loaded {len(txs)} transactions")

    start_overall = time.time()
    for tx in tqdm(txs, total=len(txs)):
        type = tx['type']
        params = tx['params']
        if type == 'eth_send':
            reciept = await web3.eth.send_transaction(params)
            result = await web3.eth.wait_for_transaction_receipt(reciept)
        elif type == 'eth_call':
            res = await web3.provider.make_request("eth_call", params)
        elif type == 'eth_sendTransaction':
            tx = await web3.provider.make_request("eth_sendTransaction", params)
        else:
            raise ValueError(f"{type,params}")

    print(f"Web3.py AsyncHTTP Anvil: {round(time.time()-start_overall,2)} seconds\n")


if __name__ == "__main__":
    print("RUNNING ON ANVIL LOCAL FORK OVER AsyncHTTP WITH WEB3.PY")
    os.system("npx kill-port 8545")
    asyncio.run(main())