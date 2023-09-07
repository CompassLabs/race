# race
A speed benchmark replaying transactions on a Uniswap V3 pool.

## Setup

```bash
scripts/setup.sh
```

Running this script will do 3 things:
1. Install [`foundry`](!https://book.getfoundry.sh/getting-started/installation#using-foundryup), an EVM manager which is used to fork mainnet.
2. Install `node` dependencies
3. Install `Python` dependencies

## Quick Start

1. In one terminal run:
    ```bash
    anvil --fork-url <YOUR RPC URL> --fork-block-number 17151020 --hardfork shanghai --accounts 1 --balance 10000000000000000000 --chain-id 31337 --port 8545 --base-fee 0 --disable-block-gas-limit --no-rate-limit --ipc /tmp/anvil_debug.ipc
    ```

2. Create a `.env` file and fill in the `RPC_URL` environment variable, similar to `.env.example`

3. Run:
    ```bash
    scripts/run_all.sh
    ```

## What does success look like?

You should see an output that looks something like:
```bash
➜  race git:(main) ✗ scripts/run_all.sh
RUNNING DIRECT ARCHIVE NODE REQUESTS OVER HTTP
Loaded 58 transactions
100%|███████████████████████████████████████████| 58/58 [00:07<00:00,  7.62it/s]
HTTP archive node: 7.62 seconds

RUNNING ON ANVIL LOCAL FORK OVER HTTP WITH WEB3.PY
Could not kill process on port 8545. No process running on port.
Loaded 194 transactions
100%|█████████████████████████████████████████| 194/194 [00:07<00:00, 24.38it/s]
Web3.py HTTP Anvil: 7.96 seconds

RUNNING ON ANVIL LOCAL FORK OVER AsyncHTTP WITH WEB3.PY
Process on port 8545 killed
Loaded 194 transactions
100%|█████████████████████████████████████████| 194/194 [00:07<00:00, 26.46it/s]
Web3.py AsyncHTTP Anvil: 7.34 seconds

RUNNING ON ANVIL LOCAL FORK OVER IPC WITH WEB3.PY
Process on port 8545 killed
Loaded 194 transactions
100%|█████████████████████████████████████████| 194/194 [00:07<00:00, 26.34it/s]
Web3.py IPC Anvil: 7.37 seconds
```
