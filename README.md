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
NOTE: web3.js is running without provider. You need to pass a provider in order to interact with the network!
RUNNING ON ANVIL LOCAL FORK OVER HTTP WITH WEB3.JS
Web3.js HTTP Anvil: 3.418 seconds

RUNNING ON ANVIL LOCAL FORK OVER HTTP WITH WEB3.PY
Process on port 8545 killed
Loaded 194 transactions
Web3.py HTTP Anvil: 7.98 seconds

RUNNING ON ANVIL LOCAL FORK OVER AsyncHTTP WITH WEB3.PY
Process on port 8545 killed
Loaded 194 transactions
Web3.py AsyncHTTP Anvil: 7.87 seconds

RUNNING ON ANVIL LOCAL FORK OVER IPC WITH WEB3.PY
Process on port 8545 killed
Loaded 194 transactions
Web3.py IPC Anvil: 7.46 seconds
```
