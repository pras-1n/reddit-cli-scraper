# Reddit CLI Scraper

A lightweight Python CLI tool that scrapes an entire Reddit thread (OP + recursive comments) and pipes the formatted text directly to your system clipboard.

I built this because manual copying fails on deep threads due to Reddit's lazy loading and "load more replies" API calls.

## Features
- **Bypasses Lazy Loading:** Fetches the raw JSON directly from Reddit.
- **Recursive Parsing:** Handles deeply nested comment chains automatically.
- **Auto-Copy:** content is instantly available in your clipboard (`Ctrl+V`).

## Prerequisites

You need Python 3 and the `xclip` tool for Linux clipboard access.

```bash
sudo apt install xclip
pip install requests pyperclip
```
## Usage

Run the script with the Reddit URL as an argument:

```bash
python3 main.py "https://www.reddit.com/r/SomeThread/..."
```

## License
MIT

#Installation (Optional - Global Usage)

## Optional: Add to PATH (Linux/Mac)

To run this tool from anywhere in your terminal:

1. Make the script executable:
   chmod +x main.py

2. Create a symbolic link to your bin folder:
   sudo ln -s $(pwd)/main.py /usr/local/bin/reddit-rip

3. Now you can just type:
   reddit-rip "https://reddit.com/..."
