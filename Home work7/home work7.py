import colorama

from colorama import Fore, Back, Style

print(Fore.MAGENTA + 'Це фіолетовий текст')
print(Back.BLACK + 'Тепер на чорному фоні')
print(Style.RESET_ALL)
print('Тепер нормальний текст')
