#! /usr/bin/env python3.6
# inspired by https://github.com/riki95/Many-Time-Pad-Cracker/blob/master/cracker.py solution

import base64
import fileinput

unresolved_character = '#'


def xor(string1, string2):
    return string1 ^ string2


def is_space(rows, current, column):
    for row in rows:
        result = xor(current, row[column])
        if not (chr(result).isalpha() or result == 0):
            return False
    return True


def decode_base_64_data_file_to_bytes_list(filename):
    decoded_line = []
    with open(filename, 'r') as file:
        for line in file.read().split("\n"):
            decoded_line.append(base64.b64decode(line))
    return decoded_line


def create_empty_list_in_bytes_format(cypher_text_in_bytes):
    empty_list = []
    for line in cypher_text_in_bytes:
        empty_list.append(bytearray(bytes(unresolved_character, 'utf-8') * len(line)))
    return empty_list


def greater_line_size_from_cipher_text(lines_list_from_cipher_text):
    max_line_size = 0
    for line in lines_list_from_cipher_text:
        if len(line) > max_line_size:
            max_line_size = len(line)

    return max_line_size


def main():
    input_file = "file.txt.crypt"
    output_file = "file.txt"
    last_output_file = "last_file.txt"

    lines_from_cipher_text = decode_base_64_data_file_to_bytes_list(input_file)
    # print("cipher lines (bytes format): ", lines_from_cipher_text)

    bytes_lines = create_empty_list_in_bytes_format(lines_from_cipher_text)
    # print(bytes_lines)

    for column_pos in range(greater_line_size_from_cipher_text(lines_from_cipher_text)):

        # print(column_pos)

        cipher_text_pos = []

        for line in lines_from_cipher_text:
            if len(line) > column_pos:
                cipher_text_pos.append(line)

        for row in cipher_text_pos:
            if is_space(cipher_text_pos, row[column_pos], column_pos):
                index = 0

                for current_row in range(len(bytes_lines)):
                    if (len(bytes_lines[current_row])) != 0 and column_pos < len(bytes_lines[current_row]):
                        result = xor(row[column_pos], cipher_text_pos[index][column_pos])

                        if result == 0:
                            # probably a space
                            bytes_lines[current_row][column_pos] = ord(' ')
                        elif chr(result).isupper():
                            bytes_lines[current_row][column_pos] = ord(chr(result).lower())
                        elif chr(result).islower():
                            bytes_lines[current_row][column_pos] = ord(chr(result).upper())

                        index += 1
                # print(index)

    clear_text = "\n".join(line.decode('utf-8') for line in bytes_lines)
    # print(clear_text)

    file = open(output_file, "w")
    file.write(clear_text)
    file.close()

    print("almost clear text: \n", clear_text)

    checkWords = ("##e ", "##at ", "Ha##e#", "ha##e#", "##u ", "w#n# ", "##ere ", " # ", "##ck#r", "h#c##r#",
                  "t# ")
    repWords = ("the ", "what ", "Hacker", "hacker", "you ", "want ", "there ", " a ", "hacker", "hackers",
                "to ")

    for line in fileinput.input([output_file], inplace=True, backup='.bk'):
        # print(line.replace('##e ', 'the '), end='')
        for check, rep in zip(checkWords, repWords):
            line = line.replace(check, rep)
        print(line)


if __name__ == "__main__":
    main()
