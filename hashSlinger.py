#!/usr/bin/env python3
####################################################
## Author: Astrixo                                ##
## Purpose: Train password cracking               ##
####################################################

#Imports and globals
import argparse, hashlib, random, sys

REDTEXT = "\033[31m" #Wrong
GREENTEXT = "\033[32m" #Success
YELLOWTEXT = "\033[33m" #Errors :(
BLUETEXT = "\033[34m" #I just like this color
RETURNDEFAULTCOLOR = "\033[0m" #Default term color
BARRIER = "#########################################"

def pick_randomLine():
    with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='utf-8', errors='ignore') as passwordList:
        lines = passwordList.readlines()
        return random.choice(lines).strip()

def level_one():
    title = "LEVEL ONE"
    print(f'##{BLUETEXT}{title.center(len(BARRIER)-4)}{RETURNDEFAULTCOLOR}##')
    print(BARRIER)
    print('General: You will be given an MD5 Hash of a password randomly picked from the RockYou wordlist.')
    print('Instructions: Enter the plaintext password associated with this MD5 Hash.')
    print('Hint: hashcat -a 0 -m 0 <hash.txt> /usr/share/wordlists/rockyou.txt')
    print('Picking a password...')
    password = pick_randomLine()
    print('Password picked!')
    print(f'Target Hash: {hash('md5', password)}')
    guess = input("Guess: ")
    while guess != password:
        print(f'{REDTEXT}Nope, try again :) {RETURNDEFAULTCOLOR}')
        guess = input("Guess: ")
    print(f'{GREENTEXT}Correct!{RETURNDEFAULTCOLOR}')

def level_two():
    print(BARRIER)
    title = "LEVEL TWO"
    print(f'##{BLUETEXT}{title.center(len(BARRIER)-4)}{RETURNDEFAULTCOLOR}##')
    print(BARRIER)
    print('General: Good job on solving the MD5 Hash. This one is SHA256.')
    print('Instructions: Enter the plaintext password associated with this SHA256 Hash.')
    print('Hint: It will not be -m 0. It will be -m 1400')
    print('Picking a password...')
    password = pick_randomLine()
    print('Password picked!')
    print(f'Target Hash: {hash('sha256', password)}')
    guess = input("Guess: ")
    while guess != password:
        print(f'{REDTEXT}Nope, try again :){RETURNDEFAULTCOLOR}')
        guess = input("Guess: ")
    print(f'{GREENTEXT}Correct!{RETURNDEFAULTCOLOR}')

def hash(algo: str, s: str) -> str:
    try:
        return hashlib.new(algo, s.encode('utf-8')).hexdigest()
    except ValueError:
        print(f"{YELLOWTEXT}[!] Unsupported algorithm: {algo}")
        sys.exit(1)
    
def main():
    print(BARRIER)
    print(f'##{BLUETEXT} Preparing the Hash Slinger Training {RETURNDEFAULTCOLOR}##')
    print('#########################################')
    level_one()
    level_two()


if __name__ == '__main__':
    main()
