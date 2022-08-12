import string
import re
import sys

rotor_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"

rotor_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

rotor_4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"

rotor_5 = "VZBRGITYUPSDNHLXAWMJQOFECK"

reflector_alpha = "EJMZALYXVBWFCRQUONTSPIKHGD"

reflector_beta = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

reflector_charlie = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


# for i, k in enumerate(string.ascii_lowercase):
#     print(i, k)

# newlist = {i + 1: k for i, k in enumerate(string.ascii_lowercase)}
# print(newlist)

# {
#     1: "a",
#     2: "b",
#     3: "c",
#     4: "d",
#     5: "e",
#     6: "f",
#     7: "g",
#     8: "h",
#     9: "i",
#     10: "j",
#     11: "k",
#     12: "l",
#     13: "m",
#     14: "n",
#     15: "o",
#     16: "p",
#     17: "q",
#     18: "r",
#     19: "s",
#     20: "t",
#     21: "u",
#     22: "v",
#     23: "w",
#     24: "x",
#     25: "y",
#     26: "z",
# }

# alpha = "abcdefghijklmopqrstuvwxyz"
# number = alpha.find('e')
# print(number)
# all_rotors = [rotor_1_letters, rotor_2_letters, rotor_3_letters]
# print(all_rotors)
# def encode(all_rotors, letter):
#     for rotor in all_rotors:
#         num = alpha.find(letter)
#         print(rotor[num])

# encode(all_rotors, "a")

# testing a manual switch board
# switchboard = {"a": "g", "b": "e", "c": "w"}

# def encrypt_test(string):
#     new_string = []
#     for letter in string:
#         if letter in switchboard.keys():
#             new_string.append(switchboard[f"{letter}"])
#         else:
#             new_string.append(letter)
#     print(new_string)
# # encrypt_test("abcdefg")

# # def rotor(letter, rotor):
# #     new_letter = []
# #     new_letter.append(rotor[letter])
# #     print(new_letter)

# # rotor("a", rotor_1)

# # new = rotor_1.rotate(1)
# # print(new)

# # a - y

# def rotors(letter):

#     new_val = letter
#     new_val = rotor_1[new_val]
#     print(new_val)
#     new_val = rotor_2[new_val]
#     print(new_val)
#     new_val = rotor_3[new_val]
#     print(new_val)
#     new_val = reflector[new_val]
#     print(new_val)
#     new_val = rotor_3[]
    


def string_format(input_string):
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
        return input_string  # string is empty should return error

# print(string_format("Hello, ,./how #$%@@are     you?"))






#### Doing one direction encryption is fine, but doing a " reverse look up " in a python dic is a pain.
#### this made me go towards another index style solution

# new_dict = {"A":"Z","B":"W"}

def switchboard(input_string, switch):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    input_string = string_format(input_string)
    # print(switch)

    
    new_string = ""
    if len(switch) > 0:
        for i in input_string:
            if i in switch:
                new_string += switch[i]
            else:
                new_string += i
        return new_string
    else:
        return input_string
# print(switchboard("Hello How are you, i am fine, beat your ass i will", {"A":"Z", "B":"W"}))





## FIGURED OUT REVERSE SWITCH.... What a pain
def reverse_switchboard(input_string):

    switch = {"A": "Z", "B": "W"}
    new_string = ""
    if len(switch) > 0:
        rev_switch = {v: k for k, v in switch.items()}
        for i in input_string:
            if i in rev_switch:
                new_string += rev_switch[i]
            else:
                new_string += i
        return new_string
    else:
        return input_string

    
    
# print(reverse_switchboard("Test string"))



'''
Rotor turnover notch position:

Rotor   Notch   Effect
I	        Q	If rotor steps from Q to R, the next rotor is advanced
II	        E	If rotor steps from E to F, the next rotor is advanced
III	        V	If rotor steps from V to W, the next rotor is advanced
IV	        J	If rotor steps from J to K, the next rotor is advanced
V	        Z	If rotor steps from Z to A, the next rotor is advanced

'''

# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def rotor_setting(rotor, setting=0):

#     new_string = ""
#     new_string = rotor[setting:] + rotor[:setting]
#     return new_string


# def rotate(rotor_string):
#     new_string = ""
#     new_string = rotor_string[1:] + rotor_string[0]
#     return new_string

# print(rotor_setting(alphabet))

# (self, letter, switch_dict={}, rotor_1=rotor_1, rotor_2=rotor_2, rotor_3=rotor_3, reflector=reflector_alpha):

# strings = "ab, cd"

# a = re.findall(r"(?:\W|^)+([a-zA-Z]{2})(?:,|$)+", strings)

# print(a)


# def get_input_list(prompt="", error=None):

#     while True:
#         try:       
#             response = input(prompt)
#             response = response.strip()
#             if re.match(r"(?:\W|^)+([a-zA-Z]{2})(?:,|$)+", response):
#                 response = re.findall(r"(?:\W|^)+([a-zA-Z]{2})(?:,|$)+", response)
#                 return response
#             else:
#                 pass
#         except KeyboardInterrupt:
#             sys.exit("")
#         except EOFError:
#             sys.exit("")
#         except:
#             print(error or "Invalid entry")

# print(get_input_list())

def get_input_int(prompt="", condition=None, error=None):
    while True:
        try:       
            response = int(input(prompt))
            x = lambda x: x > 0 and x < 7
            assert x(response)
            return response
        except KeyboardInterrupt:
            sys.exit("")
        except EOFError:
            sys.exit("")
        except:
            print(error or "Invalid entry")

get_input_int()


