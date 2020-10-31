import subprocess
import sys
import get_pip
import os
import importlib
import contextlib

def install(package):

    # installs packages using pip
    # parameter of package: string

    subprocess.call([sys.executable, "-m", "pip", "install", package])

required = []
failed = []

# Try to open requirements.txt file and read all required packages
try:
    file = open("requirements.txt", "r")
    file_lines = file.readlines()
    required = [line.strip().lower() for line in file_lines]
    file.close()
except FileNotFoundError:
    print("[ERROR] No requirement.txt file found")

if len(required) > 0:
    print("[INPUT] You are about to install", len(required), "packages, would you like to proceed (y/n):", end=" ")
    ans = input()