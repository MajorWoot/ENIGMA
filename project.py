"""
CS50P Final Project: THE ENIGMA MACHINE
Author: BORIS (MajorWoot)
From: EDMONTON, ALBERTA, CANADA!
"""

"""
Future notes:
you can use 'from collections import deque .rotate to rotate the rotors.
will have to take a look and see if its faster or 'clearner' to code.
"""

import sys
import string
import re

'''
Source: https://en.wikipedia.org/wiki/Enigma_rotor_details

Each Rotor var contains a tuple of cypher text and notch position ( for next rotor advancement)

'''

rotor_1 = ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")

rotor_2 = ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")

rotor_3 = ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")

rotor_4 = ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")

rotor_5 = ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

reflector_1 = "EJMZALYXVBWFCRQUONTSPIKHGD"

reflector_2 = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

reflector_3 = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

# alpha = str(string.ascii_uppercase)

class Enigma:
    
    def __init__(self, letter, rotor_1=rotor_1, rotor_2=rotor_2, rotor_3=rotor_3, rotor_key="AAA", reflector=reflector_1, switch_dict={"A":"B"}):

        self.switch_dict = switch_dict
        self.rotor_1 = Rotor(rotor_1)
        self.rotor_2 = Rotor(rotor_2)
        self.rotor_3 = Rotor(rotor_3)
        self.rotor_key = rotor_key
        self.reflector = Reflector(reflector)
        self.letter = letter
        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                  # str(string.ascii_uppercase)

    def __str__(self):
        return f"{self.letter}, {self.rotor_1}, {self.rotor_2}, {self.rotor_3}, {self.rotor_key}, {self.reflector}, {self.switch_dict}"

    def string_format(self, input_string):
        '''
        Formats the incoming string, taking out spaces, punctuation and capitalizing entire string.
        Returns fully formated 
        '''
        input_string = input_string.strip().upper().replace(" ", "")

        punctuation = string.punctuation
        if len(input_string) > 0:
            new_string = ""
            for letter in input_string:
                if letter in punctuation:
                    pass
                else:
                    new_string += letter
            return new_string
        else:
            return input_string
    
    def full_passthrough(self):
        '''

        Simulates a full pass of electric signal though various parts of the machine.
        Returns encrypted string or decrypted string.

        P.S. The 'magic' of the Enigma machine is the settings and path for encryption and decryption are exactly the same.   

        '''
        letter = self.string_format(self.letter)
        switch = Switchboard(letter, self.switch_dict)
        letter = switch.switchboard()
        self.rotor_1.rotate_key(self._alphabet.find(self.rotor_key[0]))
        self.rotor_2.rotate_key(self._alphabet.find(self.rotor_key[1]))
        self.rotor_3.rotate_key(self._alphabet.find(self.rotor_key[2]))
        encrypted = ""
        for i in letter:
            
            self.rotor_1.rotate()
            if self.rotor_1._alphabet[0] == self.rotor_1.rotor_notch:
                self.rotor_2.rotate()
            if self.rotor_2._alphabet[0] == self.rotor_2.rotor_notch:
                self.rotor_3.rotate()
            l = self.rotor_1.rotor(i)
            l = self.rotor_2.rotor(l)
            l = self.rotor_3.rotor(l)
            l = self.reflector.reflect(l)
            l = self.rotor_3.back_rotor(l)
            l = self.rotor_2.back_rotor(l)
            l = self.rotor_1.back_rotor(l)
            encrypted += l

        switch_rev = Switchboard(encrypted, self.switch_dict)

        encrypted = switch_rev.switchboard()
    
        return encrypted

class Rotor:

    '''
    Source: https://en.wikipedia.org/wiki/Enigma_rotor_details
    Rotor turnover notch position:
    Rotor   Notch   Effect
    I	        Q	If rotor steps from Q to R, the next rotor is advanced
    II	        E	If rotor steps from E to F, the next rotor is advanced
    III	        V	If rotor steps from V to W, the next rotor is advanced
    IV	        J	If rotor steps from J to K, the next rotor is advanced
    V	        Z	If rotor steps from Z to A, the next rotor is advanced
    '''

    def __init__(self, rotor):
        """
        __init__ takes a string of rotor cypher and notch position
        saves it in 2 class variables.

        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rotor_str = rotor[0]
        self.rotor_notch = rotor[1]

        """

        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rotor_str = rotor[0]
        self.rotor_notch = rotor[1]
        # self.letter = letter
        
    def __str__(self):
        return f"Rotor {self.rotor_str} with notch {self.rotor_notch}"

    def rotor(self, letter):
        """
        rotor takes a letter and finds its index in the alphabet
        passes the index into the rotor cypher string and returns it.
        """
        index = self._alphabet.find(letter)
        return self.rotor_str[index]
    
    def back_rotor(self, letter):
        """
        back_rotor takes a letter and finds its index in the rotor cypher string
        passes the index into the alphabet string and returns is ( this is the back pass )
        """
        index = self.rotor_str.find(letter)
        return self._alphabet[index]

    def rotate(self, n=1):
        """
        takes in a default value of 1 and rotates the rotor with every call
        of the function.
        """
        self._alphabet = self._alphabet[n:] + self._alphabet[0]
        # self.rotor_str = self.rotor_str[n:] + self.rotor_str[0]
        return self._alphabet

    def rotate_key(self, n):
        """
        takes in an int value for variable n and rotates the rotor to an "n" position
        used for settings.
        """
        self._alphabet = self._alphabet[n:] + self._alphabet[:n]
        
class Reflector:

    def __init__(self, reflector):
        """
        takes in a string and assigns it to a class variable
        """
        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.reflector = reflector
        # self.letter = letter

    def __str__(self):
        return f"Reflector string: -> {self.reflector}"

    def reflect(self, letter):

        """
        takes in a letter and "reflects" it
        """

        index = self._alphabet.find(letter)
        return self.reflector[index]

class Switchboard:

    def __init__(self, input_string, switch_dict):

        """
        takes in input string and a dictionary of key pair values to swap places.
        Key = From letter, Value = To letter

        assigns them to class variables
        """

        self.input_string = input_string
        self.switch_dict = switch_dict

    def __str__(self):
        return f"Input string: -> {self.input_string}. Switches made: -> {self.switch_dict}"

    def switchboard(self):

        """
        creates a reverse dictionary from the class variable 'switch_dict'
        and appends them together to create a full dictionary of key pair 
        values that can switch it both directions.
        uses the dictionary to swap values and returns a new modified string. 
        """
        
        rev_dict = {v: k for k, v in self.switch_dict.items()}
        switch_dict = {**self.switch_dict, **rev_dict} 
        new_string = ""
        if len(switch_dict) > 0:
            for i in self.input_string:
                if i in switch_dict:
                    new_string += switch_dict[i]
                else:
                    new_string += i
            return new_string
        else:
            return self.input_string


def get_input_int(prompt="",condition=None, error=None):

    """
    takes in 3 or none custom arguments
    prompt = What will be show in the terminal
    condition = a lambda function with a condition to check the input
    error = an error message that will be shown in case condition is not met
    """

    while True:
        try:       
            response = int(input(prompt))
            # x = lambda x: x > 0 and x < 7
            # assert x(response)
            assert condition is None or condition(response)
            return response
        except KeyboardInterrupt:
            sys.exit("")
        except EOFError:
            sys.exit("")
        except:
            sys.exit(error or "Invalid entry")

def get_input_str(prompt="", condition=None, error=None):

    """
    takes in 3 or none custom arguments
    prompt = What will be show in the terminal
    condition = a lambda function with a condition to check the input
    error = an error message that will be shown in case condition is not met
    """

    while True:
        try:       
            response = str(input(prompt))
            if any(i.isdigit() for i in response):
                print(error or "Invalid entry")
            else:           
                assert condition is None or condition(response)
                return response   
        except KeyboardInterrupt:
            sys.exit("")
        except EOFError:
            sys.exit("")
        except:
            print(error or "Invalid entry")
    
def get_input_list(prompt="", error=None):

    """
    takes in 2 or none custom arguments
    prompt = What will be show in the terminal
    error = an error message that will be shown in case condition is not met
    condition is hard coded in TODO
    """

    while True:
        try:       
            response = input(prompt)
            response = response.strip()
            if re.match(r"(?:\W|^)+([a-zA-Z]{2})(?:,|$)+", response):
                response = re.findall(r"(?:\W|^)+([a-zA-Z]{2})(?:,|$)+", response)
                return response
            else:
                pass
        except KeyboardInterrupt:
            sys.exit("")
        except EOFError:
            sys.exit("")
        except:
            sys.exit(error or "Invalid entry")


def default_enigma(quick_string):

    """
    takes in a string checks that its a string and not an int and 
    side effect (prints) the default settings to screen for user to note
    returns string back to caller function
    """

    # print("Enter a string you would like to encrypt!")
    # quick_string = str(input("--->: "))
    
    
    if any(i.isdigit() for i in quick_string):
        print("Input can't contain any digits!")
        sys.exit(1)
    else:

        # quick = Enigma(quick_string)
        
        print("""Settings used:

ROTOR Position 1: 1
ROTOR Position 2: 2
ROTOR Position 3: 3
KEY for ROTOR setting: AAA
REFLECTOR # ( 1: Alpha, 2: Bravo, 3: Charlie): 1
PLUGBOARD comma separated pair values: AB
""")
        # return quick.full_passthrough()
        return quick_string
                
def custom_enigma(letter, r1, r2, r3, key, reflector, switchboard):

    """
    takes in all inputs sent from 'user_input' (letter, r1, r2, r3, key, reflector, switchboard)
    dynamically assigns them to variables (not suggested apparently)
    converts switchboard list to a tuple and then to a dictionary
    returns a tuple of converted and assigned variables back to caller function / variable
    """
    
    r1 = globals()["rotor_%s" % r1]
    
    r2 = globals()["rotor_%s" % r2]
    
    r3 = globals()["rotor_%s" % r3]
    
    key = key.upper()
    
    reflector = globals()["reflector_%s" % reflector]
    
    temp = [tuple(x.upper()) for x in switchboard]
    switchboard = dict(temp)
    return letter, r1, r2, r3, key, reflector, switchboard
    
    custom = Enigma(letter, r1, r2, r3, key, reflector, switchboard)
    return custom.full_passthrough()
   
def user_input():

    """
    prints to screen program related information and prompts for input
    2 Options using the custom 'get_input_str' function
    Quick encryption using standard settings
    Custom settings

    if option 1 
        calls custom input function 'get_input_str'
        checks if string
        sends output to 'default_enigma' function
        returns results of 'default_enigma' to caller function / variable
    
    if option 2
        calls custom input functions 'get_input_int', 'get_input_str', and 'get_input_list'
        sends variables to 'custom_enigma' function
        returns results of 'custom_enigma' to caller function / variable
    """
    
    print("Welcome to the Python version of the ENIGMA machine.")
    print("Please make your selection:")
    print("")
    print("1. Quick encryption (Use standard settings).")
    print("2. Customize settings.")
    option = get_input_int(
        "Please make your selection: ",
        condition=lambda x: x > 0 and x < 3,
        )
   
    if option == 1:
        
        print("Enter a string you would like to encrypt!")
        # quick_string = str(input("--->: "))
        quick_string = get_input_str(
            condition=lambda x: len(x) > 0,
            error="You did not enter a valid KEY"
            )
        return default_enigma(quick_string)

    elif option == 2:

        print("Select a rotor (1 - 5) for each rotor position.")
        r1 = get_input_int(
            "Enter ROTOR # for Position 1: ",
            condition=lambda x: x > 0 and x < 6,
            error="You did not enter a valid ROTOR number ( 1 - 5 )"
            )
        
        r2 = get_input_int(
            "Enter ROTOR # for Position 2: ",
            condition=lambda x: x > 0 and x < 6,
            error="You did not enter a valid ROTOR number ( 1 - 5 )"
            )
        
        r3 = get_input_int(
            "Enter ROTOR # for Position 3: ",
            condition=lambda x: x > 0 and x < 6,
            error="You did not enter a valid ROTOR number ( 1 - 5 )"
            )
        
        key = get_input_str(
            "Enter KEY for ROTOR setting ( Eg: DOG ): ",
            condition=lambda x: len(x) == 3,
            error="You did not enter a valid KEY"
            )
        key = key.upper()
        reflector = get_input_int(
            "Enter REFLECTOR # ( 1: Alpha, 2: Bravo, 3: Charlie): ",
            condition=lambda x: x > 0 and x < 4,
            error="You did not enter a valid REFLECTOR number ( 1 - 3 )"
            )
        
        switchboard = get_input_list(
            "Enter PLUGBOARD comma separated pair values. (Eg: AZ, GF etc..) -> A will be changed to Z, G to F: ",
            error="You did not enter a valid list, please follow the EXAMPLE or read the DOCUMENTATION"
            )
        letter = get_input_str(
            "Enter a string you would like to encrypt: ",
            condition=lambda x: len(x) > 0,
            error="You did not enter a valid string of text."
        )

        return custom_enigma(letter, r1, r2, r3, key, reflector, switchboard)

    else:
        sys.exit(1)     
   
def banner():

    print(r"")
    print(r"Source FIGlet-ascii font: isometric1/alpha")
    print(r"            _____                    _____                    _____                    _____                    _____                    _____           ")    
    print(r"           /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \          ")
    print(r"          /::\    \                /::\____\                /::\    \                /::\    \                /::\____\                /::\    \         ")
    print(r"         /::::\    \              /::::|   |                \:::\    \              /::::\    \              /::::|   |               /::::\    \        ")
    print(r"        /::::::\    \            /:::::|   |                 \:::\    \            /::::::\    \            /:::::|   |              /::::::\    \       ")
    print(r"       /:::/\:::\    \          /::::::|   |                  \:::\    \          /:::/\:::\    \          /::::::|   |             /:::/\:::\    \      ")
    print(r"      /:::/__\:::\    \        /:::/|::|   |                   \:::\    \        /:::/  \:::\    \        /:::/|::|   |            /:::/__\:::\    \     ")
    print(r"     /::::\   \:::\    \      /:::/ |::|   |                   /::::\    \      /:::/    \:::\    \      /:::/ |::|   |           /::::\   \:::\    \    ")
    print(r"    /::::::\   \:::\    \    /:::/  |::|   | _____    ____    /::::::\    \    /:::/    / \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \   ")
    print(r"   /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /\   \  /:::/\:::\    \  /:::/    /   \:::\ ___\  /:::/   |::::::::\    \  /:::/\:::\   \:::\    \  ")
    print(r"  /:::/__\:::\   \:::\____\/:: /    |::|   /::\____\/::\   \/:::/  \:::\____\/:::/____/  ___\:::|    |/:::/    |:::::::::\____\/:::/  \:::\   \:::\____\ ")
    print(r"  \:::\   \:::\   \::/    /\::/    /|::|  /:::/    /\:::\  /:::/    \::/    /\:::\    \ /\  /:::|____|\::/    / ~~~~~/:::/    /\::/    \:::\  /:::/    / ")
    print(r"   \:::\   \:::\   \/____/  \/____/ |::| /:::/    /  \:::\/:::/    / \/____/  \:::\    /::\ \::/    /  \/____/      /:::/    /  \/____/ \:::\/:::/    /  ")
    print(r"    \:::\   \:::\    \              |::|/:::/    /    \::::::/    /            \:::\   \:::\ \/____/               /:::/    /            \::::::/    /   ")
    print(r"     \:::\   \:::\____\             |::::::/    /      \::::/____/              \:::\   \:::\____\                /:::/    /              \::::/    /    ")
    print(r"      \:::\   \::/    /             |:::::/    /        \:::\    \               \:::\  /:::/    /               /:::/    /               /:::/    /     ")
    print(r"       \:::\   \/____/              |::::/    /          \:::\    \               \:::\/:::/    /               /:::/    /               /:::/    /      ")
    print(r"        \:::\    \                  /:::/    /            \:::\    \               \::::::/    /               /:::/    /               /:::/    /       ")
    print(r"         \:::\____\                /:::/    /              \:::\____\               \::::/    /               /:::/    /               /:::/    /        ")
    print(r"          \::/    /                \::/    /                \::/    /                \::/____/                \::/    /                \::/    /         ")
    print(r"           \/____/                  \/____/                  \/____/                                           \/____/                  \/____/          ")
    print(r"                                                                                                                                                         ")
    
def main():

    """
    main caller function
    calls the 'banner' function that prints the banner
    assigns results of 'user_input' to a variable 'x'
    checks if results are a tuple
    if yes
        takes the tuple apart and sends all values to the 'Enigma' class init
        and prints 'Enigma.full_passthrough' return
    if no
        takes the string and passes to 'Enigma' class init with defaults
        and prints 'Enigma.full_passthrough' return
    """

    banner()
    

    x = user_input()
    
    if isinstance(x, tuple):
        y = Enigma(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
        print(y.full_passthrough())
    else:
        y = Enigma(x)
        print(y.full_passthrough())





if __name__ == "__main__":
    main()
