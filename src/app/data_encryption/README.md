# Data Encryption

## Everyday Problem

Sharing sensitive information—such as database passwords, API keys, private notes, or financial details—over public chat channels or email exposes secrets in plain text.

## The Solution

A lightweight symmetric cryptographic vault. Encrypt text into ciphertext using Fernet encryption tied to a user-chosen passkey. Only recipients with the matching passkey can decrypt the message. Built-in brute-force protection locks out guessing attempts after 3 consecutive failures.

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
