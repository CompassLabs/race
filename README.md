# race
A speed benchmark replaying transactions on a Uniswap V3 pool.

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
Web3.js HTTP Anvil: 1.097 seconds

Process on port 8545 killed
RUNNING ON ANVIL LOCAL FORK OVER HTTP WITH WEB3.PY
Could not kill process on port 8545. No process running on port.
Loaded 194 transactions
Web3.py HTTP Anvil: 14.84 seconds

RUNNING ON ANVIL LOCAL FORK OVER IPC WITH WEB3.PY
Process on port 8545 killed
Loaded 194 transactions
Web3.py IPC Anvil: 11.74 seconds
```
