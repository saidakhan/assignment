#!/usr/bin/env python3

import collections
import concurrent.futures
import os
import subprocess
import sys
import time

# Constants

DATABASES = (
    ('WordsDict', '-d'),
    ('WordsList', '-l'),
    ('WordsSet' , '-s'),
)

# Functions

def run_once(args):
    start_time = time.time()
    command    = ['./spell_check.py'] + list(args[:-1])
    subprocess.run(command,
        stdin  = open(args[-1]),
        stdout = subprocess.DEVNULL,
    )
    return time.time() - start_time

# Main Execution

def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} path')
        sys.exit(1)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        args  = [(db_flag, sys.argv[1]) for _, db_flag in DATABASES]
        times = executor.map(run_once, args)

    for (db_name, db_flag), db_time in zip(DATABASES, times):
        print(f'{db_name:>10}: {db_time:0.2f}')

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
