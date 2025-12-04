#!/usr/bin/env python3
"""
NILOY CYBER - Legal Utility Tool (safe version)
Converted from an unsafe script into a legal developer/tester utility.

Features:
- Random User Data Generator (IDs, names, emails, passwords)
- User-Agent generator (for testing only, no malicious use)
- Account creation-year heuristic (read-only, informational)
- Multi-threaded local generation and saving to CSV/TXT
- Simple interactive menu

This tool performs NO network requests and contains NO hacking/brute-force functionality.
"""

import os
import sys
import csv
import random
import string
import datetime
from concurrent.futures import ThreadPoolExecutor

# ------------------------- Configuration -------------------------
APP_NAME = "NILOY CYBER"
OUTPUT_DIR = "output"
DEFAULT_WORKERS = 8

# ------------------------- Helpers -------------------------

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


# ------------------------- User-Agent Generator -------------------------

def generate_user_agent():
    """Return a plausible, non-malicious user-agent string for testing."""
    windows_versions = ["5.1", "6.1", "6.2", "6.3", "10.0"]
    chrome_major = random.choice(list(range(70, 125)))
    webkit_minor = random.choice(range(500, 540))
    ua = (
        f"Mozilla/5.0 (Windows NT {random.choice(windows_versions)}; Win64; x64) "
        f"AppleWebKit/{webkit_minor}.36 (KHTML, like Gecko) "
        f"Chrome/{chrome_major}.0.0.0 Safari/{webkit_minor}.36"
    )
    return ua


# ------------------------- Random Data Generators -------------------------

FIRST_NAMES = [
    "Niloy", "Juned", "Rahim", "Sakib", "Fatema", "Aisha", "Karim", "Rana",
    "Tanvir", "Sumi", "Arafat", "Nusrat", "Imran", "Sadia", "Rahima"
]
LAST_NAMES = ["Ahmed", "Hossain", "Khan", "Chowdhury", "Sarker", "Das", "Roy"]
DOMAINS = ["example.com", "mail.com", "testmail.org", "demo.net"]


def random_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"


def random_email(name=None):
    if name is None:
        name = random_name()
    local = ''.join(ch for ch in name.lower().replace(' ', '') if ch.isalnum())
    suffix = random.choice(DOMAINS)
    num = random.choice(['', str(random.randint(1,9999))])
    return f"{local}{num}@{suffix}"


def random_password(length=8, strong=False):
    if strong:
        alphabet = string.ascii_letters + string.digits + string.punctuation
    else:
        alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))


def random_id(prefix='NIL', digits=6):
    return f"{prefix}{''.join(random.choice(string.digits) for _ in range(digits))}"


# ------------------------- Creation Year Heuristic (Informational) -------------------------

def creationyear(uid: str) -> str:
    """A harmless heuristic that guesses an "account creation year" based on a numeric ID format.
    This is purely informational and kept from the original code for compatibility.
    """
    uid = str(uid)
    if len(uid) == 15:
        if uid.startswith('100000'):
            return '2009-2010 (approx)'
        elif uid.startswith('10000'):
            return '2016-2021 (approx)'
        else:
            return 'unknown (approx)'
    if len(uid) in (9, 10):
        return '2008 (approx)'
    if len(uid) == 8:
        return '2007 (approx)'
    if len(uid) == 7:
        return '2006 (approx)'
    return 'unknown'


# ------------------------- Worker & Save Logic -------------------------

def generate_single_record(index=None):
    name = random_name()
    uid = random_id(prefix='NIL', digits=6)
    email = random_email(name)
    password = random_password(length=random.choice([8,10,12]), strong=random.choice([False, True]))
    ua = generate_user_agent()
    created = datetime.datetime.utcnow().isoformat() + 'Z'
    return {
        'uid': uid,
        'name': name,
        'email': email,
        'password': password,
        'user_agent': ua,
        'created_at': created,
        'creation_year_guess': creationyear(uid)
    }


def save_records_to_csv(records, filename=None):
    ensure_output_dir()
    if filename is None:
        filename = os.path.join(OUTPUT_DIR, f"niloycyber_records_{int(time.time())}.csv")
    else:
        filename = os.path.join(OUTPUT_DIR, filename)

    fieldnames = ['uid', 'name', 'email', 'password', 'user_agent', 'created_at', 'creation_year_guess']
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow(r)
    return filename


# ------------------------- Interactive Menu -------------------------
import time

def menu_generate():
    clear_screen()
    print(f"{APP_NAME} - Random User Data Generator\n")
    try:
        limit = int(input('How many records to generate? (e.g. 100): ').strip())
    except Exception:
        print('Invalid number. Returning to menu.')
        time.sleep(1)
        return

    workers = DEFAULT_WORKERS
    try:
        w = input(f"Number of worker threads [{DEFAULT_WORKERS}]: ").strip()
        if w:
            workers = max(1, int(w))
    except Exception:
        workers = DEFAULT_WORKERS

    print('\nGenerating... This is local generation only — no network activity.')
    records = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(generate_single_record, i) for i in range(limit)]
        for f in futures:
            try:
                records.append(f.result())
            except Exception:
                pass

    default_filename = f"niloycyber_{limit}_records.csv"
    saved = save_records_to_csv(records, filename=default_filename)
    print(f"\nDone. Saved {len(records)} records to: {saved}")
    input('\nPress Enter to return to the main menu...')


def menu_preview_single():
    clear_screen()
    print(f"{APP_NAME} - Preview a single generated record\n")
    rec = generate_single_record()
    for k, v in rec.items():
        print(f"{k}: {v}")
    input('\nPress Enter to return to the main menu...')


def main_menu():
    while True:
        clear_screen()
        print(f"{APP_NAME} - Safe Utility Tool\n")
        print("1) Generate random user records (save to CSV)")
        print("2) Preview a single generated record")
        print("3) Generate sample user-agent string")
        print("4) About / Credits")
        print("5) Exit")
        choice = input('\nEnter choice: ').strip()
        if choice == '1':
            menu_generate()
        elif choice == '2':
            menu_preview_single()
        elif choice == '3':
            clear_screen()
            print('Sample User-Agent:')
            print(generate_user_agent())
            input('\nPress Enter to return to the main menu...')
        elif choice == '4':
            clear_screen()
            print(f"{APP_NAME}\nLegal utility tool converted by Niloy/Juned.\nNo network or hacking features included.")
            input('\nPress Enter to return to the main menu...')
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Try again.')
            time.sleep(1)


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print('\nInterrupted by user. Exiting...')
