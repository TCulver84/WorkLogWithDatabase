import os


class Utilities():
    """Operating functions with no business logic"""
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # if on windows 'nt'
