import subprocess
import platform

def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        subprocess.run('cls', shell=True)
    elif system == 'Linux' or system == 'Darwin':  # Linux or macOS
        subprocess.run('clear', shell=True)