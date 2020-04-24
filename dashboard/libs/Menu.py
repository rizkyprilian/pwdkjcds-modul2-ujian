import re

yes_regex = re.compile(r'(yes)|(ya)', flags = re.IGNORECASE)
no_regex = yes_regex = re.compile(r'\bno\b|\btidak\b|\b0\b|\bn\b|\bnok\b|\bga\b|\bnga\b}\bngga\b''', flags = re.IGNORECASE)

class Menu:
    def validate_input_menu(self, list_menu, command):
        try:
            command = int(command)
            list_menu[command-1]
            return command
        except:
            print('Invalid input!!')
            return False

    def validateAllowedCommand(self, command, allowList = []):
        if len(allowList) < 1:
            print('Invalid Input')
            return False
        elif command in allowList:
            return command
        else:
            print('Invalid Input')
            return False

    def validateInt(self, command, _min=None, _max=None):
        try:
            command = int(command)
            if (_min is not None) and command < _min:
                print('Invalid Input')
                return False
            if (_max is not None) and command > _max:
                print('Invalid Input')
                return False

            return command
        except:
            print('Invalid Input')
            return False

    def sanitize_yesno(self, command):
        # will return 1 for yes, 0 for no. invalid input will return false
        if (re.search('yes|ya|k|1|ok|[y]$', command, flags=re.IGNORECASE) is not None):
            return 1
        elif(re.search('no|tidak|ga|0|nok|[n]$', command, flags=re.IGNORECASE) is not None):
            return 0
        else:
            print('Invalid Input')
            return False

    def print_menu(self, list_menu):
        print('---------------------')
        for (idx, menu) in zip(range(1, len(list_menu) +1 ), list_menu):
            print('{}. {}'.format(idx, menu))
        print('\n')