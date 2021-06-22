from colorama import Fore

class admin:

    def __init__():
        pass

    def print_admin(str):
        print(f'{Fore.BLUE}\t{str}{Fore.WHITE}')

    def prefix_change(old_prefix, message):
        if len(message[len(old_prefix) + 6:].replace(' ', '')) >= 1:
            admin.print_admin(f'Prefix changed to {message[len(old_prefix) + 6:].replace(" ", "")}')
            return message[len(old_prefix) + 6:].replace(' ', '')
        
        else:
            return old_prefix