from colorama import Fore
import sys

def red(text:str):     return Fore.RED    + text + Fore.WHITE
def green(text:str):   return Fore.GREEN  + text + Fore.WHITE
def blue(text:str):    return Fore.BLUE   + text + Fore.WHITE
def yellow(text:str):  return Fore.YELLOW + text + Fore.WHITE

def fast_error(text:str):
    print(red(text)); sys.exit(1)