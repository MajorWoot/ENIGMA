# ENIGMA MACHINE ( Command-line program )
### By: Boris ( MajorWoot )
#### Video Demo: <URL>

## Reference Material:

    Rotor and Reflector settings were found on [Wikipedia](https://en.wikipedia.org/wiki/Enigma_rotor_details)

## Description:

    This is a re-creation of an ENIGMA Cypher machine used by the Germans in WWII written in Pyhon 3.

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
    was a series of letters that could be swaped with one another. For example a signal for a letter "A" could enter 
    the Plugboard but a letter "Z" would exit. The Rotors could also be set with an initial offset with numbers coresponding
    with the letters in the alphabet. The Rotors, Reflector rotors, and the plugboard settings were all interchangable.
    As per
    [Wikipedia](https://en.wikipedia.org/wiki/Enigma_machine#:~:text=Combining%20three%20rotors%20from%20a,quintillion%20or%20about%2067%20bits)
    the military Enigma machine had 158,962,555,217,826,360,000 different settings (nearly 159 quintillion or about 67 bits)

    Signal Path Example:

        Keyboard -> Plugboard -> Rotor 1 -> Rotor 2 -> Rotor 3 -> Reflector Rotor -> (Reverse process) -> Light Board
        
    The biggest advantage of the machine was the rotation of the Rotors with every key press the same
    letter would be encrypted to a different output. If you were to encrypt a string like "AAAAAAA",
    every "A" would give you a different letter back. (One way to test if an Enigma is a "True" Enigma machine code ;) )
    Every rotating Rotor would also have a "Notch" which would advance the next Rotor at a given position.

    This Python rendition is an atempt to modernize a piece of world history, converting electrical signal going through 
    wires and metal components into code that can be ran on any home computer. I tried to take every single mechanical piece
    and convert its workings into code. This project took a very long time in research and understanding of the innerworkings.

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
        Returns fully formated 
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
        passes the index into the alphabet string and retrurns is ( this is the back pass )
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
        takes in a string and assignes it to a class variable

        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.reflector = reflector
        """
        

