# race
A speed benchmark replaying transactions on a Uniswap V3 pool.

## Quick Start

1. In one terminal run:
    ```bash
    anvil --fork-url <YOUR RPC URL> --fork-block-number 17151020 --hardfork shanghai --accounts 1 --balance 10000000000000000000 --chain-id 31337 --port 8545 --base-fee 0 --disable-block-gas-limit --no-rate-limit --ipc /tmp/anvil_debug.ipc
    ```

2. Create a `.env` file and fill in the `RPC_URL` environment variable, similar to `.env.example`

3. Run `scripts/run_all.sh`
