# Secure Data Encryption System

A web utility for securely storing and retrieving encrypted data using passkeys. Built with [Streamlit](https://streamlit.io/) and [cryptography](https://cryptography.io/).

## Everyday Problem

Sharing sensitive information—such as database passwords, API keys, private notes, or financial details—over public chat channels or email exposes secrets in plain text.

## The Solution

A lightweight symmetric cryptographic vault. Encrypt text into ciphertext using Fernet encryption tied to a user-chosen passkey. Only recipients with the matching passkey can decrypt the message. Built-in brute-force protection locks out guessing attempts after 3 consecutive failures.

## Features

- **Encrypt and store data** with a user-defined passkey.
- **Retrieve and decrypt data** using the correct passkey.
- **Hashing** is used for passkey verification.
- **Brute-force protection**: After 3 failed attempts, reauthorization is required.

## How It Works

- Data is encrypted using a symmetric key (Fernet).
- The passkey is hashed and stored alongside the encrypted data.
- To retrieve data, the correct passkey must be provided.

## Usage & Workflow

1. **To Encrypt a Message**:
   - Enter your plain text secret into the input area.
   - Set a private passkey.
   - Click **Encrypt & Store** to generate the encrypted ciphertext.
2. **To Decrypt a Message**:
   - Select the stored item or enter the ciphertext.
   - Provide the matching passkey.
   - Click **Decrypt** to reveal the secret in plain text.
3. **Security Safeguards**:
   - Incorrect passkey entries increment a failure counter.
   - Exceeding 3 failed attempts locks retrieval until identity re-authorization.

## Outcome

Confidential text and secrets can be safely stored or passed through untrusted mediums without risk of interception.
