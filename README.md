# File Integrity Checker

A simple Python cybersecurity tool that uses SHA-256 hashing
to detect whether a file has been modified.

## Features

- Creates a SHA-256 hash baseline for a file
- Checks a file against its saved baseline
- Detects when a file has been modified
- Uses Python's built-in `hashlib` module
- Uses a simple command-line interface

## How It Works

The program calculates the SHA-256 hash of a selected file
and saves it as a baseline.

When checking the file later, the program calculates the hash
again and compares it to the original baseline.

If the hashes match, the file has not changed.

If the hashes are different, the program reports that the file
may have been modified.

## Requirements

- Python 3.10 or newer

No external Python packages are required.

## How to Run

Run the program with:

```bash
python main.py