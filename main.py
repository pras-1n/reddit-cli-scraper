#!/usr/bin/env python3
"""
Reddit Thread Scraper
Author: Prashant Guragai (pras-1n)
Description: A CLI tool to fetch entire Reddit threads (including nested comments)
             and copy them directly to the system clipboard.
"""

import requests
import json
import sys
import pyperclip

# Increases recursion depth for deep comment threads
sys.setrecursionlimit(10000)

def get_thread_data(url):
    if not url.endswith('.json'):
        url += '.json'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: Failed to retrieve data (Status Code: {response.status_code})")
        return None
    
    return response.json()

def parse_comments(comments, level=0):
    text_output = ""
    if isinstance(comments, dict):
        if 'data' in comments and 'children' in comments['data']:
            children = comments['data']['children']
        else:
            return ""
    elif isinstance(comments, list):
        children = comments
    else:
        return ""

    for child in children:
        if child['kind'] == 't1':  # t1 is a comment
            data = child['data']
            author = data.get('author', '[deleted]')
            body = data.get('body', '[deleted]')
            score = data.get('score', 0)
            
            indent = "    " * level
            text_output += f"{indent}--------------------------------------------------\n"
            text_output += f"{indent}User: {author} (Score: {score})\n"
            text_output += f"{indent}{body}\n\n"
            
            if data.get('replies') and data['replies'] != "":
                text_output += parse_comments(data['replies']['data']['children'], level + 1)
                
    return text_output

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <URL>")
        return

    print("Fetching data from Reddit... please wait.")
    url = sys.argv[1]
    data = get_thread_data(url)
    
    if not data:
        return

    post_data = data[0]['data']['children'][0]['data']
    comments_data = data[1]['data']['children']

    title = post_data.get('title', "No Title")
    op_text = post_data.get('selftext', "")
    op_author = post_data.get('author', "[deleted]")

    final_output = ""
    final_output += f"TITLE: {title}\n"
    final_output += f"AUTHOR: {op_author}\n"
    final_output += "="*80 + "\n"
    final_output += op_text + "\n"
    final_output += "="*80 + "\n\n"
    final_output += "COMMENTS:\n\n"
    final_output += parse_comments(comments_data)

    pyperclip.copy(final_output)
    print("\nSuccess! The thread content has been copied to your clipboard.")

if __name__ == "__main__":
    main()
