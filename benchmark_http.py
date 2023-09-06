import json
import time

from web3 import Web3, IPCProvider, HTTPProvider
import random

from eth_abi import decode, encode
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



""" START ANVIL LIKE THIS
anvil --fork-url https://eth-mainnet.g.alchemy.com/v2/3d0zJXgqTEDrHY-nptBN-iJULY_DpjYc --fork-block-number 17151020 --hardfork shanghai --accounts 1 --balance 10000000000000000000 --chain-id 31337 --port 8545 --base-fee 0 --disable-block-gas-limit --no-rate-limit --ipc /tmp/anvil_debug.ipc
"""


web3 = Web3(HTTPProvider(f"http://localhost:8545"))
web3.provider.make_request("anvil_autoImpersonateAccount", [True])



with open("requests.json", "r") as f:
    txs = json.load(f)


print(f"Loaded {len(txs)} transactions")


tx = txs[0]

start_overall = time.time()
for ix, tx in enumerate(txs):
    type=tx['type']
    params=tx['params']
    if type=='eth_send':
        before = web3.eth.get_balance(params['to'])
        reciept = web3.eth.send_transaction(params)
        result = web3.eth.wait_for_transaction_receipt(reciept)
        after = web3.eth.get_balance(params['to'])
        assert after>before
    elif type=='eth_call':
        res = web3.provider.make_request("eth_call", params)
        result = decode_response(res, tx['return_types'])
        print(result)
    elif type=='eth_sendTransaction':
        tx= web3.provider.make_request("eth_sendTransaction", params)
        print(tx)
    else:
        raise ValueError(f"{type,params}")

print(f"total {round(time.time()-start_overall,2)} seconds")
