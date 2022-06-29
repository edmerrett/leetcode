import string


def encode(input_string: str, shift: int) -> str:
    '''
    Takes a string inpuit and outputs an encoded string per the shift

    Args:
        input_string: str -> Text to be encoded
        shift: int -> Number of shifts to do
    '''

    if not isinstance(input_string, str):
        return 'invalid input'
    elif not isinstance(shift, int):
        return 'invalid input'
        
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    punct_alphabet = string.punctuation

    encoded = ''
    for char in input_string:
        if char in lower_alphabet:
            current = lower_alphabet.index(char)
            new = current + shift
            encoded += lower_alphabet[new%26]
        elif char in upper_alphabet:
            current = upper_alphabet.index(char)
            new = current + shift
            encoded += upper_alphabet[new%26]
        elif char in punct_alphabet:
            current = punct_alphabet.index(char)
            new = current + shift
            encoded += punct_alphabet[new%32]
        else:
            encoded += char

    return encoded


print(encode("This is a test message from, Ed!", 7))
