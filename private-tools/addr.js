const bs58check = require('bs58check');
const bs58check = require('bs58check');
const bs58check = require('bs58check');
const bs58check = require('bs58check');
let { bech32, bech32m } = require('bech32')
let { bech32, bech32m } = require('bech32')
let { bech32, bech32m } = require('bech32')
let { bech32, bech32m } = require('bech32')




function addressToHex(address) {
function addressToHex(address) {
function addressToHex(address) {
function addressToHex(address) {
    let bytes;
    let bytes;
    let bytes;
    let bytes;
    if (address.startsWith('1') || address.startsWith('3')) {
    if (address.startsWith('1') || address.startsWith('3')) {
    if (address.startsWith('1') || address.startsWith('3')) {
    if (address.startsWith('1') || address.startsWith('3')) {
        // Base58Check address
        // Base58Check address
        // Base58Check address
        // Base58Check address
        bytes = bs58check.decode(address).toString('hex');
        bytes = bs58check.decode(address).toString('hex');
        bytes = bs58check.decode(address).toString('hex');
        bytes = bs58check.decode(address).toString('hex');
    } else if (address.startsWith('bc1')) {
    } else if (address.startsWith('bc1')) {
    } else if (address.startsWith('bc1')) {
    } else if (address.startsWith('bc1')) {
        // Bech32 address
        // Bech32 address
        // Bech32 address
        // Bech32 address
        const decoded = bech32.decode(address);
        const decoded = bech32.decode(address);
        const decoded = bech32.decode(address);
        const decoded = bech32.decode(address);
        console.log("prefix: ", decoded.prefix);
        console.log("prefix: ", decoded.prefix);
        console.log("prefix: ", decoded.prefix);
        console.log("prefix: ", decoded.prefix);
        const words = bech32.fromWords(decoded.words.slice(1)); // remove the version byte
        const words = bech32.fromWords(decoded.words.slice(1)); // remove the version byte
        const words = bech32.fromWords(decoded.words.slice(1)); // remove the version byte
        const words = bech32.fromWords(decoded.words.slice(1)); // remove the version byte
        return "0014" + Buffer.from(words).toString('hex');
        return "0014" + Buffer.from(words).toString('hex');
        return "0014" + Buffer.from(words).toString('hex');
        return "0014" + Buffer.from(words).toString('hex');
    } else {
    } else {
    } else {
    } else {
        throw new Error('Invalid Bitcoin address');
        throw new Error('Invalid Bitbi address');
        throw new Error('Invalid Bitcoin address');
        throw new Error('Invalid Bitcoin address');
    }
    }
    }
    }
    return bytes;
    return bytes;
    return bytes;
    return bytes;
}
}
}
}




const address = 'bc1qc2ky0nanf5vgtqc080fawm8ep9tqk4nykummrg';
const address = 'bc1qc2ky0nanf5vgtqc080fawm8ep9tqk4nykummrg';
const address = 'bc1qc2ky0nanf5vgtqc080fawm8ep9tqk4nykummrg';
const address = 'bc1qc2ky0nanf5vgtqc080fawm8ep9tqk4nykummrg';
console.log(addressToHex(address));console.log(addressToHex(address));console.log(addressToHex(address));console.log(addressToHex(address));