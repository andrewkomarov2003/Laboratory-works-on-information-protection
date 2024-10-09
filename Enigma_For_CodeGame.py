alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotors = ["", "", ""]

mode = input()
starting_shift = int(input())
rotors[0] = input()
rotors[1] = input()
rotors[2] = input()
message = input()

caesar_result = []
rotor_1_result = []
rotor_2_result = []
rotor_3_result = []

current_position = 0
result_message = ""

if mode == "ENCODE":
    for symbol in message:
        current_position = alphabet.index(symbol) + starting_shift

        while current_position > 25:
            current_position = current_position - 26

        starting_shift += 1
        caesar_result.append(alphabet[current_position])

    for symbol in caesar_result:
        rotor_1_result.append(rotors[0][alphabet.index(symbol)])

    for symbol in rotor_1_result:
        rotor_2_result.append(rotors[1][alphabet.index(symbol)])

    for symbol in rotor_2_result:
        rotor_3_result.append(rotors[2][alphabet.index(symbol)])

    for symbol in rotor_3_result:
        result_message += symbol

    print(result_message)

if mode == "DECODE":
    for symbol in message:
        rotor_3_result.append(symbol)

    for symbol in rotor_3_result:
        rotor_2_result.append(alphabet[rotors[2].index(symbol)])

    for symbol in rotor_2_result:
        rotor_1_result.append(alphabet[rotors[1].index(symbol)])

    for symbol in rotor_1_result:
        caesar_result.append(alphabet[rotors[0].index(symbol)])

    for symbol in caesar_result:
        current_position = alphabet.index(symbol) - starting_shift

        while current_position < 0:
            current_position = current_position + 26

        starting_shift += 1
        result_message += alphabet[current_position]

    print(result_message)
