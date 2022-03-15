#caracteres ANSI

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"
REVERSE = "\033[;7m"

print(BOLD + RED + "ERROR!" + RESET + "Something went wrong...")

#outra opção
from termcolor import colored

print(colored('Error Test!!!', 'red'))
print(colored('Warning Test!!!', 'yellow'))
print(colored('Success Test!!!', 'green'))