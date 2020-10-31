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