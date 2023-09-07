# race
A speed benchmark replaying transactions on a Uniswap V3 pool.

## Setup

```bash
scripts/setup.sh
```

We recommend to use an INFURA node, alchemy rate limits will timeout the first async benchmark.

Running this script will do 3 things:
1. Install [`foundry`](!https://book.getfoundry.sh/getting-started/installation#using-foundryup), an EVM manager which is used to fork mainnet.
2. Install `node` dependencies
3. Install `Python` dependencies

## Quick Start

1. Create a `.env` file and fill in the `RPC_URL` environment variable, similar to `.env.example`

2. Run:
    ```bash
    scripts/run_all.sh
    ```

## What does success look like?

You should see an output that looks something like:
```bash
➜  race git:(main) ✗ scripts/run_all.sh
RUNNING DIRECT ARCHIVE NODE REQUESTS OVER ASYNC HTTP
Loaded 58 transactions
Async HTTP archive node: 1.31 seconds

RUNNING DIRECT ARCHIVE NODE REQUESTS OVER HTTP
Loaded 58 transactions
100%|███████████████████████████████████████████| 58/58 [00:06<00:00,  9.06it/s]
HTTP archive node: 6.41 seconds

RUNNING ON ANVIL LOCAL FORK OVER HTTP WITH WEB3.PY
Could not kill process on port 7545. No process running on port.
Loaded 194 transactions
100%|█████████████████████████████████████████| 194/194 [00:06<00:00, 27.86it/s]
Web3.py HTTP Anvil: 6.97 seconds

RUNNING ON ANVIL LOCAL FORK OVER IPC WITH WEB3.PY
Process on port 7545 killed
Loaded 194 transactions
100%|█████████████████████████████████████████| 194/194 [00:06<00:00, 32.08it/s]
Web3.py IPC Anvil: 6.05 seconds
```
