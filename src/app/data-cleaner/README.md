# Data Cleaner

A simple web tool built with Streamlit that allows users to upload, clean, edit, and convert CSV and Excel files with ease.

## Everyday Problem

Spreadsheets and exported datasets (CSV/Excel) frequently contain corrupt or duplicate records, empty cells, and unwanted columns. Opening heavy desktop spreadsheet tools just to strip duplicates or impute missing values is slow and error-prone.

## The Solution

A zero-install, browser-based data hygiene utility. Upload single or batch CSV/XLSX files, visually inspect records, remove duplicates with a single click, fill numeric blanks with column means, prune irrelevant columns, and convert between formats on export.

## Features

- Upload CSV and Excel files
- Preview and edit uploaded files directly in an interactive table
- Remove duplicate rows
- Fill missing numeric values with column means
- Select specific columns for processing
- Visualize numerical data with bar charts
- Convert files between CSV and Excel formats
- Download the processed files

## Usage & Workflow

1. Open the app via the main dashboard or run directly with Streamlit.
2. Upload CSV or Excel files using the file uploader.
3. Edit the dataset directly in the interactive table.
4. Apply data cleaning options (remove duplicates, fill missing values).
5. Select columns for further processing.
6. Visualize data and download the cleaned file in your preferred format.

## Outcome

Production-ready, standardized datasets cleaned in seconds without manual formulas or data loss.

## Dependencies

- Python
- Streamlit
- Pandas
- OpenPyXL (for Excel file handling)