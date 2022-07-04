import string

class cesarCipher():
    
    def encodeCesar(self, input_string: str, shift: int) -> str:
        '''
        Takes a string inpuit and outputs an encoded string per the shift

        Args:
            input_string: str -> Text to be encoded
            shift: int -> Number of shifts to do
        '''

        if not isinstance(input_string, str) or isinstance(shift, int):
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


    def cesarMap(self, text, shift, alphabets):
        '''
        A more complex, but logical use of maps and maketrans
        '''
        def shift_alphabet(alphabet):
            return alphabet[shift:] + alphabet[:shift]

        shifted_alphabets = tuple(map(shift_alphabet, alphabets))

        final_alphabet = ''.join(alphabets)

        final_shifted_alphabet = ''.join(shifted_alphabets)

        table = str.maketrans(final_alphabet, final_shifted_alphabet)
        
        return text.translate(table)
     


c = cesarCipher()

plain_text = input('Enter message to encrypt: ')
print(c.cesarMap(plain_text, 1, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
print(c.encodeCesar(plain_text, 7))
