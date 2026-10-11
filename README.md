# Everyday Utilities & Productivity Suite

A centralized toolkit of essential daily utilities that every person encounters regularly—whether securing personal credentials, sharing confidential messages safely, cleaning messy spreadsheets, recovering email handles, or verifying unexpected phone numbers. 

Instead of juggling heavy desktop software, registering for single-use online accounts, or trusting third-party web scrapers with private data, this suite provides instant, private, browser-based tools for your daily digital tasks.

---

## Tool Catalog

| Tool | Everyday Problem | Solution | Outcome |
| :--- | :--- | :--- | :--- |
| **Unit Converter** | Manual arithmetic errors when converting length units across metrics. | Instant bidirectional converter between Kilometers, Meters, and Centimeters. | Real-time, error-free measurement conversions. |
| **Data Cleaner** | Messy CSV/Excel files with duplicates, missing values, and wrong formats. | Browser-based interactive table cleaner, deduplicator, mean-filler, and format converter. | Clean, standardized CSV/Excel ready for analysis. |
| **Readable Password Generator** | Unmemorizable random passwords or weak, easily cracked patterns. | Transforms personal memorable phrases into strong, leetspeak-reinforced passwords. | Memorable passwords meeting complex security criteria. |
| **Data Encryption** | Need to share sensitive secrets, passwords, or notes over unsecure channels. | Passkey-protected symmetric Fernet encryption with brute-force lockout safeguards. | Tamper-proof cipher text only unlockable with the shared passkey. |
| **Forgot Email Digits Tool** | Account lockout because you forgot the trailing numbers of your email handle. | Permutation generator that builds targeted candidate lists in batch chunks. | Fast recovery list ready for validation without guessing. |
| **Phone Number Info** | Unknown callers, ambiguous country codes, or invalid customer phone numbers. | Parsing and validation engine that surfaces country, telecom carrier, timezone, and E.164 formats. | Instant number verification and origin detection. |
| **Wearable Cheat Notes** | Smartband notification character limits cutting off incoming text. | Splits long messages into clean 130-character chunks optimized for wearable screens. | Complete, readable alerts on wearable smartbands. |

---

## Quickstart

Run the suite using `uv`:

```bash
uv run streamlit run main.py
```

Or on Windows:

```cmd
run.bat
```

Access the dashboard in your browser at `http://localhost:8501`.

---

## Project Architecture

```text
Streamlit-tools/
├── main.py                     # Global multi-page routing and sidebar navigation
├── pyproject.toml              # Dependencies managed via uv
├── run.bat                     # Windows shortcut launcher
└── src/
    ├── app/                    # Tool modules
    │   ├── data-cleaner/
    │   ├── data_encryption/
    │   ├── find-email-combos/
    │   ├── phone-number-info/
    │   ├── readable-password-generator/
    │   ├── streamlit-apps-suite/
    │   └── unit_converter/
    └── components/             # Shared UI headers, footers, and tool registry
```
