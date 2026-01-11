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

# Installation (Optional - Global Usage)

1. **Clone the repository:**
   ```
   git clone https://github.com/pras-1n/reddit-cli-scraper.git
   cd reddit-cli-scraper
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script with the Reddit URL as an argument:

```
python3 main.py "https://www.reddit.com/r/CharacterRant/comments/1ppo5lf/..."
```

## Optional: Global Usage (Linux/Mac)

To run this tool from anywhere in your terminal:

1. **Make the script executable:**
   ```
   chmod +x main.py
   ```

2. **Create a symbolic link:**
   ```
   sudo ln -s $(pwd)/main.py /usr/local/bin/reddit-rip
   ```

3. **New Usage:**
   ```
   reddit-rip "YOUR_URL_HERE"
   ```
   
## License
MIT
```
