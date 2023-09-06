const Web3 = require('web3');
const axios = require('axios');
const nodeUrl = 'http://localhost:8545';

const net = require('net');
const ipcPath = '/path/to/your/hardhat.ipc'; // Replace with the actual IPC path
const web3 = new Web3.Web3('http://localhost:8545')


var data = require('./requests.json');

async function main() {
    console.log("RUNNING ON ANVIL LOCAL FORK OVER HTTP WITH WEB3.JS")
    const start = Date.now();
    for (tx of data) {
        tt = tx['type'];
        params = tx['params'];

        if (tt == 'eth_send') {
            let reciept = await web3.eth.sendTransaction(params);
        } else if (tt == 'eth_call') {
            let body = {
                jsonrpc: '2.0',
                method: 'eth_call',
                params: params,
                id: 1,
            };
            axios.post(nodeUrl, body)
                .then(response => {
                    //console.log('Response:', response.data.result);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            // console.log("RESULT", result);
        } else if (tt == 'eth_sendTransaction') {
            let body = {
                jsonrpc: '2.0',
                method: 'eth_sendTransaction',
                params: params,
                id: 1,
            };
            axios.post(nodeUrl, body)
                .then(response => {
                    //console.log('Transact Response:', response.data.result);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        } else {
            throw new Error('AAAAA!');
        }
        // console.log(tx);
    }
    const end = Date.now();
    console.log(`Web3.js HTTP Anvil: ${(end - start) / 1000} seconds\n`);

}


// Call the main function to initiate the transaction
main();