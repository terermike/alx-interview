#!/usr/bin/python3


def validUTF8(data):
    num_bytes = 0

    for byte in data:
        # Check if the current byte is a continuation byte
        if num_bytes == 0:
            # Count the number of bytes required for the current character
            if byte >> 7 == 0b0:
                num_bytes = 1
            elif byte >> 5 == 0b110:
                num_bytes = 2
            elif byte >> 4 == 0b1110:
                num_bytes = 3
            elif byte >> 3 == 0b11110:
                num_bytes = 4
            else:
                return False
        else:
            # Check if the byte is a continuation byte
            if byte >> 6 != 0b10:
                return False

        # Decrement the byte count for the current character
        num_bytes -= 1

    # Ensure that all characters were properly terminated
    return num_bytes == 0
