# ENIGMA MACHINE ( Command-line program )
### By: Boris ( MajorWoot )
#### Video Demo: <URL>

## Reference Material:

    Rotor and Reflector settings were found on [Wikipedia](https://en.wikipedia.org/wiki/Enigma_rotor_details)

## Description:

    This is a re-creation of an ENIGMA Cypher machine used by the Germans in WWII written in Python 3.

    It uses 5 original Rotors and 3 Reflector rings.

    Rotor #	    ABCDEFGHIJKLMNOPQRSTUVWXYZ	Date Introduced	Model Name & Number
    I	        EKMFLGDQVZNTOWYHXUSPAIBRCJ	1930	Enigma      I
    II	        AJDKSIRUXBLHWTMCQGZNPYFVOE	1930	Enigma      I
    III	        BDFHJLCPRTXVZNYEIWGAKMUSQO	1930	Enigma      I
    IV	        ESOVPZJAYQUIRHXLNFTGKDCMWB	December 1938	    M3 Army
    V	        VZBRGITYUPSDNHLXAWMJQOFECK	December 1938	    M3 Army

    Reflector A	EJMZALYXVBWFCRQUONTSPIKHGD		
    Reflector B	YRUHQSLDPXNGOKMIEBFZCWVJAT		
    Reflector C	FVPJIAOYEDRZXWGCTKUQSBNMHL		


    The original encryption was done using an electrical signal that went through numerous components and displayed an
    encrypted letter on a light board. Each component excluding the keyboard had customizable settings. The Plugboard 
    was a series of letters that could be swapped with one another. For example a signal for a letter "A" could enter 
    the Plugboard but a letter "Z" would exit. The Rotors could also be set with an initial offset with numbers corresponding
    with the letters in the alphabet. The Rotors, Reflector rotors, and the plugboard settings were all interchangeable.
    As per
    [Wikipedia](https://en.wikipedia.org/wiki/Enigma_machine#:~:text=Combining%20three%20rotors%20from%20a,quintillion%20or%20about%2067%20bits)
    the military Enigma machine had 158,962,555,217,826,360,000 different settings (nearly 159 quintillion or about 67 bits)

    Signal Path Example:

        Keyboard -> Plugboard -> Rotor 1 -> Rotor 2 -> Rotor 3 -> Reflector Rotor -> (Reverse process) -> Light Board
        
    The biggest advantage of the machine was the rotation of the Rotors with every key press the same
    letter would be encrypted to a different output. If you were to encrypt a string like "AAAAAAA",
    every "A" would give you a different letter back. (One way to test if an Enigma is a "True" Enigma machine code ;) )
    Every rotating Rotor would also have a "Notch" which would advance the next Rotor at a given position.

    This Python rendition is an attempt to modernize a piece of world history, converting electrical signal going through 
    wires and metal components into code that can be ran on any home computer. I tried to take every single mechanical piece
    and convert its workings into code. This project took a very long time in research and understanding of the inner workings.

## The Code

    The program code consists of three classes:

        class Enigma:

        class Rotor:

        class Reflector:

        class Switchboard:
    
    ## Enigma:

        Enigma takes all of the settings in a form of an __init__ class function assigning values to its class variables.
        rotor_n and reflector class variables become Rotor and Reflector class instances.

        def __init__(self, letter, rotor_1=rotor_1, rotor_2=rotor_2, rotor_3=rotor_3, rotor_key="AAA", reflector=reflector_1, switch_dict={"A":"B"}):

            The default values get passed in for default encryption.

            """
            self.switch_dict = switch_dict
            self.rotor_1 = Rotor(rotor_1)
            self.rotor_2 = Rotor(rotor_2)
            self.rotor_3 = Rotor(rotor_3)
            self.rotor_key = rotor_key
            self.reflector = Reflector(reflector)
            self.letter = letter
            self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            """

        def string_format(self, input_string):
            
            '''
            Formats the incoming string, taking out spaces, punctuation and capitalizing entire string.
            Returns fully formatted 
            '''
        


        def full_passthrough(self):

            '''
            Simulates a full pass of electric signal though various parts of the machine.
            Returns encrypted string or decrypted string.

            P.S. The 'magic' of the Enigma machine is the settings and path for encryption and decryption are exactly the same.   
            '''

    ## Rotor:

        def __init__(self, rotor):

            """
            __init__ takes a string of rotor cypher and notch position
            saves it in 2 class variables.

            self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.rotor_str = rotor[0]
            self.rotor_notch = rotor[1]
            """

        def rotor(self, letter):

            """
            rotor takes a letter and finds its index in the alphabet
            passes the index into the rotor cypher string and returns it.
            """

        def back_rotor(self, letter):

            """
            back_rotor takes a letter and finds its index in the rotor cypher string
            passes the index into the alphabet string and returns is ( this is the back pass )
            """

        def rotate(self, n=1):

            """
            takes in a default value of 1 and rotates the rotor with every call
            of the function.
            """

        def rotate_key(self, n):

            """
            takes in an int value for variable n and rotates the rotor to an "n" position
            used for settings.
            """

    ## Reflector:

        def __init__(self, reflector):

            """
            takes in a string and assigns it to a class variable

            self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.reflector = reflector
            """
        
        def reflect(self, letter):

            """
            takes in a letter and "reflects" it
            """

    ## Switchboard ( Plugboard )

        def __init__(self, input_string, switch_dict):

            """
            takes in input string and a dictionary of key pair values to swap places.
            Key = From letter, Value = To letter

            assigns them to class variables

            self.input_string = input_string
            self.switch_dict = switch_dict

            """

        def switchboard(self):

            """
            creates a reverse dictionary from the class variable 'switch_dict'
            and appends them together to create a full dictionary of key pair 
            values that can switch it both directions.
            uses the dictionary to swap values and returns a new modified string.
            """

    ## Custom input functions

        Three similar input functions that take 2 or 3 custom arguments

        def get_input_int(prompt="",condition=None, error=None):

            """
            takes in 3 or none custom arguments
            prompt = What will be show in the terminal
            condition = a lambda function with a condition to check the input
            error = an error message that will be shown in case condition is not met
            """

        def get_input_list(prompt="", error=None):

            """
            takes in 2 or none custom arguments
            prompt = What will be show in the terminal
            error = an error message that will be shown in case condition is not met
            condition is hard coded in TODO
            """

        def get_input_str(prompt="", condition=None, error=None):

            """
            takes in 3 or none custom arguments
            prompt = What will be show in the terminal
            condition = a lambda function with a condition to check the input
            error = an error message that will be shown in case condition is not met
            """

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
                assigns values dynamically to variables
                sends variables to 'custom_enigma' function
                returns results of 'custom_enigma' to caller function / variable
            """

        def default_enigma(quick_string):

            """
            takes in a string checks that its a string and not an int and 
            side effect (prints) the default settings to screen for user to note
            returns string back to caller function
            """

        def custom_enigma(letter, r1, r2, r3, key, reflector, switchboard):

            """
            takes in all inputs sent from 'user_input' (letter, r1, r2, r3, key, reflector, switchboard)
            dynamically assigns them to variables (not suggested apparently)
            converts switchboard list to a tuple and then to a dictionary
            returns a tuple of converted and assigned variables back to caller function / variable
            """

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