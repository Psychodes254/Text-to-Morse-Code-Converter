# Morse code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
}

# Loop List
morse_to_text_dict = {v: k for k, v in morse_code_dict.items()}

# Access User Input
user_input = input("Type M for text to Morse or T for Morse to Text: ").upper()

if user_input == "M":

    text_input = input("Enter the text you want to convert to Morse Code? ").upper()

    morse_code = []
    for char in text_input:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        elif char == ' ':
            morse_code.append("/")

    morse_code_string = ' '.join(morse_code)
    print(f"Morse Code Output: {morse_code_string}")

elif user_input == "T":

    morse_input = input("Enter the Morse Code you want to convert to text (use '/' for spaces between words): ")

    words = morse_input.split(' / ')

    text = []
    for word in words:
        morse_symbol = word.split(' ')
        for symbol in morse_symbol:
            if symbol in morse_to_text_dict:
                text.append(morse_to_text_dict[symbol])

    text_code_string = ' '.join(text)
    print(f"Decoded text: {text_code_string.lower()}")
